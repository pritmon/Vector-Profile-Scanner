# Vector Profile Scanner

A TensorFlow-powered skill classification system that identifies Google AI Engineer–relevant skills using a structured, production-style Machine Learning pipeline.

Built following industry-standard ML project architecture, including modular components for data processing, training, evaluation, and prediction.

## Tech Stack
- **Language**: Python 3.9+
- **Machine Learning Framework**: TensorFlow / Keras (Sequential Models, TextVectorization)
- **Data Modification**: Pandas & CSV Parsing
- **Data Exploration**: Jupyter Notebooks & Matplotlib
- **Testing**: Pytest (Unit Testing)
- **Environment**: Virtual Env / `pip`

## Project Scope
This project is an end-to-end **Machine Learning Classification Pipeline** built from scratch. It demonstrates the complete lifecycle of a professional AI project:
1. **Data Ingestion (Custom Vocabulary):** Uses TensorFlow's `TextVectorization` to read strictly from a custom dataset (`skills.csv`) and break text down into mathematical arrays, ignoring out-of-vocabulary words.
2. **Model Training (Sequential Neural Network):** Builds a specialized Deep Learning model to mathematically learn the exact weights of what makes a candidate's skill "Google AI Engineer relevant" vs "Non-relevant".
3. **Live Inference (Command-Line Predictions):** Provides a lightweight script (`predict.py`) to instantly calculate live Confidence Scores for any new custom string against the trained `.keras` brain.
4. **Industry Standards (Stability & Visualization):** Includes Data Science visualizations via Jupyter Notebooks for EDA (Exploratory Data Analysis) and an automated Pytest suite to proactively verify the logic integrity of the neural network.

## Project Structure

<pre>
Vector-Profile-Scanner/
├── <a href="./src">src/</a>                    # Core Python modules (model, training, prediction)
│   ├── <a href="./src/data_loader.py">data_loader.py</a>      # Script to load and preprocess data
│   ├── <a href="./src/model.py">model.py</a>            # Neural network architecture definition
│   ├── <a href="./src/train.py">train.py</a>            # Script for training the model
│   └── <a href="./src/predict.py">predict.py</a>          # Script to run predictions on new data
├── <a href="./data">data/</a>                   # Raw and processed datasets needed for training
│   └── <a href="./data/raw">raw/</a>                
│       └── <a href="./data/raw/skills.csv">skills.csv</a>      # The core dataset containing raw profile skills
├── <a href="./notebooks">notebooks/</a>              # Exploratory Data Analysis (EDA) Jupyter notebooks
│   └── <a href="./notebooks/01_data_exploration.ipynb">01_data_exploration.ipynb</a> # Visualizing the dataset imbalance and trends
├── <a href="./tests">tests/</a>                  # Automated pytest verification suite
│   ├── <a href="./tests/__init__.py">__init__.py</a>         # Test package initialization
│   ├── <a href="./tests/test_data_loader.py">test_data_loader.py</a> # Tests for data loading and preprocessing
│   └── <a href="./tests/test_model.py">test_model.py</a>       # Tests for neural network architecture
├── <a href="./models">models/</a>                 # Generated artifacts and TensorFlow `.keras` weights
├── <a href="./requirements.txt">requirements.txt</a>        # Python dependencies
├── <a href="./setup.py">setup.py</a>                # Package installation configuration
└── <a href="./README.md">README.md</a>               # Project documentation
</pre>

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

### 5. Run Web API Server (FastAPI)
```bash
uvicorn src.api:app --reload
```
Navigate to `http://localhost:8000/docs` in your browser to use the interactive Swagger UI.

### 6. Run via Docker
```bash
docker build -t vector-profile-scanner .
docker run -p 8000:8000 vector-profile-scanner
```
