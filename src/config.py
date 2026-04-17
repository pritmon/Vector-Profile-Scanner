import os

# Base Directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data', 'raw')
MODEL_DIR = os.path.join(BASE_DIR, 'models')

# File Paths
DATA_PATH = os.path.join(DATA_DIR, 'skills.csv')
MODEL_PATH = os.path.join(MODEL_DIR, 'skill_classifier.keras')
VOCAB_PATH = os.path.join(MODEL_DIR, 'vectorizer_vocab.pkl')
