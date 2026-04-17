import csv
import tensorflow as tf
from src.config import DATA_PATH

def load_data(filepath=DATA_PATH):
    """Loads text data and labels from a CSV file."""
    data = []
    labels = []
    
    with open(filepath, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row['skill'])
            labels.append(int(row['label']))
            
    return data, tf.constant(labels)

def create_vectorizer(data):
    """Creates and adapts a TextVectorization layer."""
    vectorizer = tf.keras.layers.TextVectorization(
        output_mode='count', 
        standardize='lower_and_strip_punctuation',
        split='whitespace'
    )
    vectorizer.adapt(data)
    return vectorizer
