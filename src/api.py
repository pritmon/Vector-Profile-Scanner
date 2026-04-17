from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
from contextlib import asynccontextmanager
from src.utils import load_inference_artifacts
from src.config import MODEL_PATH, VOCAB_PATH

from fastapi.middleware.cors import CORSMiddleware
import time

# Global artifacts
artifacts = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load artifacts on startup
    print("🚀 Starting API server and loading ML artifacts...")
    start_time = time.time()
    try:
        model, vectorizer = load_inference_artifacts(MODEL_PATH, VOCAB_PATH)
        artifacts["model"] = model
        artifacts["vectorizer"] = vectorizer
        duration = time.time() - start_time
        print(f"✅ ML artifacts loaded successfully in {duration:.2f}s")
    except FileNotFoundError as e:
        print(f"❌ Failed to load artifacts: {e}")
        print("💡 Hint: Run 'python -m src.train' first.")
    yield
    # Clean up on shutdown
    print("🛑 Shutting down API server...")
    artifacts.clear()

app = FastAPI(
    title="Vector Profile Scanner API",
    description="Enterprise-grade AI Skill Classification Engine.",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS for frontend integrations
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.responses import RedirectResponse

@app.get("/", include_in_schema=False)
def root_placeholder():
    return RedirectResponse(url="/docs")

@app.get("/health")
def health_check():
    """Service health monitoring endpoint."""
    status = "ready" if artifacts.get("model") else "warning: model not loaded"
    return {"status": status, "timestamp": time.time()}


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
