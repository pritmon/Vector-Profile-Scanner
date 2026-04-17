# Vector Profile Scanner

A TensorFlow-powered skill classification system that identifies Google AI Engineer–relevant skills using a structured, production-style Machine Learning pipeline.

Built following industry-standard ML project architecture, including modular components for data processing, training, evaluation, and prediction.

**Live Web API Demo:** [https://vector-profile-scanner.onrender.com/docs](https://vector-profile-scanner.onrender.com/docs) *(Replace with your actual deployed URL)*

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
├── <a href="./.github">.github/</a>                # CI/CD pipeline automation and MLOps integrations
├── <a href="./artifacts">artifacts/</a>              # Detailed technical documentation, FAQs, and system glossaries
├── <a href="./src">src/</a>                    # Core engine for data ingestion, training algorithms, and inference
│   ├── <a href="./src/api.py">api.py</a>              # Asynchronous FastAPI gateway serving real-time model inference
│   ├── <a href="./src/config.py">config.py</a>           # Centralized environment constants routing all data and model paths
│   ├── <a href="./src/data_loader.py">data_loader.py</a>      # Orchestrates dataset ingestion and TextVectorization pipelines
│   ├── <a href="./src/model.py">model.py</a>            # Compiles the neural network geometry and binary loss functions
│   ├── <a href="./src/predict.py">predict.py</a>          # Instantiates learned tensors to confidently score new data inputs
│   ├── <a href="./src/train.py">train.py</a>            # Executes the ML training lifecycle to generate `.keras` weights
│   └── <a href="./src/utils.py">utils.py</a>            # Reusable resource dependencies enforcing DRY software principles
├── <a href="./data">data/</a>                   # Data storage layer for raw and processed classification assets
│   └── <a href="./data/raw">raw/</a>                
│       └── <a href="./data/raw/skills.csv">skills.csv</a>      # Hand-curated dataset mapping raw strings to probability labels
├── <a href="./notebooks">notebooks/</a>              # Interactive Jupyter scratchpads for Data Scientists
│   └── <a href="./notebooks/01_data_exploration.ipynb">01_data_exploration.ipynb</a> # Visual telemetry plotting class imbalances and token trends
├── <a href="./tests">tests/</a>                  # Automated quality assurance and mathematical constraint suite
│   ├── <a href="./tests/__init__.py">__init__.py</a>         # Initialization registry for the local test packages
│   ├── <a href="./tests/test_data_loader.py">test_data_loader.py</a> # Mathematically validates CSV ingestion logic and tensor shapes
│   └── <a href="./tests/test_model.py">test_model.py</a>       # Asserts the network compiles with correct probability thresholds
├── <a href="./models">models/</a>                 # Secure artifact directory holding the compiled AI intelligence
├── <a href="./requirements.txt">requirements.txt</a>        # Hard-coded dependency locker for strict environment clones
├── <a href="./setup.py">setup.py</a>                # Local package constructor converting `src/` into a pip module
├── <a href="./Dockerfile">Dockerfile</a>              # Immutable container blueprint assembling the OS and AI engine
├── <a href="./.dockerignore">.dockerignore</a>           # Security definitions excluding sensitive or bloated cache files
├── <a href="./LICENSE">LICENSE</a>                 # Formal MIT Open-Source software distribution legality
└── <a href="./README.md">README.md</a>               # High-level architecture overview and execution instructions
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
PYTHONPATH=. python3 -m src.train
```

### 2. Predict a Skill
```bash
PYTHONPATH=. python3 -m src.predict "Vertex AI"
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
python3 -m uvicorn src.api:app --reload
```
Navigate to `http://localhost:8000/docs` in your browser to use the interactive Swagger UI.

### 6. Run via Docker
```bash
docker build -t vector-profile-scanner .
docker run -p 8000:8000 vector-profile-scanner
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
