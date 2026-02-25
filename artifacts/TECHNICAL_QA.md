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
