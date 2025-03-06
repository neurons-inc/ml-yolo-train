## YOLO Training with in-house 100 Images

## Trained Model
Final trained model (based on YOLO 11x.pt) can be found here:
https://drive.google.com/drive/folders/1zOcGuUJ2aAbJeBkJ-0oF-pyioVVuMtdS?usp=sharing

## Purpose Overview  
This YOLO model is trained for **object detection** on a dataset of static assets categorized into five key classes:  
- **Branding**  
- **Headline Text**  
- **Body Text**  
- **Call-to-Action (CTA)**  
- **Product**  

The dataset follows the YOLO format with:  
- **Training images**: `src/data/images/train`  
- **Validation images**: `src/data/images/val`  
- **Test images**: Uses the same validation set (`src/data/images/val`)  

The model aims to **accurately detect and classify these elements** within images, supporting **ad performance analysis and content optimization**.

---

## Repository Structure  
This repo contains **everything needed** to train or retrain the YOLO model for AOI (Area of Interest) detection.

### 1. Core Model Training Components  
- **`data/`** – Example of YOLO dataset structure. Replace the images and label files with the actual training data.  
- **`models/`** – Placeholder folder for model checkpoints. The latest YOLO model is **not included** and can be downloaded using Ultralytics.  
- **`runs/`** – Stores training outputs. Currently empty but will populate after running the training.  
- **`src/`** – Contains the `config.py` file defining hyperparameters and model training settings.  
- **`train_yolo11.py`** – Main Python script for YOLO training, using configurations from `config.py`.  
- **`yolo_train.yaml`** – Defines the dataset structure, including **image locations, labels, and class definitions**.  

### 2. Data Preparation & Visualization  
- **`train_yolo11.py`** also includes some **training visualizations**.  
- If additional visualization is needed, **ClearML** can be used to log and track training performance.  

---

## Installation  
To install dependencies, run:  

```
pip install -r requirements.txt
```

## License
See **`LICENSE` file


**Contact:**  i.white@neuronsinc.com

This project was developed for internal content analysis at Neurons Inc.
