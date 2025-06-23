# README: LLM Testing and Evaluation

## Overview

This project evaluates the performance of four different Large Language Models (LLMs) using a dataset of test cases. The goal is to compare their capabilities, processing times, and suitability for lightweight applications. The models tested are:

- **phi:latest**  
- **qwen:1.8b**  
- **tinyllama:latest**  
- **gemma:2b**

---

## Models Overview

The following table provides a comparison of the models based on their parameters:

| **Model**         | **Image ID**      | **Size** | **Last Updated** | **Notes**                  |
|--------------------|-------------------|----------|------------------|----------------------------|
| **phi:latest**     | e2fd6321a5fe     | 1.6 GB   | 8 minutes ago    | Balanced performance       |
| **qwen:1.8b**      | b6e8ec2e7126     | 1.1 GB   | 8 minutes ago    | Lightweight, fast response |
| **tinyllama:latest** | 2644915ede35   | 637 MB   | 9 minutes ago    | Smallest, fastest          |
| **gemma:2b**       | b50d6c999e59     | 1.7 GB   | 20 minutes ago   | Largest, detailed output   |

---

## Dataset Used for Testing

The dataset consists of six test cases, each containing a user query, location, time, mood, and ideal recommendations. Below is an example of one test case:

```json
{
  "test_case_id": "cairo_chill_evening",
  "inputs": {
    "user_prompt": "Looking for something chill after work.",
    "location": "Cairo",
    "time": "Weekday Evening",
    "mood": "chill"
  },
  "ideal_recommendations": [
    "Art cafés",
    "Meditation events",
    "Movie nights nearby"
  ]
}
```

---

## Model Responses for Selected Test Cases

Here are the responses from the models for three randomly selected test cases:

### Test Case 1: `dubai_happy_friday`

**Prompt:**  
"User opens app on a Friday at 8 PM. Location: Dubai, Time: Friday 8 PM, Mood: happy."

| **Model**         | **Generated Response**                                                                                     | **Match Score** |
|--------------------|-----------------------------------------------------------------------------------------------------------|-----------------|
| **phi:latest**     | "1. A rooftop party with live music, cocktails and a stunning view of the city skyline. 2. A laser tag..." | 2               |
| **qwen:1.8b**      | "1. Declic Night Club Experience: Friday 8 PM, Declic App. 2. Declic Restaurant Challenge: Friday 8 PM..." | 0               |
| **tinyllama:latest** | "1. Virtual Trivia Night. 2. Virtual Happy Hour. 3. Virtual Movie Night."                                | 2               |
| **gemma:2b**       | "1. Attend a rooftop party in Dubai with stunning city views. 2. Explore the vibrant nightlife scene..."   | 2               |

---

### Test Case 2: `riyadh_lonely_outdoors`

**Prompt:**  
"I'm on my own this weekend and want to be outdoors. Location: Riyadh, Time: Solo Weekend, Mood: lonely + outdoors."

| **Model**         | **Generated Response**                                                                                     | **Match Score** |
|--------------------|-----------------------------------------------------------------------------------------------------------|-----------------|
| **phi:latest**     | "1. Explore a hiking trail in the mountains surrounding Riyadh. 2. Rent a bike or go for a long walk..."   | 2               |
| **qwen:1.8b**      | "1. Outdoor Adventure: The user wants to be outdoors, so an outdoor adventure could be organized..."       | 3               |
| **tinyllama:latest** | "1. Outdoor concert or festival. 2. Hiking trail. 3. Outdoor movie night."                               | 1               |
| **gemma:2b**       | "1. Riyadh Park Adventure. 2. Al Bujairi Park Hike. 3. Al Ustad Park Kayaking Tour."                       | 1               |

---

### Test Case 3: `cairo_curious_saturday`

**Prompt:**  
"What is there to discover in the city this morning? Location: Cairo, Time: Saturday Morning, Mood: curious."

| **Model**         | **Generated Response**                                                                                     | **Match Score** |
|--------------------|-----------------------------------------------------------------------------------------------------------|-----------------|
| **phi:latest**     | "1. Explore the historic Old City of Cairo, which includes iconic landmarks like the Great Pyramid..."     | 4               |
| **qwen:1.8b**      | "1. Historical Tour: The Declic app can provide a historical tour of Cairo, highlighting significant..."   | 4               |
| **tinyllama:latest** | "1. Art Walk. 2. Food Tour. 3. Culture Trip."                                                            | 6               |
| **gemma:2b**       | "1. Explore the bustling streets of Khan el-Khalili and discover hidden gems like the Khan el-Khalili..." | 4               |

---

## Processing Time Comparison

The table below compares the average processing time (in seconds) for each model across all test cases:

| **Model**         | **Average Processing Time (s)** |
|--------------------|---------------------------------|
| **phi:latest**     | 21.67                          |
| **qwen:1.8b**      | 13.23                          |
| **tinyllama:latest** | 2.88                          |
| **gemma:2b**       | 7.25                           |

---

## Conclusion

Based on the results:

1. **Best Lightweight Model:**  
   - **tinyllama:latest** is the fastest model with an average processing time of 2.88 seconds. It is ideal for lightweight applications where speed is critical.

2. **Best Match Score:**  
   - **phi:latest** and **gemma:2b** consistently achieve higher match scores, making them suitable for applications requiring detailed and accurate responses.

3. **Balanced Choice:**  
   - **qwen:1.8b** offers a good balance between speed and response quality, making it a versatile option.

For this project, **tinyllama:latest** is recommended if speed is the primary concern, while **phi:latest** is better for accuracy. Further testing with a larger dataset is advised to confirm these findings.