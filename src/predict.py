import tensorflow as tf
import pickle
import argparse

def load_inference_artifacts():
    """Loads the trained model and recreates the TextVectorization layer."""
    model = tf.keras.models.load_model('models/skill_classifier.keras')
    
    with open('models/vectorizer_vocab.pkl', 'rb') as f:
        vocab = pickle.load(f)
        
    vectorizer = tf.keras.layers.TextVectorization(output_mode='multi_hot')
    vectorizer.set_vocabulary(vocab)
    
    return model, vectorizer

def predict(skill):
    model, vectorizer = load_inference_artifacts()
    
    # Run prediction
    X = vectorizer([skill])
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
