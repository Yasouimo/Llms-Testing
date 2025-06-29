import ollama
import json
import time
import re
import pandas as pd 

# --- Configuration ---
# Dictionary to store the parameter count (in billions) for each model.
# This is crucial for calculating our new efficiency metric.
MODEL_PARAMS = {
    "gemma:2b": 2.0,
    "phi": 2.7,
    "qwen:1.8b": 1.8,
    "tinyllama": 1.1,
    "deepseek-coder:1.3b": 1.3,
    "stablelm2:1.6b": 1.6,
    "tinydolphin": 2.8
}

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
    Now simplified to return only the core metrics we need.

    Args:
        model_name: The name of the Ollama model to test.
        test_data: A list of test cases from the JSON file.

    Returns:
        A list of dictionaries with the raw results for each test case.
    """
    results = []
    print(f"\n--- Testing Model: {model_name} ---")

    for i, item in enumerate(test_data):
        inputs = item['inputs']
        ideal_recommendations = item['ideal_recommendations']
        prompt = (
            f"Based on the context, suggest three event ideas for the Declic app.\n"
            f"Context: Location: {inputs['location']}, Time: {inputs['time']}, Mood: {inputs['mood']}, Query: \"{inputs['user_prompt']}\"\n"
            f"Provide only a numbered list of suggestions."
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

            # Simple keyword match score for a basic idea of relevance.
            match_score = 0
            ideal_keywords = set(re.split(r'\s+', ' '.join(ideal_recommendations).lower()))
            ideal_keywords -= {'a', 'an', 'the', 'in', 'on', 'at', 'for', 'with', 'and', 'or', 'events', 'nearby'}
            for keyword in ideal_keywords:
                if keyword in generated_text.lower():
                    match_score += 1

            results.append({
                'model': model_name,
                'match_score': match_score,
                'processing_time_seconds': processing_time,
            })
            print(f"  Completed test case {i+1}/{len(test_data)}")

        except Exception as e:
            print(f"An error occurred while testing {model_name} on case {item['test_case_id']}: {e}")
            results.append({'model': model_name, 'error': str(e)})

    return results

def main():
    """
    Main function to run the model testing suite and print a summary report
    directly to the terminal.
    """
    models_to_test = [
        "gemma:2b",
        "phi",
        "qwen:1.8b",
        "tinyllama",
        "deepseek-coder:1.3b",
        "stablelm2:1.6b",
        "tinydolphin"
    ]
    test_data_filepath = 'test_data.json'
    all_results = []

    test_data = load_test_data(test_data_filepath)
    if not test_data:
        return

    # Test each model and collect results
    for model in models_to_test:
        if model not in MODEL_PARAMS:
            print(f"Warning: Parameter count for '{model}' not found. Skipping.")
            continue
        model_results = test_llm_model(model, test_data)
        all_results.extend(model_results)

    # --- Generate Terminal Report ---
    if not all_results:
        print("No results to report.")
        return
        
    df = pd.DataFrame(all_results)
    if 'error' in df.columns:
        df = df.dropna(subset=['match_score']) # Ignore failed runs for summary

    # Calculate average metrics
    summary = df.groupby('model').agg(
        avg_match_score=('match_score', 'mean'),
        avg_time_sec=('processing_time_seconds', 'mean')
    ).reset_index()

    # Add parameter count from our dictionary
    summary['params_billions'] = summary['model'].map(MODEL_PARAMS)

    # Calculate the new 'Efficiency Score'
    # This score balances relevance and speed against the model's size. Higher is better.
    summary['efficiency_score'] = \
        (summary['avg_match_score'] / summary['avg_time_sec']) / summary['params_billions']
    
    # Clean up the report for display
    summary = summary.round(2)
    summary = summary.sort_values(by='efficiency_score', ascending=False)
    summary = summary[[
        'model',
        'params_billions',
        'avg_time_sec',
        'avg_match_score',
        'efficiency_score'
    ]]

    # Print the final, simple report to the terminal
    print("\n\n--- LLM Performance & Efficiency Report ---")
    print("Models are ranked by 'efficiency_score' (higher is better).")
    print(summary.to_string(index=False))
    print("\n'efficiency_score' = (Avg Match Score / Avg Time) / Parameters\n")


if __name__ == '__main__':
    main()
