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

---

## Key Findings

### 1. **Best Models by Category**
- **Fastest Model:** `tinydolphin` (Average Processing Time: 3.78 seconds)
- **Most Accurate Model:** `stablelm2:1.6b` (Highest Match Score: 2.33)
- **Best Balanced Model:** `tinyllama` (Best Trade-off Between Speed and Accuracy)

### 2. **Performance Summary**
| **Model**         | **Avg. Match Score** | **Avg. Processing Time (s)** | **Avg. Performance Score** |
|--------------------|---------------------:|-----------------------------:|---------------------------:|
| **phi:latest**     | 2.00                | 25.18                        | 0.18                       |
| **qwen:1.8b**      | 1.00                | 28.55                        | 0.12                       |
| **tinyllama**      | 1.67                | 3.91                         | 1.08                       |
| **gemma:2b**       | 1.33                | 8.74                         | 0.46                       |
| **stablelm2:1.6b** | 2.33                | 7.78                         | 0.42                       |
| **tinydolphin**    | 1.17                | 3.78                         | 0.94                       |
| **deepseek-coder** | 0.67                | 5.74                         | 0.22                       |

---

## Detailed Report

For a full breakdown of the results, including test case-specific performance and generated responses, see the [LLM Performance Report](LLm%20performance%20report/llm_performance_report.md).

---

## Conclusion

- **For Speed:** Use `tinydolphin` or `tinyllama` for lightweight applications requiring fast responses.
- **For Accuracy:** Use `stablelm2:1.6b` for applications requiring high relevance and match scores.
- **For Balance:** Use `tinyllama` for a good trade-off between speed and accuracy.

Further testing with a larger dataset is recommended to validate these findings.
