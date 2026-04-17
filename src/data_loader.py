import os
import pandas as pd
import tensorflow as tf
from src.config import DATA_PATH

def load_data(filepath=DATA_PATH):
    """
    Loads and validates the skill dataset from a CSV file.
    Specifically checks for the existence of 'skill' and 'label' columns.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at {filepath}")
        
    df = pd.read_csv(filepath)
    
    # Audit: Ensure required columns are present
    required_cols = {'skill', 'label'}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"Dataset is missing required columns: {required_cols - set(df.columns)}")
    
    # Audit: Drop empty rows to prevent model crashes
    df = df.dropna(subset=['skill', 'label'])
    
    return df['skill'].values, tf.convert_to_tensor(df['label'].values, dtype=tf.float32)


def create_vectorizer(data):
    """Creates and adapts a TextVectorization layer."""
    vectorizer = tf.keras.layers.TextVectorization(
        output_mode='count', 
        standardize='lower_and_strip_punctuation',
        split='whitespace'
    )
    vectorizer.adapt(data)
    return vectorizer
