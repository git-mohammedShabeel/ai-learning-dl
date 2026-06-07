from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
EXPERIMENTS_DIR = BASE_DIR / "experiments"

SUMMARIZATION_MODEL = "facebook/bart-large-cnn"
QA_MODEL = "deepset/roberta-base-squad2"
VIT_MODEL = "google/vit-base-patch16-224"

MAX_INPUT_LENGTH = 1024
MAX_OUTPUT_LENGTH = 256
BATCH_SIZE = 8
LEARNING_RATE = 2e-5
EPOCHS = 3