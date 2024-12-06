# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from dataclasses import dataclass

@dataclass
class PretrainedModel:
    model_name: str