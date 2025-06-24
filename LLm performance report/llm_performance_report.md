# LLM Performance Comparison Report

This report details the performance of several lightweight LLMs for the Declic app's recommendation engine.

## 1. Overall Performance Summary

| model               |   avg_match_score |   avg_processing_time |   avg_response_length |   avg_performance_score |   avg_relevance_density |
|:--------------------|------------------:|----------------------:|----------------------:|------------------------:|------------------------:|
| deepseek-coder:1.3b |              0.67 |                  5.74 |                909.17 |                    0.22 |                    0.08 |
| gemma:2b            |              1.33 |                  8.74 |                249.17 |                    0.46 |                    0.69 |
| phi                 |              2    |                 25.18 |                829.67 |                    0.18 |                    0.42 |
| qwen:1.8b           |              1    |                 28.55 |               1479.17 |                    0.12 |                    0.15 |
| stablelm2:1.6b      |              2.33 |                  7.78 |               1218.33 |                    0.42 |                    0.2  |
| tinydolphin         |              1.17 |                  3.78 |                522.83 |                    0.94 |                    0.36 |
| tinyllama           |              1.67 |                  3.91 |                624    |                    1.08 |                    0.42 |

## 2. Best in Class

**Fastest Model (Lowest Avg. Time):** `tinydolphin`
**Most Relevant (Highest Avg. Match Score):** `stablelm2:1.6b`
**Most Efficient (Highest Avg. Performance Score):** `tinyllama`
**Most Concise & Relevant (Highest Avg. Relevance Density):** `gemma:2b`

## 3. Detailed Results per Test Case

### Test Case: `cairo_chill_evening`

**Ideal Recommendations:** Art cafÃ©s, Meditation events, Movie nights nearby

| model               |   match_score |   processing_time_seconds |   performance_score | generated_text                                                                                          |
|:--------------------|--------------:|--------------------------:|--------------------:|:--------------------------------------------------------------------------------------------------------|
| gemma:2b            |             0 |                     34.52 |                0    | Sure, here are three event ideas for the user:                                                          |
|                     |               |                           |                     |                                                                                                         |
|                     |               |                           |                     | 1. Live music event at a rooftop bar.                                                                   |
|                     |               |                           |                     | 2. Chill jazz ...                                                                                       |
| phi                 |             1 |                     48.92 |                0.02 | Sure! Based on your query, here are three event ideas that you can check out in Cairo this evening:     |
|                     |               |                           |                     | ...                                                                                                     |
| qwen:1.8b           |             1 |                     34.88 |                0.03 | 1. "Gone chilling after work with friends or colleagues at a cozy café or bar in the city center."      |
|                     |               |                           |                     | 2...                                                                                                    |
| tinyllama           |             1 |                     12.91 |                0.08 | 1. HIATUS Cafe & Bar - Join us for a night out with friends or colleagues to enjoy some delicious fo... |
| deepseek-coder:1.3b |             0 |                     17.12 |                0    | I'm sorry, but as an AI model developed by Deepseek specifically designed to assist with programming... |
| stablelm2:1.6b      |             1 |                     18.6  |                0.05 | 1. Rooftop Terrace: Head to one of Cairo's trendy rooftop terraces for a sunset chat with friends ov... |
| tinydolphin         |             0 |                     12.6  |                0    | Sure, here are three event ideas based on the context you provided:                                     |
|                     |               |                           |                     | 1. Visit a relaxing spa near Cai...                                                                     |

### Test Case: `cairo_curious_saturday`

**Ideal Recommendations:** Visit a museum, Historical walking tour, Explore a local market (souq)

| model               |   match_score |   processing_time_seconds |   performance_score | generated_text                                                                                          |
|:--------------------|--------------:|--------------------------:|--------------------:|:--------------------------------------------------------------------------------------------------------|
| gemma:2b            |             4 |                      2.91 |                1.37 | 1. Explore the bustling Khan el-Khalili market.                                                         |
|                     |               |                           |                     | 2. Visit the Hanging Church, a unique and mysterious...                                                 |
| phi                 |             4 |                      7.31 |                0.55 | 1. Explore the ancient Egyptian Museum and learn about the country's rich history.                      |
|                     |               |                           |                     | 2. Visit the famo...                                                                                    |
| qwen:1.8b           |             4 |                      7.04 |                0.57 | 1. Historical Walks: The Declic app can suggest a series of historical walks in the city, exploring ... |
| tinyllama           |             3 |                      2.1  |                1.43 | 1. Start the day with a guided meditation session led by a local practitioner. This could be a peace... |
| deepseek-coder:1.3b |             0 |                      2.83 |                0    | I'm sorry, but as an AI model developed by Deepseek for programming assistance and answering compute... |
| stablelm2:1.6b      |             7 |                     11.54 |                0.61 | 1. Explore Khan el-Kalbouty Market: Stroll around Khan el-Kalbouty Market, one of Cairo's oldest and... |
| tinydolphin         |             4 |                      0.96 |                4.17 | Sure, here are three event ideas for a user of the Declic app:                                          |
|                     |               |                           |                     | 1. Attend a public lecture by a famou...                                                                |

### Test Case: `dubai_energetic_tuesday`

**Ideal Recommendations:** Late-night gym session, Kickboxing class, Indoor rock climbing

| model               |   match_score |   processing_time_seconds |   performance_score | generated_text                                                                                          |
|:--------------------|--------------:|--------------------------:|--------------------:|:--------------------------------------------------------------------------------------------------------|
| gemma:2b            |             0 |                      2.94 |                0    | 1. Dance the night away at a vibrant nightclub in Dubai.                                                |
|                     |               |                           |                     | 2. Hit the dance floor at a lively beach pa...                                                          |
| phi                 |             2 |                     11.2  |                0.18 | 1. Join a local dance class or participate in a group exercise session at a fitness center, such as ... |
| qwen:1.8b           |             0 |                      4.58 |                0    | 1. "Dubai Escape Party: Let loose and burn off all your stress tonight!"                                |
|                     |               |                           |                     |                                                                                                         |
|                     |               |                           |                     | 2. "Energetic Dubai Nigh...                                                                             |
| tinyllama           |             1 |                      3.3  |                0.3  | Event Ideas for a User of Declic App:                                                                   |
|                     |               |                           |                     | 1. Declic Fitness Challenge: Join a 30-minute fitness challeng...                                       |
| deepseek-coder:1.3b |             0 |                      3.19 |                0    | As an AI developed by Deepseek, I'm designed with a focus on computer science and programming topics... |
| stablelm2:1.6b      |             1 |                      3.72 |                0.27 | 1. Yoga Night - Join an evening yoga session at a local studio in Dubai, where you can unwind after ... |
| tinydolphin         |             1 |                      1.1  |                0.91 | Three event ideas for a user in Dubai, tuesday evening, and feeling energized could be as follows:      |
|                     |               |                           |                     | 1...                                                                                                    |

### Test Case: `dubai_happy_friday`

**Ideal Recommendations:** Live music venues, Dance parties, Comedy shows

| model               |   match_score |   processing_time_seconds |   performance_score | generated_text                                                                                          |
|:--------------------|--------------:|--------------------------:|--------------------:|:--------------------------------------------------------------------------------------------------------|
| gemma:2b            |             2 |                      2.9  |                0.69 | 1. Attend a live music performance at the Dubai Miracle Garden.                                         |
|                     |               |                           |                     | 2. Enjoy a sunset cruise along the D...                                                                 |
| phi                 |             2 |                      9.76 |                0.2  | 1. A rooftop lounge party with live music and cocktails to enjoy the vibrant nightlife in Dubai.        |
|                     |               |                           |                     | 2. ...                                                                                                  |
| qwen:1.8b           |             0 |                    104.76 |                0    | 1. "Declic Event Night 8 PM UAE @ Dubai,"                                                               |
|                     |               |                           |                     | 2. "Declic Fest 8 PM UAE, #DubaiEvent,"                                                                 |
|                     |               |                           |                     | 3. "Declic Dubai 8...                                                                                   |
| tinyllama           |             2 |                      1.58 |                1.27 | 1. Declic Happy Hour - Hosted by one of the users in your community, this event will feature live mu... |
| deepseek-coder:1.3b |             2 |                      6.09 |                0.33 | 1) Feedback Event - Declic App Review Post (Friday, Auguest 20th): This event would provide an infor... |
| stablelm2:1.6b      |             2 |                      1.96 |                1.02 | 1. "Happy hour celebration at an upscale restaurant in Downtown Dubai, featuring live music and a sp... |
| tinydolphin         |             0 |                      1.01 |                0    | Sure, here are three event ideas for a user of Declic:                                                  |
|                     |               |                           |                     |                                                                                                         |
|                     |               |                           |                     | 1. Walk around the city and enjoy the atmosp...                                                         |

### Test Case: `riyadh_family_rainy_day`

**Ideal Recommendations:** Bowling alley, Indoor playground, Science center exhibit

| model               |   match_score |   processing_time_seconds |   performance_score | generated_text                                                                                          |
|:--------------------|--------------:|--------------------------:|--------------------:|:--------------------------------------------------------------------------------------------------------|
| gemma:2b            |             1 |                      7.47 |                0.13 | Sure, here are three event ideas for the user:                                                          |
|                     |               |                           |                     |                                                                                                         |
|                     |               |                           |                     | 1. **Riyadh Zoo Adventure:** Explore the wonders of ...                                                 |
| phi                 |             2 |                     59.63 |                0.03 | Sure, here are three event ideas that you may be interested in based on your query:                     |
|                     |               |                           |                     | 1. Outdoor Movie...                                                                                     |
| qwen:1.8b           |             0 |                      9.21 |                0    | 1. Organize a Family Game Night: Declic app can be used to schedule and organize games nights with f... |
| tinyllama           |             3 |                      0.88 |                3.41 | 1. Indoor bowling alley with lanes designed for families.                                               |
|                     |               |                           |                     | 2. Escape room themed for kids, where pare...                                                           |
| deepseek-coder:1.3b |             1 |                      1.35 |                0.74 | I'm sorry, but as an AI focused on computer science and programming related questions, I am not equi... |
| stablelm2:1.6b      |             2 |                      6.54 |                0.31 | 1. Visit an amusement park or theme park - The whole family can enjoy various rides, exhibitions, an... |
| tinydolphin         |             1 |                      3.25 |                0.31 | Sure, I can help! Here are three event ideas suitable for families in Riyadh this rainy Sunday after... |

### Test Case: `riyadh_lonely_outdoors`

**Ideal Recommendations:** Group hikes, Public park meetups, Community clean-up events

| model               |   match_score |   processing_time_seconds |   performance_score | generated_text                                                                                          |
|:--------------------|--------------:|--------------------------:|--------------------:|:--------------------------------------------------------------------------------------------------------|
| gemma:2b            |             1 |                      1.71 |                0.58 | 1. Explore the King Khalid Park                                                                         |
|                     |               |                           |                     | 2. Visit the Riyadh Adventure Park                                                                      |
|                     |               |                           |                     | 3. Enjoy a picnic in the Al Bujai...                                                                    |
| phi                 |             1 |                     14.27 |                0.07 | 1. Join a local outdoor event in Riyadh, such as a bike ride or hiking excursion, which is perfect f... |
| qwen:1.8b           |             1 |                     10.83 |                0.09 | 1. Outdoor Hiking: With a solo weekend, you can plan an outdoor hike in nearby mountains or reserves... |
| tinyllama           |             0 |                      2.69 |                0    | 1. Outdoor BBQ with friends: This event idea could take place in a scenic location with plenty of op... |
| deepseek-coder:1.3b |             1 |                      3.86 |                0.26 | 1. "Traveling for Fun in Riyadh": A user could suggest that they might enjoy a sightseeing trip thro... |
| stablelm2:1.6b      |             1 |                      4.34 |                0.23 | 1. Hiking in Burdah Al-Jalil Regional Park:                                                             |
|                     |               |                           |                     | Located in Riyadh, Burdah Al-Jalil Regional Park offers ...                                             |
| tinydolphin         |             1 |                      3.75 |                0.27 | Sure, here are three event ideas for your user:                                                         |
|                     |               |                           |                     |                                                                                                         |
|                     |               |                           |                     | 1) Explore a nearby forest or park with your friend...                                                  |

## 4. Conclusion

Based on the analysis, the choice of the best model depends on the primary business objective:

- **For Maximum Speed:** `tinydolphin` is the clear winner, offering the quickest responses.
- **For Maximum Relevance:** `stablelm2:1.6b` provides the most accurate suggestions according to the ideal keywords.
- **For a Balanced Approach:** `tinyllama` offers the best trade-off between relevance and speed.

Further analysis should consider the qualitative aspects of the generated text.
