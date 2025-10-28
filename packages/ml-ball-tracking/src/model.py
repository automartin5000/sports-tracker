"""
Ball tracking model using PyTorch.

This is a starter implementation for ball detection and tracking in sports videos.
The model will be trained to detect and track ball positions across video frames.
"""

import torch
import torch.nn as nn
import torchvision.models as models
from typing import Tuple


class BallDetectionModel(nn.Module):
    """
    Ball detection model based on a pre-trained ResNet backbone.
    
    This model outputs:
    - Ball presence probability (classification)
    - Ball position coordinates (x, y) (regression)
    """
    
    def __init__(self, pretrained: bool = True):
        super(BallDetectionModel, self).__init__()
        
        # Use ResNet18 as backbone
        self.backbone = models.resnet18(pretrained=pretrained)
        
        # Remove the final fully connected layer
        num_features = self.backbone.fc.in_features
        self.backbone.fc = nn.Identity()
        
        # Classification head: ball present or not
        self.classifier = nn.Sequential(
            nn.Linear(num_features, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )
        
        # Regression head: ball position (x, y)
        self.regressor = nn.Sequential(
            nn.Linear(num_features, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 2),
            nn.Sigmoid()  # Output normalized coordinates [0, 1]
        )
    
    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Forward pass.
        
        Args:
            x: Input image tensor of shape (batch, 3, height, width)
            
        Returns:
            Tuple of (presence_prob, position)
            - presence_prob: Ball presence probability (batch, 1)
            - position: Ball position coordinates (batch, 2)
        """
        features = self.backbone(x)
        presence = self.classifier(features)
        position = self.regressor(features)
        
        return presence, position


def create_model(pretrained: bool = True) -> BallDetectionModel:
    """
    Create a ball detection model.
    
    Args:
        pretrained: Whether to use pretrained ResNet weights
        
    Returns:
        BallDetectionModel instance
    """
    return BallDetectionModel(pretrained=pretrained)


if __name__ == "__main__":
    # Simple test
    model = create_model(pretrained=False)
    dummy_input = torch.randn(2, 3, 224, 224)
    presence, position = model(dummy_input)
    
    print(f"Model created successfully!")
    print(f"Input shape: {dummy_input.shape}")
    print(f"Presence output shape: {presence.shape}")
    print(f"Position output shape: {position.shape}")
