# Vector Profile Scanner: Technical Architecture Q&A

This document serves as an internal reference for the technical decisions, architecture, and implementation details of the Vector Profile Scanner project.

## 1. Data Preprocessing & Pipeline

**Q: Why was `TextVectorization` chosen instead of traditional TF-IDF or Word2Vec for this project?**
**A:** `TextVectorization` is a native TensorFlow Keras preprocessing layer. By using it, the preprocessing logic becomes intrinsically part of the TensorFlow pipeline. This means when the model is saved and deployed, it expects raw strings rather than requiring a separate preprocessing library (like `scikit-learn`) to transform the text in production. For this vocabulary-based skill classification, a `multi_hot` encoding was sufficient and highly performant.

**Q: How does the dataset loading mechanism handle scalability?**
**A:** Currently, `src/data_loader.py` reads a CSV using Python's native `csv` module, which is perfect for smaller datasets. If the data were to scale to millions of rows, the architecture allows us to easily swap the native Python reader with `tf.data.Dataset` or `Pandas` chunking without affecting the model definition.

## 2. Model Architecture

**Q: Why use a Sequential Neural Network with a single Dense layer instead of a more complex architecture like an LSTM or Transformer?**
**A:** This is a binary classification problem based on single keywords/phrases (e.g., "Vertex AI"), not complex sequential sentences where context and word order matter. Therefore, recurrent layers (LSTM) or attention mechanisms (Transformers) would be computationally excessive and prone to overfitting. A single Dense layer with a sigmoid activation acts similarly to Logistic Regression—it efficiently learns the independent weight of each vocabulary token.

**Q: Why was `binary_crossentropy` selected as the loss function?**
**A:** The goal of the model is to distinguish between two exclusive classes: Target Google Skill (1) and Non-Target Skill (0). `binary_crossentropy` is mathematically designed for binary classification tasks, calculating the error between a predicted probability (from the sigmoid activation) and the actual binary label.

## 3. Project Structure & Engineering Standards

**Q: Why is the repository structured with `src/`, `tests/`, and `data/` instead of a monolithic script?**
**A:** This structure adheres to professional MLOps and software engineering standards (often seen at enterprise companies like Google). 
*   **Separation of Concerns:** Model architecture (`model.py`), data ingestion (`data_loader.py`), and execution (`train.py`) are logically separated, making the code maintainable.
*   **Testing:** It allows for isolated unit testing (`tests/`) to be run via `pytest`, ensuring CI/CD pipelines can validate the code automatically.
*   **Packaging:** Using `setup.py` allows the project to be installed as a local package, preventing `sys.path` import issues across different directories and notebooks.

**Q: What is the purpose of the `notebooks/` directory if the training happens in `.py` scripts?**
**A:** Jupyter Notebooks (`.ipynb`) are excellent tools for Exploratory Data Analysis (EDA) and visualizing class distributions using libraries like Matplotlib. However, they are notoriously difficult to test, version control, and deploy. Therefore, experimentation is kept in `notebooks/`, while production-grade training and inference are formalized in standard Python modules (`src/`).

## 4. Environment & Reproducibility

**Q: How does the project guarantee environment reproducibility across different developer machines?**
**A:** The `requirements.txt` file uses exact version pinning (e.g., `tensorflow==2.20.0`). This ensures that anyone cloning the repository will download the exact same dependencies, preventing "it works on my machine" bugs caused by upstream library updates.
