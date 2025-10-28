# ML Ball Tracking Service

This package contains the machine learning model for detecting and tracking balls in sports videos.

## Overview

The ball tracking model uses a PyTorch-based deep learning approach with a ResNet backbone for:
- Ball detection (presence/absence classification)
- Ball localization (position prediction)

## Structure

```
ml-ball-tracking/
├── src/
│   ├── model.py       # Model architecture
│   ├── train.py       # Training script
│   └── inference.py   # Inference utilities (TODO)
├── tests/             # Unit tests
├── data/              # Training data (not committed)
├── models/            # Trained models (not committed)
└── requirements.txt   # Python dependencies
```

## Getting Started

### Installation

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Training

```bash
# Run training (when data is available)
python src/train.py --data-dir data/ --output-dir models/ --epochs 50
```

### Testing the Model

```bash
# Test model creation
python src/model.py
```

## TODO

- [ ] Implement data loading pipeline
- [ ] Add data augmentation
- [ ] Implement inference script
- [ ] Add model evaluation metrics
- [ ] Create Docker container for training/inference
- [ ] Integrate with CDK for SageMaker deployment
- [ ] Add video processing utilities
- [ ] Implement tracking across frames (temporal coherence)
