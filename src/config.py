
SEED = 42

# CLASS MAPPING
LABEL_MAPPING = {
    "branding": 0,
    "headline_text": 1,
    "body_text": 2,
    "call_to_action_(cta)": 3,
    "product": 4
}

USED_MODEL = "src/models/yolo11x.pt"

# MODEL TRAINING SET-UP
EPOCHS = 100
IMGSZ = 640 #1280
BATCH_SIZE = 8
PATIENCE = 30
PROJECT = './runs/train'
DETERMINISTIC = False

#MODEL HYPERPARAMETERS
OPTIMIZER = "AdamW"
COS_LR = False
LR0 = 0.00001
LRF = 0.001
MOMENTUM = 0.9
BOX = 3.5
CLS = 1.5
WEIGHT_DECAY = 0.0001

# Warmup
WARMUP_EPOCHS = 5.0
WARMUP_MOMENTUM = 0.69

# Augmentation parameters
AUTO_AUGMENT = "randaugment"
CLOSE_MOSAIC = 5
MOSAIC = 0.2
MIXUP = 0.1
COPY_PASTE = 0.408