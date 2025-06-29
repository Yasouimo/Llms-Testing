# README: LLM Testing and Evaluation

## Overview

This project evaluates the performance of several lightweight Large Language Models (LLMs) using a dataset of test cases. The goal is to compare their capabilities, processing times, and suitability for lightweight applications. The models tested are: 

- **phi:latest**   
- **qwen:1.8b**  
- **tinyllama:latest**  
- **gemma:2b**  
- **stablelm2:1.6b**  
- **tinydolphin**  
- **deepseek-coder:1.3b**
- **t5-large**

---

## Models Overview

The following table provides a brief comparison of the models based on their parameters:

| **Model**         | **Size**  | **Notes**                  |
|--------------------|-----------|----------------------------|
| **phi:latest**     | 1.6 GB    | Balanced performance       |
| **qwen:1.8b**      | 1.1 GB    | Lightweight, fast response |
| **tinyllama:latest** | 637 MB  | Smallest, fastest          |
| **gemma:2b**       | 1.7 GB    | Largest, detailed output   |
| **stablelm2:1.6b** | 1.6 GB    | High relevance             |
| **tinydolphin**    | 522 MB    | Extremely fast             |
| **deepseek-coder:1.3b** | 909 MB | Programming-focused        |
| **t5-large**       | ~1.2 GB   | Text-to-text transfer transformer |

---

## Key Metrics

### 1. **Metrics Introduced**
The following metrics were used to evaluate the models:

- **`avg_time_sec`**: The average time (in seconds) taken by the model to process a single test case.
- **`avg_match_score`**: The average relevance score of the model's responses compared to the ideal recommendations.
- **`params_billions`**: The number of parameters (in billions) in the model, which impacts its size and computational requirements.
- **`efficiency_score`**: A composite metric calculated as

```
efficiency_score = (avg_match_score / avg_time_sec) * params_billions
```

This score balances relevance, speed, and model size. Higher scores indicate better overall efficiency.

---

### 2. **Performance Summary**
| **Model**         | **Params (B)** | **Avg. Time (s)** | **Avg. Match Score** | **Efficiency Score** |
|--------------------|---------------:|------------------:|---------------------:|---------------------:|
| **tinyllama**      | 1.1            | 4.17              | 2.00                | 0.44                |
| **stablelm2:1.6b** | 1.6            | 12.63             | 2.33                | 0.12                |
| **deepseek-coder** | 1.3            | 6.52              | 0.83                | 0.10                |
| **qwen:1.8b**      | 1.8            | 11.36             | 1.67                | 0.08                |
| **tinydolphin**    | 2.8            | 5.16              | 1.17                | 0.08                |
| **phi:latest**     | 2.7            | 12.10             | 2.00                | 0.06                |
| **gemma:2b**       | 2.0            | 10.77             | 1.00                | 0.05                |
| **t5-large**       | 1.7            | 5.44              | 0.00                | 0.00                |

---

## Key Findings

### 1. **Best Models by Category**
- **Fastest Models:** `tinydolphin` and `tinyllama` (Average Processing Time: 5.16 seconds)
- **Most Accurate Model:** `stablelm2:1.6b` (Highest Match Score: 2.33)
- **Most Efficient Model:** `tinyllama` (Highest Efficiency Score: 0.44)

### 2. **Insights from Metrics**
- **Efficiency Trade-offs:**  
Models like `tinyllama` and `tinydolphin` excel in speed and efficiency, making them ideal for lightweight applications. However, `stablelm2:1.6b` offers the highest accuracy, which is better suited for applications requiring detailed and relevant responses.
- **Parameter Impact:**  
Larger models like `phi` and `gemma:2b` have higher parameter counts, which can lead to slower processing times and lower efficiency scores despite decent match scores.


## Conclusion

- **For Speed:** Use `tinydolphin` or `tinyllama` for lightweight applications requiring fast responses.
- **For Accuracy:** Use `stablelm2:1.6b` for applications requiring high relevance and match scores.
- **For Efficiency:** Use `tinyllama` for a good trade-off between speed, accuracy, and model size.

Further testing with a larger dataset is recommended to validate these findings.
