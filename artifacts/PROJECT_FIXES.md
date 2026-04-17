# 🛠️ Vector Profile Scanner: Project Fixes & Updates Log

> [!NOTE]
> This document tracks the evolution, architectural restructuring, and pipeline enhancements applied to the Vector Profile Scanner—from its initial script concept to a production-ready ML system.

---

## 🏗️ Phase 1: Foundation & Setup
*The initial lifecycle of creating the model and moving to a version-controlled workspace.*

| Component | Action Taken | Impact / Benefit |
| :--- | :--- | :--- |
| **Base Script** | Created `beginner_tf.py` to distinguish Google AI Engineer skills. | Established the core logic for the TensorFlow binary classification. |
| **Dependencies** | Resolved `ModuleNotFoundError` by isolating package installations. | Ensured the environment had exactly what the script needed to run. |
| **Version Control** | Initialized standard Git tracking, pushed to remote GitHub. | Secured code history and enabled cloud backups/sharing. |
| **Workspace Curation** | Created `.gitignore` and `README.md`. Renamed to *Vector Profile Scanner*. | Prevented cache files from bloating git; improved professional appearance. |
| **IDE Fixes** | Generated `.vscode/settings.json` pointing to the correct local framework. | Eliminated annoying "Select Interpreter" warnings for developers using VS Code. |

---

## 🧠 Phase 2: Architecture & ML Pipeline Refactoring
*Transforming the single script into a scalable, modular Machine Learning architecture.*

| Component | Action Taken | Impact / Benefit |
| :--- | :--- | :--- |
| **Modularization** | Refactored script into distinct `src/`, `data/`, and `models/` directories. | Codebase is now scalable and conforms to top-tier Python ML standards. |
| **DRY Principles** | Centralized paths into `src/config.py` and model-loading into `src/utils.py`. | Eliminated hardcoded paths; made `api.py` and `predict.py` easier to scale and maintain. |
| **Overfitting Fix** | Reduced TensorFlow training epochs from `500` down to `100`. | Stopped the neural network from catastrophically mathematical overfitting on the tiny payload. |
| **Model Verification** | Added `pytest` framework with `test_data_loader.py` and `test_model.py`. | Guarantees code integrity and mathematical shapes automatically without manual testing. |
| **EDA Space** | Added `notebooks/01_data_exploration.ipynb`. | Provides Data Scientists a native Jupyter environment for exploratory dataset visualization. |

---

## 🚀 Phase 3: Infrastructure & Deployment
*Hardening the application for production release, containerization, and cloud pipelines.*

| Component | Action Taken | Impact / Benefit |
| :--- | :--- | :--- |
| **Native Packaging** | Engineered `setup.py` and locked versions in `requirements.txt`. | Allows the project to be smoothly installed or embedded into larger ecosystems via `pip install -e .`. |
| **Open-Source** | Added MIT `LICENSE` file and populated `setup.py` metadata classifiers. | Formally protects the developer from liability while granting community open-source rights. |
| **FastAPI Upgrade** | Replaced deprecated startup components with `@asynccontextmanager lifespan`. | Modernized the web server while adding graceful protections and warnings for missing models artifacts. |
| **Docker Reliability** | Forced the `Dockerfile` to self-train (`python -m src.train`) during image build. | Bakes the intelligence into the container autonomously, overcoming `.gitignore` artifact exclusion limitations. |
| **CI/CD Hardening** | Enforced strict `PYTHONPATH=. python -m` contexts in `.github/workflows/ci.yml`. | Resolved `ModuleNotFoundError` execution failures running inside GitHub's automated validation suites. |
