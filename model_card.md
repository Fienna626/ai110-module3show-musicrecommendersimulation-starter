# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

The current system gives a strong advantage to genre because genre matches are worth twice as much as mood. That means the same genre can dominate recommendations even when the mood or energy is not a great fit. The dataset is small and skewed toward pop, lofi, and chill songs, so underrepresented genres like metal or classical are less likely to be recommended. The energy gap is calculated as a simple direct difference, so users with conflicting preferences such as high energy but a moody mood can get recommendations that feel inconsistent. The acoustic bonus also biases the system toward acoustic songs for users who set that flag, which may reduce diversity.

---

## 7. Evaluation 

How you checked whether the recommender behaved as expected. 

I tested several user profiles, including High-Energy Pop, Chill Lofi, and Deep Intense Rock. I also added a conflicting profile with high energy and a moody jazz preference to see if the system could handle edge cases. To evaluate the scoring, I looked for whether top recommendations matched the expected genre, mood, and energy. The main surprise was that the same strong genre match can make one song appear near the top across multiple profiles. I also ran an energy-weighted experiment and observed that increasing energy importance changed the top results more than changing the mood weight.

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
