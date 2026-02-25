# Vector Profile Scanner: Technical Architecture Q&A

This document serves as an internal reference for the technical decisions, architecture, and implementation details of the Vector Profile Scanner project.

## 1. Data Processing

**Q: Why was `TextVectorization` chosen instead of other word processors?**
**A:** Imagine teaching someone to read by giving them a dictionary where every word has a secret number code. `TextVectorization` is like building that exact dictionary right into the robot's brain (the model). When the model is active, we don't need a separate translator standing next to it to convert words to numbers; it does it entirely by itself instantly.

**Q: How does getting the data from the CSV file handle growing bigger?**
**A:** Right now, reading our CSV file is like reading a short recipe card from start to finish. If our recipe book grew to millions of pages, Python natively lets us read it "page by page" (chunking) instead of trying to carry the whole heavy book at once. The code is structured so we can swap out smaller recipe cards for bigger storage smoothly.

## 2. Model Architecture

**Q: Why use a simple Neural Network with just one Dense layer instead of a massive AI structure?**
**A:** Deciding if a skill is an "AI Skill" or "Cooking" only requires checking if specific keywords exist in a phrase. A massive AI (like a Transformer) is built for understanding complex storylines, long paragraphs, and deep context. Using a massive AI for our task would be like using a heavy crane just to pick up a single apple—our simple one-layer network is much faster, uses less energy, and perfectly gets the job done. 

**Q: Why use `binary_crossentropy` to measure errors?**
**A:** Our project is essentially a game of sorting things into exactly two buckets: Bucket 1 (Google Skill) or Bucket 0 (Not Relevant). `binary_crossentropy` is the special math formula perfectly designed for two-bucket sorting games. It calculates exactly how far off a guess was from landing safely in the correct bucket.

## 3. Project Structure & Organization

**Q: Why is the project split into different folders like `src/`, `tests/`, and `data/` instead of one big file?**
**A:** Think of a professional kitchen. You don't chop raw chicken, bake the cake, and wash the dishes all on the exact same table. 
*   **`src/`:** The cooking station where the actual meals (code) are made.
*   **`data/`:** The pantry where ingredients (CSV files) are stored untouched.
*   **`tests/`:** The health inspector's checklist making sure the kitchen is safe.
Keeping things separated stops a messy disaster and keeps the workspace clean for other developers.

**Q: What is the `notebooks/` folder for?**
**A:** Notebooks are like sketchpads. Developers use them to draw graphs, test ideas out, and visualize the data playfully before committing to building the final, sturdy product in the main `src/` folder.

## 4. Environment Safety

**Q: How do you make sure this runs exactly the same way on another computer?**
**A:** We use a `requirements.txt` file, which is like a strict packing list. By telling the other computer exactly which versions of tools it *must* download (e.g., `tensorflow==2.20.0`), we ensure the other machine is an exact clone of ours, stopping any unexpected surprises or crashes.

---

## 5. System Design

**Q: How would we scale this Vector Profile Scanner if millions of users wanted to scan profiles at the exact same moment?**
**A:** Right now, the scanner runs on a single computer. To handle millions of users, we would package the `src/predict.py` file into a web server (like a massive drive-thru window) using a tool like FastAPI or Flask. We would then place multiple copies of this web server onto a cloud network (like AWS or Google Cloud). A "Load Balancer" (a traffic cop) would sit at the front, directing incoming scans to whichever server is currently least busy!

**Q: If the list of "Must-Have Skills" changes daily, how do we update the model without shutting the system down?**
**A:** We would connect our system to a live Database (like PostgreSQL) instead of a static CSV file. Every night, an automated "cron job" (an invisible worker) would fetch the new skills, retrain a brand new model entirely in the background, and then instantly copy the new model into the live folder. The users would never experience a pause in the service.
