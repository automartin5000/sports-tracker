"""
Training script for the ball tracking model.

This script will train the ball detection model on annotated sports video frames.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from typing import Optional
import argparse
from pathlib import Path

from model import create_model


class BallTrackingDataset(Dataset):
    """
    Dataset for ball tracking.
    
    TODO: Implement data loading from annotated video frames.
    Expected format:
    - Images: video frames
    - Labels: ball presence (0/1) and position (x, y) if present
    """
    
    def __init__(self, data_dir: Path, transform=None):
        self.data_dir = data_dir
        self.transform = transform
        # TODO: Load annotations and image paths
        
    def __len__(self):
        # TODO: Return dataset size
        return 0
    
    def __getitem__(self, idx):
        # TODO: Load image and labels
        raise NotImplementedError("Dataset loading not yet implemented")


def train_epoch(
    model: nn.Module,
    dataloader: DataLoader,
    optimizer: optim.Optimizer,
    device: torch.device,
    epoch: int
) -> float:
    """Train for one epoch."""
    model.train()
    total_loss = 0.0
    
    # Loss functions
    bce_loss = nn.BCELoss()
    mse_loss = nn.MSELoss()
    
    for batch_idx, (images, presence_labels, position_labels) in enumerate(dataloader):
        images = images.to(device)
        presence_labels = presence_labels.to(device)
        position_labels = position_labels.to(device)
        
        optimizer.zero_grad()
        
        # Forward pass
        presence_pred, position_pred = model(images)
        
        # Compute losses
        cls_loss = bce_loss(presence_pred, presence_labels)
        reg_loss = mse_loss(position_pred, position_labels)
        
        # Combined loss
        loss = cls_loss + reg_loss
        
        # Backward pass
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        
        if batch_idx % 10 == 0:
            print(f"Epoch {epoch} [{batch_idx}/{len(dataloader)}] Loss: {loss.item():.4f}")
    
    return total_loss / len(dataloader)


def main(args):
    """Main training function."""
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    # Create model
    model = create_model(pretrained=True)
    model = model.to(device)
    
    # TODO: Create dataset and dataloader
    # train_dataset = BallTrackingDataset(args.data_dir)
    # train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True)
    
    # Optimizer
    optimizer = optim.Adam(model.parameters(), lr=args.learning_rate)
    
    # Training loop
    print(f"Starting training for {args.epochs} epochs...")
    for epoch in range(args.epochs):
        # avg_loss = train_epoch(model, train_loader, optimizer, device, epoch)
        # print(f"Epoch {epoch} completed. Average loss: {avg_loss:.4f}")
        
        # Save checkpoint
        if (epoch + 1) % args.save_every == 0:
            checkpoint_path = Path(args.output_dir) / f"checkpoint_epoch_{epoch+1}.pth"
            checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
            }, checkpoint_path)
            print(f"Checkpoint saved to {checkpoint_path}")
    
    # Save final model
    final_model_path = Path(args.output_dir) / "ball_tracking_model.pth"
    torch.save(model.state_dict(), final_model_path)
    print(f"Final model saved to {final_model_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train ball tracking model")
    parser.add_argument("--data-dir", type=str, default="data/", help="Path to training data")
    parser.add_argument("--output-dir", type=str, default="models/", help="Path to save models")
    parser.add_argument("--epochs", type=int, default=50, help="Number of training epochs")
    parser.add_argument("--batch-size", type=int, default=32, help="Batch size")
    parser.add_argument("--learning-rate", type=float, default=1e-4, help="Learning rate")
    parser.add_argument("--save-every", type=int, default=10, help="Save checkpoint every N epochs")
    
    args = parser.parse_args()
    main(args)
