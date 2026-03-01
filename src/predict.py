"""
Prediction module for the Vector Profile Scanner.

Loads the trained model and vocabulary artifacts from the `models/` directory,
and provides a command-line interface to classify if a given skill is relevant 
to a Google AI Engineer role.
"""
import tensorflow as tf
import pickle
import argparse

def load_inference_artifacts():
    """
    Loads the trained model and recreates the TextVectorization layer.
    
    Returns:
        tuple: (Compiled Keras model, Initialized TextVectorization layer)
    """
    model = tf.keras.models.load_model('models/skill_classifier.keras')
    
    with open('models/vectorizer_vocab.pkl', 'rb') as f:
        vocab = pickle.load(f)
        
    vectorizer = tf.keras.layers.TextVectorization(
        output_mode='count',
        standardize='lower_and_strip_punctuation',
        split='whitespace'
    )
    vectorizer.set_vocabulary(vocab)
    
    return model, vectorizer

def predict(skill):
    """
    Predicts the relevance of a single skill string.
    
    Args:
        skill (str): The skill text to classify (e.g. "TensorFlow")
    """
    model, vectorizer = load_inference_artifacts()
    
    # Run vectorization
    X = vectorizer([skill])
    
    # Check for completely unknown vocabulary
    # If the sum of the count array is 0, the model knows literally none 
    # of the words in the input. Force a 0% confidence to prevent 
    # the Dense layer from predicting its mathematical baseline bias.
    if tf.reduce_sum(X).numpy() == 0:
        prediction = 0.0
    else:
        # Run standard prediction
        prediction = model.predict(X, verbose=0)[0][0]
    
    # Output result
    category = "Google AI Engineer Skill" if prediction > 0.5 else "Non-relevant"
    print(f"\n--- Prediction Result ---")
    print(f"Skill: '{skill}'")
    print(f"Classification: {category} (Confidence: {prediction:.2f})\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Predict if a skill is relevant for an AI Engineer at Google.')
    parser.add_argument('skill', type=str, help='The skill name to predict (e.g., "Vertex AI")')
    args = parser.parse_args()
    
    predict(args.skill)
