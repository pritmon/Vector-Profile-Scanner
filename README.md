# Vector Profile Scanner

This is a beginner-friendly project using TensorFlow to classify Google AI Engineer skills vs. non-relevant skills. It is built using the industry-standard structure for Machine Learning projects.

## Tech Stack
- **Language**: Python 3.9+
- **Machine Learning Framework**: TensorFlow / Keras (Sequential Models, TextVectorization)
- **Data Modification**: Pandas & CSV Parsing
- **Data Exploration**: Jupyter Notebooks & Matplotlib
- **Testing**: Pytest (Unit Testing)
- **Environment**: Virtual Env / `pip`

## Project Structure

*   [**`src/`**](./src) - Core Python modules (model, training, prediction)
    *   [**`data_loader.py`**](./src/data_loader.py) - Script to load and preprocess data
    *   [**`model.py`**](./src/model.py) - Neural network architecture definition
    *   [**`train.py`**](./src/train.py) - Script for training the model
    *   [**`predict.py`**](./src/predict.py) - Script to run predictions on new data
*   [**`data/`**](./data) - Raw and processed datasets needed for training
*   [**`notebooks/`**](./notebooks) - Exploratory Data Analysis (EDA) Jupyter notebooks
*   [**`tests/`**](./tests) - Automated pytest verification suite
*   [**`models/`**](./models) - Generated artifacts and TensorFlow `.keras` weights
*   [**`requirements.txt`**](./requirements.txt) - Python dependencies
*   [**`setup.py`**](./setup.py) - Package installation configuration
*   [**`README.md`**](./README.md) - Project documentation

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
