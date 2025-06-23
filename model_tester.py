import ollama
import json
import time
import re

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

            # Calculate match score
            match_score = 0
            # Clean and tokenize ideal recommendations to get keywords
            ideal_keywords = set(re.split(r'\s+', ' '.join(ideal_recommendations).lower()))

            for keyword in ideal_keywords:
                if keyword in generated_text.lower():
                    match_score += 1

            # Store result
            results.append({
                'test_case_id': item['test_case_id'],
                'model': model_name,
                'prompt': prompt,
                'ideal_recommendations': ideal_recommendations,
                'generated_text': generated_text.strip(),
                'match_score': match_score,
                'processing_time_seconds': processing_time,
                'response_length_chars': len(generated_text)
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

def main():
    """Main function to run the model testing suite."""
    models_to_test = [
        "gemma:2b",
        "phi",
        "qwen:1.8b",
        "tinyllama"
    ]
    test_data_filepath = 'test_data.json'
    all_results = []

    # Load the dataset
    test_data = load_test_data(test_data_filepath)
    if not test_data:
        return

    # Test each model
    for model in models_to_test:
        model_results = test_llm_model(model, test_data)
        all_results.extend(model_results)

    # Print a summary of the results
    print("\n--- Test Summary ---")
    for result in all_results:
        if 'error' in result:
            print(f"Model: {result['model']}, Case: {result['test_case_id']}, Error: {result['error']}")
        else:
            print(
                f"Model: {result['model']:<12} | "
                f"Case: {result['test_case_id']:<25} | "
                f"Match Score: {result['match_score']:<2} | "
                f"Time: {result['processing_time_seconds']:<5}s | "
                f"Output: \"{result['generated_text'][:80]}...\""
            )
            
    # You can also save the full results to a JSON file for more detailed analysis
    with open('test_results.json', 'w') as f:
        json.dump(all_results, f, indent=2)
    print("\nFull results have been saved to 'test_results.json'")

if __name__ == '__main__':
    main()