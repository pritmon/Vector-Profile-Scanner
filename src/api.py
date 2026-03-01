from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import pickle

app = FastAPI(
    title="Vector Profile Scanner API",
    description="A Machine Learning API to classify if a candidate's skills are relevant for a Google AI Engineer."
)

# Initialize global model variables
model = None
vectorizer = None

@app.on_event("startup")
def load_artifacts():
    global model, vectorizer
    model = tf.keras.models.load_model('models/skill_classifier.keras')
    with open('models/vectorizer_vocab.pkl', 'rb') as f:
        vocab = pickle.load(f)
    vectorizer = tf.keras.layers.TextVectorization(
        output_mode='count',
        standardize='lower_and_strip_punctuation',
        split='whitespace'
    )
    vectorizer.set_vocabulary(vocab)

class SkillRequest(BaseModel):
    skill: str
    
class PredictionResponse(BaseModel):
    skill: str
    classification: str
    confidence: float

@app.post("/predict", response_model=PredictionResponse)
def predict_skill(request: SkillRequest):
    # Run vectorization
    X = vectorizer([request.skill])
    
    # Check for Out-Of-Vocabulary
    if tf.reduce_sum(X).numpy() == 0:
        prediction = 0.0
    else:
        prediction = float(model.predict(X, verbose=0)[0][0])
        
    category = "Google AI Engineer Skill" if prediction > 0.5 else "Non-relevant"
    return {
        "skill": request.skill,
        "classification": category,
        "confidence": prediction
    }
