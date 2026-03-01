# Vector Profile Scanner: Project Commands Reference

This document serves as a quick-reference guide for all terminal commands used throughout the development, deployment, and testing of the Vector Profile Scanner.

## 1. Environment & Setup

Create the local development environment and install required libraries:

```bash
# Install all required libraries exactly as specified
pip install -r requirements.txt

# Install the current directory as a local package (allows src/ to be imported anywhere)
pip install -e .
```

## 2. Model Execution

The core commands to train the model and make immediate predictions:

```bash
# Train the model from the CSV dataset and save the .keras artifacts
python3 src/train.py

# Make a live prediction against the saved model.
# Note: You can replace "Vertex AI" with any custom string like "Cooking" to test it
python3 src/predict.py "Vertex AI"
```

## 3. Automated Testing

Commands to verify the health and integrity of the project's logic:

```bash
# Run the entire automated test suite to verify code logic
pytest tests/

# If `pytest` is not globally installed on your system PATH, use the Python module runner
python3 -m pytest tests/
```

## 4. Exploration & Notebooks

Commands to load the interactive Jupyter environment for Data Analysis:

```bash
# Launch the Jupyter Notebook server in your browser to view EDA files
jupyter notebook notebooks/01_data_exploration.ipynb
```

## 5. Git & Version Control

The standard workflow used to save changes to the remote GitHub repository:

```bash
# Check the current status of files (modified, new, or deleted)
git status

# Stage a specific file for commit (e.g., the README)
git add README.md

# Stage an entire directory for commit (e.g., the source code or artifacts)
git add src/
git add artifacts/

# Commit the staged changes with a descriptive message
git commit -m "docs: add comprehensive docstrings and architecture qa"

# Push the local commits to the main branch on the remote GitHub repository
git push
```
