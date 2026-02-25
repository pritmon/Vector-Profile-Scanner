# Vector Profile Scanner: Technical Architecture Q&A

This document serves as an internal reference for the technical decisions, architecture, and implementation details of the Vector Profile Scanner project.

## 1. Data Processing

**Q: Why was `TextVectorization` chosen instead of other word processors?**
**A:** 
*   **The Problem:** Normally, models need a separate translator standing by to convert words into number codes.
*   **The Solution:** `TextVectorization` acts like a dictionary built perfectly into the robot's brain.
*   **The Benefit:** When the model is active, it doesn't need external help; it translates words to numbers instantly and entirely on its own.

**Q: How does getting the data from the CSV file handle growing bigger?**
**A:** 
*   **Current State:** Reading our CSV file is like reading a short recipe card from start to finish.
*   **Scaling Up:** If our recipe book grew to millions of pages, Python natively blocks crashes by letting us read it "page by page" (chunking).
*   **The Architecture:** The code is structured powerfully so we can swap out small recipe cards for bigger storage smoothly without carrying a heavy book all at once.

## 2. Model Architecture

**Q: Why use a simple Neural Network with just one Dense layer instead of a massive AI structure?**
**A:** 
*   **The Task:** Deciding if a skill is an "AI Skill" or "Cooking" only requires checking if specific keywords exist.
*   **The Example:** A massive AI (like a Transformer) is built for understanding complex storylines, which is like using a heavy construction crane just to pick up a single apple.
*   **The Result:** Our simple one-layer network is much faster, uses less energy, and gets the job done perfectly.

**Q: Why use `binary_crossentropy` to measure errors?**
**A:** 
*   **The Game:** Our project is essentially a game of sorting things into exactly two buckets: Bucket 1 (Google Skill) or Bucket 0 (Not Relevant).
*   **The Math:** `binary_crossentropy` is the special math formula perfectly designed for two-bucket sorting games.
*   **The Score:** It calculates exactly how far off a guess was from landing safely in the correct bucket.

## 3. Project Structure & Organization

**Q: Why is the project split into different folders like `src/`, `tests/`, and `data/` instead of one big file?**
**A:** 
*   **The Analogy:** Think of a professional kitchen. You don't chop raw chicken, bake the cake, and wash the dishes all on the exact same table.
*   **`src/`:** The cooking station where the actual meals (code) are made.
*   **`data/`:** The pantry where ingredients (CSV files) are stored untouched.
*   **`tests/`:** The health inspector's checklist making sure the kitchen is safe.
*   **The Goal:** Keeping things separated stops a messy disaster and keeps the workspace clean for other developers.

**Q: What is the `notebooks/` folder for?**
**A:** 
*   **The Purpose:** Notebooks are like sketchpads for developers.
*   **The Usage:** They use them to playfully draw graphs, test ideas out, and visualize the data.
*   **The Flow:** It happens here before committing to building the final, sturdy product in the main `src/` folder.

## 4. Environment Safety

**Q: How do you make sure this runs exactly the same way on another computer?**
**A:** 
*   **The Tool:** We use a `requirements.txt` file, which acts like a strict packing list.
*   **The Action:** It tells the other computer exactly which versions of tools it *must* download (e.g., `tensorflow==2.20.0`).
*   **The Output:** This ensures the other machine is an exact clone of ours, stopping any unexpected surprises or crashes.

---

## 5. System Design

**Q: How would we scale this Vector Profile Scanner if millions of users wanted to scan profiles at the exact same moment?**
**A:** 
*   **The Server:** We would package the `src/predict.py` file into a web server (like a massive drive-thru window) using tools like FastAPI or Flask.
*   **The Cloud:** We would place multiple copies of this web server onto a cloud network like AWS or Google Cloud.
*   **The Traffic Cop:** A "Load Balancer" would sit at the front, directing incoming scans to whichever server is currently least busy!

**Q: If the list of "Must-Have Skills" changes daily, how do we update the model without shutting the system down?**
**A:** 
*   **The Connection:** We would connect our system to a live Database (like PostgreSQL) instead of a static CSV file.
*   **The Worker:** Every night, an automated "cron job" (an invisible worker) would fetch the new skills.
*   **The Update:** It retrains a brand new model entirely in the background, and then instantly copies the new model into the live folder with zero downtime for users.

## 6. Model Performance & Evaluation

**Q: In a binary classification project like this, what is the best way to evaluate if the model is actually "good"? Is Accuracy enough?**
**A:**
*   **The Problem with Accuracy:** Imagine a hospital testing for a very rare disease where 99 people are healthy and 1 is sick. A model could just blindly guess "healthy" every single time and score 99% accuracy, even though it failed its actual job of finding the sick person.
*   **The Solution (Precision & Recall):** We must look at two other numbers. 
    *   **Precision:** Out of all the people the model *claimed* were sick, how many actually were? (Are there too many false alarms?)
    *   **Recall:** Out of all the people who were *actually* sick, how many did the model successfully find? (Did it miss anyone in danger?)
*   **The Trade-off (F1-Score):** Usually, increasing one lowers the other. The F1-Score combines them into a single reliable grade.

**Q: What is "Overfitting", and how do you prevent it in neural networks?**
**A:**
*   **The Concept:** Overfitting is like a student who memorizes the exact answers to a practice test but fails the real exam because they never actually learned the *concepts*.
*   **The Symptoms:** The model gets a near-perfect score on the training data but performs terribly when shown new, unseen data.
*   **The Prevention:** We can use **Dropout** (randomly turning off a few brain cells during training so it doesn't rely too heavily on one specific path) or **Early Stopping** (stopping the training the moment it starts memorizing instead of learning).

## 7. Data Handling

**Q: How would you handle "Imbalanced Data" if your CSV file had 10,000 non-skills but only 50 Google skills?**
**A:**
*   **The Danger:** If one bucket is overflowing and the other is nearly empty, the model will just lazily guess the full bucket every time to get an easy high score.
*   **Fix 1 (Oversampling):** We can artificially copy the 50 Google skills over and over until there are 10,000 of them, balancing the scales.
*   **Fix 2 (Undersampling):** We can randomly throw away 9,950 non-skills to match the 50 Google skills, though we lose a lot of information this way.
*   **Fix 3 (Class Weights):** We can tell the model's grading system that guessing a Google skill correctly is worth 200 points, while guessing a non-skill is only worth 1 point.

**Q: How do you handle "Missing Data" (Null values) in your datasets?**
**A:**
*   **The Decision:** We have to decide whether to delete or guess.
*   **Dropping:** If only 1% of the rows are missing data, we can safely throw those rows into the trash entirely.
*   **Imputation (Guessing):** If 30% of the rows are missing the "salary" column, we can't throw away that much data. Instead, we fill in the blank spaces with the *average* salary of everyone else, or use a smaller ML model to predict what the missing value *should* be.

## 8. Advanced NLP Concepts (Tokens & LLMs)

**Q: What exactly is a "Token", and how does the model see it?**
**A:**
*   **The Concept:** A token is the smallest piece of a puzzle. Instead of a model reading the entire sentence "Artificial Intelligence Engineer" as one giant continuous block, it chops it up into three smaller pieces (tokens): "Artificial", "Intelligence", and "Engineer".
*   **The Process:** `TextVectorization` splits a phrase into these tokens, counts them up, and assigns a specific number to each unique piece.
*   **The Analogy:** It’s exactly like taking a fully built LEGO spaceship (the phrase) and snapping it back down into individual blue, red, and yellow bricks (tokens) so the robot can count exactly how many of each color there are.

**Q: When processing text or documents, why do we use "Chunks"?**
**A:**
*   **The Problem:** The robot brain only has a small amount of short-term memory (RAM). If we give it a 10,000-word resume all at once, it will choke and crash.
*   **The Solution:** "Chunking" means slicing the massive document into smaller, bite-sized paragraphs of 100 or 200 words.
*   **The Analogy:** You can't swallow a whole pizza in one single bite without choking. You must slice the pizza into 8 chunks, eat one piece at a time, process it, and move on to the next.

**Q: Does our Vector Profile Scanner suffer from "AI Hallucination" like ChatGPT?**
**A:**
*   **Different Brain Types:** ChatGPT is a *Generative* model (a storyteller)—it generates totally new sentences, and sometimes it gets confused and just confidently makes up a lie (a hallucination) because it wants to finish the story.
*   **Our Model:** Our `Sequential` model is an *Analytical/Discriminative* model (a security guard). It doesn't create sentences; it simply looks at an ID (the tokens) and outputs a percentage (e.g., "I am 90% sure this is a Google Skill").
*   **The False Positive:** Because it only outputs a math percentage from 0% to 100%, it cannot "hallucinate" a fake skill. The worst mistake it can make is a "False Positive"—acting like an overly eager security guard who mistakenly lets a regular employee into a VIP room.

## 9. TensorFlow & Market Demands

**Q: Why choose TensorFlow/Keras over PyTorch for this specific project?**
**A:**
*   **The Market Reality:** While PyTorch is extremely popular for *academic research* and building brand new experimental architectures, TensorFlow (paired with Keras) absolutely dominates *Enterprise Production*.
*   **The Project Need:** For a production-ready application like our Vector Profile Scanner, we don't need to invent new math; we need rapid deployment, stable APIs, and easy serving (like TF Serving or TFLite for mobile).
*   **The Analogy:** PyTorch is a highly customizable laboratory for a mad scientist to build new engines from scratch. TensorFlow is the massive Toyota factory that quickly and reliably builds 1,000 standard cars every day for the real world.

**Q: Why is saving the model as `.keras` important compared to older `.h5` formats?**
**A:**
*   **The Evolution:** In modern TensorFlow (version 2.13+), the official and safest way to save a model is utilizing the new, native `.keras` format (which we use in our project!).
*   **The Benefit:** The older `.h5` format sometimes struggled to accurately save custom layers (like our `TextVectorization` layer).
*   **The Modern Standard:** Using `.keras` proves to an employer that you are up-to-date with modern 2024+ ML engineering standards rather than relying on outdated 2019 tutorials.

**Q: What is a "Tensor" and why is the framework named after it?**
**A:**
*   **The Concept:** A "Tensor" is just a fancy mathematical word for a multi-dimensional array or a grid of numbers. 
    *   A single number (Speed: 50) is a *Scalar*.
    *   A list of numbers (Coordinates: [10, 20]) is a *Vector*.
    *   A grid of numbers (An image with pixels) is a *Matrix*.
    *   Once you stack grids on top of grids (like video frames), we just simplify and call everything a *Tensor*.
*   **The Flow:** The framework is named "TensorFlow" because data (represented as these number grids) literally "flows" continuously through the layers of the neural network during training.
