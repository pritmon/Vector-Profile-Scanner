# Vector Profile Scanner

This is a beginner-friendly project using TensorFlow to classify Google AI Engineer skills vs. non-relevant skills. It is built using the industry-standard structure for Machine Learning projects.

## Project Structure
- `src/`: Core Python modules (model, training, prediction)
- `data/`: Raw and processed datasets
- `notebooks/`: Exploratory Data Analysis (EDA) Jupyter notebooks
- `tests/`: Automated pytest verification suite
- `models/`: Generated artifacts and TensorFlow `.keras` weights

## Installation
Setup the project locally using Python's package manager:

```bash
pip install -r requirements.txt
pip install -e .
```

## How to Run

### 1. Train the Model
```bash
python3 src/train.py
```

### 2. Predict a Skill
```bash
python3 src/predict.py "Vertex AI"
```

### 3. Run Automated Tests
```bash
pytest tests/
```

### 4. Explore Data Insights
```bash
jupyter notebook notebooks/01_data_exploration.ipynb
```
