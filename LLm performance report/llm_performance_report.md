# LLM Performance Comparison Report 

This report details the performance of several lightweight LLMs for the Declic app's recommendation engine.

---

## 1. Overall Performance Summary

| **Model**         | **Avg. Match Score** | **Avg. Processing Time (s)** | **Avg. Response Length (chars)** | **Avg. Performance Score** | **Avg. Relevance Density** |
|--------------------|---------------------:|-----------------------------:|---------------------------------:|---------------------------:|---------------------------:|
| **phi:latest**     | 2.00                | 25.18                        | 829.67                          | 0.18                       | 0.42                       |
| **qwen:1.8b**      | 1.00                | 28.55                        | 1479.17                         | 0.12                       | 0.15                       |
| **tinyllama**      | 1.67                | 3.91                         | 624.00                          | 1.08                       | 0.42                       |
| **gemma:2b**       | 1.33                | 8.74                         | 249.17                          | 0.46                       | 0.69                       |
| **stablelm2:1.6b** | 2.33                | 7.78                         | 1218.33                         | 0.42                       | 0.20                       |
| **tinydolphin**    | 1.17                | 3.78                         | 522.83                          | 0.94                       | 0.36                       |
| **deepseek-coder** | 0.67                | 5.74                         | 909.17                          | 0.22                       | 0.08                       |

---

## 2. Best in Class

- **Fastest Model (Lowest Avg. Time):** `tinydolphin`
- **Most Relevant (Highest Avg. Match Score):** `stablelm2:1.6b`
- **Most Efficient (Highest Avg. Performance Score):** `tinyllama`
- **Most Concise & Relevant (Highest Avg. Relevance Density):** `gemma:2b`

---

## 3. Detailed Results per Test Case

### Test Case: `cairo_chill_evening`

| **Model**         | **Match Score** | **Processing Time (s)** | **Performance Score** | **Generated Text**                                                                                     |
|--------------------|----------------:|-------------------------:|-----------------------:|:-------------------------------------------------------------------------------------------------------|
| **gemma:2b**       | 0               | 34.52                   | 0.00                  | "Live music event at a rooftop bar..."                                                                 |
| **phi:latest**     | 1               | 48.92                   | 0.02                  | "A local food tour around Cairo's famous restaurants and markets..."                                   |
| **tinyllama**      | 1               | 12.91                   | 0.08                  | "HIATUS Cafe & Bar - Join us for a night out with friends or colleagues..."                            |
| **tinydolphin**    | 0               | 12.60                   | 0.00                  | "Visit a relaxing spa near Cairo's beautiful old city walls..."                                        |

---

### Test Case: `dubai_happy_friday`

| **Model**         | **Match Score** | **Processing Time (s)** | **Performance Score** | **Generated Text**                                                                                     |
|--------------------|----------------:|-------------------------:|-----------------------:|:-------------------------------------------------------------------------------------------------------|
| **gemma:2b**       | 2               | 2.90                    | 0.69                  | "Attend a live music performance at the Dubai Miracle Garden..."                                       |
| **phi:latest**     | 2               | 9.76                    | 0.20                  | "A rooftop lounge party with live music and cocktails..."                                              |
| **tinyllama**      | 2               | 1.58                    | 1.27                  | "Declic Happy Hour - Hosted by one of the users in your community..."                                  |
| **tinydolphin**    | 0               | 1.01                    | 0.00                  | "Walk around the city and enjoy the atmosphere during sunset..."                                       |

---

## 4. Conclusion

Based on the analysis, the choice of the best model depends on the primary business objective:

- **For Maximum Speed:** `tinydolphin` is the clear winner, offering the quickest responses.
- **For Maximum Relevance:** `stablelm2:1.6b` provides the most accurate suggestions according to the ideal keywords.
- **For a Balanced Approach:** `tinyllama` offers the best trade-off between relevance and speed.

Further analysis should consider the qualitative aspects of the generated text.
