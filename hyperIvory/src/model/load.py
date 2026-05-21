import os
from strands.models import GeminiModel  # provided by strands-agents

# Default Gemini model; override via GEMINI_MODEL_ID
MODEL_ID = os.getenv("GEMINI_MODEL_ID", "gemini-1.5-flash")

def load_model() -> GeminiModel:
    """
    Get Gemini model client using Google Generative AI API (not Bedrock).
    Requires GOOGLE_API_KEY in the environment.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY is required to use Gemini outside Bedrock.")
    return GeminiModel(api_key=api_key, model_id=MODEL_ID)