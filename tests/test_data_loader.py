import pytest
import tensorflow as tf
import os
from src.data_loader import load_data, create_vectorizer

# Use the real test CSV that is guaranteed to exist
TEST_CSV_PATH = 'data/raw/skills.csv'

def test_load_data_returns_correct_types():
    # Ensure the CSV exists before testing
    assert os.path.exists(TEST_CSV_PATH), f"Test CSV not found at {TEST_CSV_PATH}"
    
    data, labels = load_data(TEST_CSV_PATH)
    
    assert isinstance(data, list)
    assert len(data) > 0
    assert isinstance(labels, tf.Tensor)
    assert len(data) == labels.shape[0]

def test_create_vectorizer_returns_adapted_layer():
    dummy_data = ["Python", "TensorFlow", "Cooking"]
    vectorizer = create_vectorizer(dummy_data)
    
    assert isinstance(vectorizer, tf.keras.layers.TextVectorization)
    assert vectorizer.vocabulary_size() > 0
    
    # Test encoding
    encoded = vectorizer([["Python"]])
    assert encoded.shape[1] > 0
