# 📖 Vector Profile Scanner: Plain English Glossary

> [!NOTE]
> This glossary translates complex Machine Learning and Software Engineering jargon into extremely simple, everyday analogies so anyone can understand exactly how our system works.

---

### 1. **Machine Learning (ML)** 🧠
* **The Definition:** Teaching a computer to spot patterns by showing it examples, rather than writing a strict list of rules.
* **The Example:** Instead of writing a million rules to describe a dog (has fur, has four legs, barks), you just show a toddler 100 pictures of dogs until they figure out the pattern themselves.

### 2. **Dataset (CSV File)** 📊
* **The Definition:** The textbook that the model studies to learn.
* **The Example:** A giant spreadsheet containing two columns. Column A has the "Skill Name" (e.g., Python), and Column B has the "Answer" (e.g., 1 for Yes, 0 for No). This is the exact textbook our robot reads to prepare for its exam.

### 3. **Binary Classification** ⚖️
* **The Definition:** A specific type of problem where there are exactly *two* possible answers.
* **The Example:** Sorting your dirty laundry into two exact baskets: "Whites" and "Colors". Our project plays this exact game, sorting skills into "AI Engineer" or "Not Relevant".

### 4. **TensorFlow** 🏭
* **The Definition:** The massive toolkit created by Google used to build and train artificial brains (neural networks).
* **The Example:** If you wanted to build a car from scratch, you wouldn't mine the metal yourself; you'd go to a Toyota factory and use their machines. TensorFlow is the factory we use to quickly build our robot's brain.

### 5. **Token / TextVectorization** 🧩
* **The Definition:** Breaking down long, complicated human sentences into tiny, countable mathematical pieces.
* **The Example:** It’s like taking a fully built LEGO castle (a long sentence) and snapping it apart into individual red, blue, and yellow bricks (tokens). The robot can't understand the "castle", but it *can* easily count 50 red bricks.

### 6. **Epoch** ⏳
* **The Definition:** Reading the entire dataset textbook from cover to cover exactly one time.
* **The Example:** If a student reads a math textbook from start to finish once, that is 1 Epoch. If our system is set to `epochs=100`, the robot is forced to read the CSV file 100 times in a row until it practically memorizes the patterns.

### 7. **Overfitting** ❌
* **The Definition:** When the model memorizes the exact training data but fails to understand the actual broad concept.
* **The Example:** A student who perfectly memorizes the answer key to a practice exam (`1: A, 2: B, 3: C`), but gets a completely failing grade on the actual real-world test because the questions were slightly different.

### 8. **Inference (Prediction)** 🔮
* **The Definition:** Using the fully trained model to make a smart guess on data it has never seen before.
* **The Example:** After graduating school and studying the textbook, a doctor (the model) looks at a brand new patient they have never met before (the new data) and successfully diagnoses them. 

### 9. **Model Confidence Score** 💯
* **The Definition:** A percentage from 0 to 100 indicating how strongly the model believes its guess is correct.
* **The Example:** Outputting `0.95` means the robot is confidently placing a $95 bet that the skill belongs to a Google AI Engineer. Outputting `0.51` means it is sweating nervously and just barely flipping a coin. 

### 10. **FastAPI** ⚡
* **The Definition:** A lightweight web server that allows external users to finally interact with our Python code over the internet.
* **The Example:** A chef (our model) can cook amazing food in the kitchen, but they need a drive-thru window (FastAPI) so customers can actually drive up, hand over their resume, and get their food (the prediction score) handed back to them.

### 11. **Docker** 🐳
* **The Definition:** A technology that completely seals our application into an identical, shippable container that works flawlessly anywhere.
* **The Example:** If you move to a new country, you can't guarantee their electrical outlets will fit your TV. Docker puts your TV, a perfect generator, and your entire living room into a master shipping box so it turns on instantly and identically on *any* computer in the world.

### 12. **CI/CD (GitHub Actions)** 🤖
* **The Definition:** The automated pipeline that strictly tests our code in the cloud before anyone is legally allowed to use it.
* **The Example:** Like health inspectors standing on a factory assembly line. Before a car is allowed to be driven out to the customer, the inspectors automatically crash-test it (`pytest`). If it fails, the assembly line halts immediately.
