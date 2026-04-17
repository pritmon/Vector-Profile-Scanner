import os
import pickle
import tensorflow as tf

def load_inference_artifacts(model_path, vocab_path):
    """
    Loads the trained model and recreates the TextVectorization layer.
    
    Args:
        model_path (str): Path to the .keras model file.
        vocab_path (str): Path to the pickled vocabulary file.
        
    Returns:
        tuple: (Keras model, TextVectorization layer)
        
    Raises:
        FileNotFoundError: If the model or vocab files are missing.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model artifact not found at: {model_path}. Please run training first.")
    
    if not os.path.exists(vocab_path):
        raise FileNotFoundError(f"Vocabulary artifact not found at: {vocab_path}. Please run training first.")

    model = tf.keras.models.load_model(model_path)
    
    with open(vocab_path, 'rb') as f:
        vocab = pickle.load(f)
        
    vectorizer = tf.keras.layers.TextVectorization(
        output_mode='count',
        standardize='lower_and_strip_punctuation',
        split='whitespace'
    )
    vectorizer.set_vocabulary(vocab)
    
    return model, vectorizer
