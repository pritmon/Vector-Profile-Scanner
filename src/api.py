from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
from contextlib import asynccontextmanager
from src.utils import load_inference_artifacts
from src.config import MODEL_PATH, VOCAB_PATH

# Global artifacts
artifacts = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load artifacts on startup
    try:
        model, vectorizer = load_inference_artifacts(MODEL_PATH, VOCAB_PATH)
        artifacts["model"] = model
        artifacts["vectorizer"] = vectorizer
    except FileNotFoundError as e:
        print(f"Warning: {e}")
    yield
    # Clean up on shutdown
    artifacts.clear()

app = FastAPI(
    title="Vector Profile Scanner API",
    description="A Machine Learning API to classify if a candidate's skills are relevant for a Google AI Engineer.",
    lifespan=lifespan
)

class SkillRequest(BaseModel):
    skill: str
    
class PredictionResponse(BaseModel):
    skill: str
    classification: str
    confidence: float

@app.post("/predict", response_model=PredictionResponse)
def predict_skill(request: SkillRequest):
    model = artifacts.get("model")
    vectorizer = artifacts.get("vectorizer")
    
    if not model or not vectorizer:
        return {
            "skill": request.skill,
            "classification": "Model not loaded",
            "confidence": 0.0
        }

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
