import ollama
import json
import time
import re
import pandas as pd
from io import StringIO

def load_test_data(filepath: str) -> list:
    """Loads the test dataset from a JSON file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file '{filepath}' is not a valid JSON file.")
        return []

def test_llm_model(model_name: str, test_data: list) -> list:
    """
    Tests a specified Ollama model against a dataset and returns performance metrics.

    Args:
        model_name: The name of the Ollama model to test (e.g., 'gemma:2b').
        test_data: A list of test cases, where each case is a dictionary.

    Returns:
        A list of dictionaries, where each dictionary contains the test results
        for a single test case.
    """
    results = []
    print(f"\n--- Testing Model: {model_name} ---")

    for i, item in enumerate(test_data):
        inputs = item['inputs']
        ideal_recommendations = item['ideal_recommendations']

        # Construct a clear prompt for the model
        prompt = (
            f"Based on the following context, suggest three event ideas for a user of the Declic app.\n"
            f"Context:\n"
            f"- Location: {inputs['location']}\n"
            f"- Time: {inputs['time']}\n"
            f"- Mood: {inputs['mood']}\n"
            f"- User Query: \"{inputs['user_prompt']}\"\n"
            f"Provide only the list of suggestions."
        )

        try:
            start_time = time.time()
            response = ollama.chat(
                model=model_name,
                messages=[{'role': 'user', 'content': prompt}]
            )
            end_time = time.time()

            generated_text = response['message']['content']
            processing_time = round(end_time - start_time, 2)

            # Calculate match score based on keywords
            match_score = 0
            ideal_keywords = set(re.split(r'\s+', ' '.join(ideal_recommendations).lower()))
            # Remove generic words from keywords to improve matching
            ideal_keywords -= {'a', 'an', 'the', 'in', 'on', 'at', 'for', 'with', 'and', 'or', 'events', 'nearby'}

            for keyword in ideal_keywords:
                if keyword in generated_text.lower():
                    match_score += 1
            
            response_length = len(generated_text)
            
            # Add new metrics
            # Performance score: rewards higher match scores achieved in less time.
            performance_score = (match_score / processing_time) if processing_time > 0 else 0
            
            # Relevance density: measures how many matching keywords appear per 100 characters.
            relevance_density = (match_score / response_length) * 100 if response_length > 0 else 0


            # Store result
            results.append({
                'test_case_id': item['test_case_id'],
                'model': model_name,
                'prompt': prompt,
                'ideal_recommendations': ideal_recommendations,
                'generated_text': generated_text.strip(),
                'match_score': match_score,
                'processing_time_seconds': processing_time,
                'response_length_chars': response_length,
                'performance_score': round(performance_score, 2),
                'relevance_density_percent': round(relevance_density, 2)
            })
            print(f"  Completed test case {i+1}/{len(test_data)}: {item['test_case_id']}")

        except Exception as e:
            print(f"An error occurred while testing {model_name} on case {item['test_case_id']}: {e}")
            results.append({
                'test_case_id': item['test_case_id'],
                'model': model_name,
                'error': str(e)
            })

    return results

def generate_report(results: list, output_filename: str = 'llm_performance_report.md'):
    """Generates a Markdown report from the test results."""
    print(f"\n--- Generating Performance Report ---")
    
    # Convert results to a pandas DataFrame for easier analysis
    df = pd.DataFrame(results)
    
    if df.empty or 'error' in df.columns and df['error'].notna().all():
        print("No valid results to generate a report.")
        return

    # Create a buffer to write the report to
    report_buffer = StringIO()
    
    report_buffer.write("# LLM Performance Comparison Report\n\n")
    report_buffer.write("This report details the performance of several lightweight LLMs for the Declic app's recommendation engine.\n\n")

    # --- Summary Section ---
    report_buffer.write("## 1. Overall Performance Summary\n\n")
    summary = df.groupby('model').agg(
        avg_match_score=('match_score', 'mean'),
        avg_processing_time=('processing_time_seconds', 'mean'),
        avg_response_length=('response_length_chars', 'mean'),
        avg_performance_score=('performance_score', 'mean'),
        avg_relevance_density=('relevance_density_percent', 'mean')
    ).round(2).reset_index()

    report_buffer.write(summary.to_markdown(index=False))
    report_buffer.write("\n\n")
    
    # --- Best in Class Section ---
    report_buffer.write("## 2. Best in Class\n\n")
    best_in_class = {
        "Fastest Model (Lowest Avg. Time)": summary.loc[summary['avg_processing_time'].idxmin()],
        "Most Relevant (Highest Avg. Match Score)": summary.loc[summary['avg_match_score'].idxmax()],
        "Most Efficient (Highest Avg. Performance Score)": summary.loc[summary['avg_performance_score'].idxmax()],
        "Most Concise & Relevant (Highest Avg. Relevance Density)": summary.loc[summary['avg_relevance_density'].idxmax()]
    }

    for category, model_data in best_in_class.items():
        report_buffer.write(f"**{category}:** `{model_data['model']}`\n")
    report_buffer.write("\n")

    # --- Detailed Results Section ---
    report_buffer.write("## 3. Detailed Results per Test Case\n\n")
    for test_id, group in df.groupby('test_case_id'):
        report_buffer.write(f"### Test Case: `{test_id}`\n\n")
        
        # Display ideal recommendations for context
        ideal_rec_list = group['ideal_recommendations'].iloc[0]
        report_buffer.write(f"**Ideal Recommendations:** {', '.join(ideal_rec_list)}\n\n")

        # Table with results for this test case
        details_table = group[[
            'model', 
            'match_score', 
            'processing_time_seconds', 
            'performance_score', 
            'generated_text'
        ]].copy()
        details_table['generated_text'] = details_table['generated_text'].str.slice(0, 100) + '...'
        report_buffer.write(details_table.to_markdown(index=False))
        report_buffer.write("\n\n")

    # --- Conclusion ---
    report_buffer.write("## 4. Conclusion\n\n")
    report_buffer.write("Based on the analysis, the choice of the best model depends on the primary business objective:\n\n")
    report_buffer.write(f"- **For Maximum Speed:** `{best_in_class['Fastest Model (Lowest Avg. Time)']['model']}` is the clear winner, offering the quickest responses.\n")
    report_buffer.write(f"- **For Maximum Relevance:** `{best_in_class['Most Relevant (Highest Avg. Match Score)']['model']}` provides the most accurate suggestions according to the ideal keywords.\n")
    report_buffer.write(f"- **For a Balanced Approach:** `{best_in_class['Most Efficient (Highest Avg. Performance Score)']['model']}` offers the best trade-off between relevance and speed.\n\n")
    report_buffer.write("Further analysis should consider the qualitative aspects of the generated text.\n")
    
    # Write the buffer to a file
    with open(output_filename, 'w') as f:
        f.write(report_buffer.getvalue())
    
    print(f"Report successfully generated: '{output_filename}'")


def main():
    """Main function to run the model testing suite."""
    models_to_test = [
        "gemma:2b",
        "phi",
        "qwen:1.8b",
        "tinyllama",
        "deepseek-coder:1.3b",
        "stablelm2:1.6b", # NEW
        "tinydolphin"       # NEW
    ]
    test_data_filepath = 'test_data.json'
    results_filepath = 'test_results.json'
    report_filepath = 'llm_performance_report.md'
    all_results = []

    # Load the dataset
    test_data = load_test_data(test_data_filepath)
    if not test_data:
        return

    # Test each model
    for model in models_to_test:
        model_results = test_llm_model(model, test_data)
        all_results.extend(model_results)

    # Save the full raw results to a JSON file
    with open(results_filepath, 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f"\nFull raw results have been saved to '{results_filepath}'")
    
    # Generate the markdown report
    generate_report(all_results, report_filepath)

if __name__ == '__main__':
    main()
