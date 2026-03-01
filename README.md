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

<pre>
Vector-Profile-Scanner/
├── <a href="./src">src/</a>                    # Core Python modules (model, training, prediction)
│   ├── <a href="./src/data_loader.py">data_loader.py</a>      # Script to load and preprocess data
│   ├── <a href="./src/model.py">model.py</a>            # Neural network architecture definition
│   ├── <a href="./src/train.py">train.py</a>            # Script for training the model
│   └── <a href="./src/predict.py">predict.py</a>          # Script to run predictions on new data
├── <a href="./data">data/</a>                   # Raw and processed datasets needed for training
├── <a href="./notebooks">notebooks/</a>              # Exploratory Data Analysis (EDA) Jupyter notebooks
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
