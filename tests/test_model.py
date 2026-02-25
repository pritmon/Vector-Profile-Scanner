import pytest
import tensorflow as tf
from src.model import build_model

def test_build_model_architecture():
    # Assume the TextVectorization layer outputs a shape of 10
    input_shape = 10
    model = build_model(input_shape)
    
    # Verify it is a Keras Sequential model
    assert isinstance(model, tf.keras.Sequential)
    
    # The output should just be a single probability float per item
    assert model.output_shape == (None, 1)
    
    # Ensure the loss function is correct for Binary Classification
    assert model.loss == 'binary_crossentropy'
