# Vector Profile Scanner: Project Fixes & Updates Log

This document summarizes all the fixes, restructuring, and improvements applied to the project from its initial conceptualization to its current state.

## 1. Initial Implementation & Fixes
*   **Created Base Script:** Originated the `beginner_tf.py` script as a single-file TensorFlow project to distinguish between Google AI Engineer skills and non-relevant skills.
*   **Resolved Dependency Error:** Fixed the `ModuleNotFoundError` by installing `tensorflow` and its required packages into the local Python environment.
*   **Model Optimization:** Increased the model training duration from 100 epochs to 500 epochs to ensure the neural network fully learned the small dataset, resulting in accurate confidence scores.

## 2. Git Setup & Name Correction
*   **Initialized Version Control:** Configured the local directory as a Git repository to enable source control.
*   **Created `README.md` & `.gitignore`:** Provided a project overview and ensured standard Python temporary files (e.g., `__pycache__`) were ignored.
*   **Renamed Project:** Updated the repository name in the README from "Beginner TensorFlow Project" to exactly match the workspace: **Vector Profile Scanner**.
*   **Pushed to GitHub:** Connected the local repository to the new remote GitHub repository.

## 3. Absolute Repository Restructuring
*   **Modular Architecture:** Refactored the single script into a standard ML project structure (`src/`, `data/`, `models/`).
*   **Ignored ML Artifacts:** Updated `.gitignore` to prevent the `models/` directory from being committed to GitHub.

## 4. IDE (VS Code) Environment Fix
*   **Resolved Python Interpreter Warning:** Removed the persistent "Select a Python Environment" popup in VS Code by explicitly creating the `.vscode/settings.json` file pointing to `/usr/bin/python3`.

## 5. Top-Tier Google ML Architecture Upgrades
*   **Automated Testing Suite:** Implemented `pytest` via a dedicated `tests/` directory containing unit tests (`test_data_loader.py` and `test_model.py`) to validate dataset loading and neural network integrity.
*   **Data Exploration Space:** Established a `notebooks/` directory and generated `01_data_exploration.ipynb` to allow Data Scientists to perform EDA (Exploratory Data Analysis) visually without touching core architecture files. 
*   **Environment Reproducibility:** Locked exact dependency versions using a permanent `requirements.txt` file (e.g., locking TensorFlow to `2.20.0`) and provided an `.env.example` template for secure credential management.
*   **Project Packaging:** Built a `setup.py` configuration to package the `src/` directory natively, allowing the project to be installed and run locally as a seamless pip package module.

## 6. Architecture Modernization & Reliability Fixes
*   **Added Open-Source Licensing:** Generated the `LICENSE` file under the MIT standard and updated `README.md` and `setup.py` classifiers to formally protect and grant usage of the repository.
*   **DRY Architecture Refactor:** Eliminated hardcoded paths and duplicated model loading scripts across `api.py` and `predict.py` by centralizing path states via `src/config.py` and loading functions via `src/utils.py`.
*   **FastAPI API Upgrade:** Modernized the core web server (`src/api.py`) by replacing the officially deprecated `@app.on_event("startup")` initialization block with the robust `@asynccontextmanager lifespan(app: FastAPI)` design pattern. Also added grace protections to avoid crashes if models aren't trained yet.
*   **Prevented Overfitting:** Lowered the core `src/train.py` lifecycle from 500 epochs to 100 epochs as the initial high training interval aggressively forced exact mathematical overfitting on a micro-dataset (30 samples).
*   **Fixed CI Pipeline Integrity:** Corrected a severe execution flaw in `.github/workflows/ci.yml` that raised `ModuleNotFoundError` by enforcing strict python module executions (`PYTHONPATH=. python -m src.train` and `... pytest tests/`) assuring that GitHub actions correctly recognized the local path directory instead of failing.
*   **Self-Contained Docker Model Build:** Rewrote the `Dockerfile` to automatically self-train (`RUN PYTHONPATH=. python -m src.train`) after dependency installation. Because weights (`models/`) are deliberately `.gitignore`'d, the original Docker instance booted empty. Generating models *during* the image build permanently bakes the intelligent weights inside the container.
