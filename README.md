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

📂 [**`Vector-Profile-Scanner/`**](./)<br>
├── 📂 [**`src/`**](./src) — Core Python modules (model, training, prediction)<br>
│&nbsp;&nbsp;&nbsp;├── 📄 [**`data_loader.py`**](./src/data_loader.py) — Script to load and preprocess data<br>
│&nbsp;&nbsp;&nbsp;├── 📄 [**`model.py`**](./src/model.py) — Neural network architecture definition<br>
│&nbsp;&nbsp;&nbsp;├── 📄 [**`train.py`**](./src/train.py) — Script for training the model<br>
│&nbsp;&nbsp;&nbsp;└── 📄 [**`predict.py`**](./src/predict.py) — Script to run predictions on new data<br>
├── 📂 [**`data/`**](./data) — Raw and processed datasets needed for training<br>
├── 📂 [**`notebooks/`**](./notebooks) — Exploratory Data Analysis (EDA) Jupyter notebooks<br>
├── 📂 [**`tests/`**](./tests) — Automated pytest verification suite<br>
├── 📂 [**`models/`**](./models) — Generated artifacts and TensorFlow `.keras` weights<br>
├── 📄 [**`requirements.txt`**](./requirements.txt) — Python dependencies<br>
├── 📄 [**`setup.py`**](./setup.py) — Package installation configuration<br>
└── 📄 [**`README.md`**](./README.md) — Project documentation<br>

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
