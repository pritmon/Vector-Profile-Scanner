"""
Training module for the Vector Profile Scanner.

Loads raw skill data, creates a TextVectorization layer,
builds the TensorFlow model, trains it, and saves the final
artifacts to the `models/` directory.
"""
import pickle
import os
from data_loader import load_data, create_vectorizer
from model import build_model

def train():
    """
    Executes the full training pipeline.
    
    Steps:
    1. Loads dataset of skills and labels.
    2. Initializes and adapts the TextVectorizer.
    3. Builds a dense Sequential model.
    4. Trains the model for 500 epochs.
    5. Saves the model and vocabulary locally.
    """
    print("Loading data...")
    data, labels = load_data()
    
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report
    
    data_train, data_test, y_train, y_test = train_test_split(
        data, labels.numpy(), test_size=0.2, random_state=42
    )
    
    print("Creating vectorizer...")
    vectorizer = create_vectorizer(data_train)
    X_train = vectorizer(data_train)
    X_test = vectorizer(data_test)
    
    print("Building model...")
    model = build_model(input_shape=X_train.shape[1])
    
    print("Training model...")
    model.fit(X_train, y_train, epochs=500, verbose=0)
    
    print("\n--- Evaluating Model on Test Data ---")
    predictions = model.predict(X_test, verbose=0)
    y_pred = (predictions > 0.5).astype(int)
    
    print(classification_report(y_test, y_pred, target_names=["Non-relevant", "AI Skill"]))

    
    print("Saving model and vectorizer...")
    os.makedirs('models', exist_ok=True)
    model.save('models/skill_classifier.keras')
    
    # Save the vectorizer's vocabulary for predicting later
    with open('models/vectorizer_vocab.pkl', 'wb') as f:
        pickle.dump(vectorizer.get_vocabulary(), f)
        
    print("Training complete! Model saved to models/")

if __name__ == '__main__':
    train()
