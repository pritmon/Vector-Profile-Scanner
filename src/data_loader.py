import csv
import tensorflow as tf

def load_data(filepath='data/raw/skills.csv'):
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
    # Using 'count' mode ensures that any word not in the vocabulary
    # simply results in a sum of 0. It prevents the model from explicitly 
    # learning a positive bias weight for the special [UNK] (Unknown) token.
    vectorizer = tf.keras.layers.TextVectorization(
        output_mode='count', 
        standardize='lower_and_strip_punctuation',
        split='whitespace'
    )
    vectorizer.adapt(data)
    return vectorizer
