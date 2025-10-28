# Sports Tracker Architecture

## Overview

The Sports Tracker is a monorepo-based application that uses dual iPhone cameras in a 3D printed holder to capture and analyze sports videos. The system provides automatic ball and player tracking using machine learning.

## Monorepo Structure

```
sports-tracker/
├── packages/
│   ├── infra/              # AWS CDK Infrastructure
│   ├── frontend/           # SvelteKit Web Application
│   └── ml-ball-tracking/   # PyTorch ML Model
├── .projenrc.ts           # Root projen configuration
└── package.json           # Workspace configuration
```

## Technology Stack

### Frontend
- **Framework**: SvelteKit
- **Language**: TypeScript
- **Features**: 
  - Video upload interface
  - Video playback and analysis
  - Real-time tracking visualization

### Infrastructure (AWS CDK)
- **S3**: Video storage with lifecycle policies
- **API Gateway**: RESTful API for frontend-backend communication
- **Lambda**: Serverless video processing functions
- **SageMaker**: ML model hosting and inference
- **CloudWatch**: Monitoring and logging

### ML Service
- **Framework**: PyTorch
- **Architecture**: ResNet-based detection model
- **Capabilities**:
  - Ball detection (classification)
  - Ball localization (regression)
  - Frame-by-frame tracking
  
## Data Flow

1. **Video Capture**: Dual iPhone cameras capture video simultaneously
2. **Upload**: Videos uploaded to S3 via frontend
3. **Processing**: Lambda functions trigger video processing
4. **Stitching**: Combine dual camera views into single panoramic view
5. **ML Inference**: SageMaker endpoint processes frames for ball/player tracking
6. **Storage**: Processed videos and tracking data stored in S3
7. **Visualization**: Frontend displays tracking overlays on video playback

## Development Workflow

### Local Development

```bash
# Install all dependencies
npm install

# Run frontend in dev mode
npm run dev:frontend

# Build all packages
npm run build:all

# Run all tests
npm run test:all
```

### ML Model Development

```bash
cd packages/ml-ball-tracking
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Test model
python src/model.py

# Train model (when data available)
python src/train.py --data-dir data/ --epochs 50
```

### Infrastructure Deployment

```bash
# Deploy to AWS
npm run deploy:infra

# Or manually
cd packages/infra
npm run deploy
```

## CI/CD Pipeline

The project uses GitHub Actions for continuous integration:

1. **Build**: All packages are built and tested
2. **Lint**: Code quality checks with ESLint
3. **Test**: Unit tests for infrastructure and frontend
4. **Deploy**: (Future) Automatic deployment to staging/production

## ML Model Architecture

### BallDetectionModel

- **Backbone**: ResNet18 (pretrained on ImageNet)
- **Classification Head**: Ball presence detection
  - Input: ResNet features (512-dim)
  - Output: Binary probability (present/absent)
- **Regression Head**: Ball position prediction
  - Input: ResNet features (512-dim)
  - Output: Normalized coordinates (x, y) in [0, 1]

### Training Pipeline

1. **Data Preparation**: Annotated video frames with ball positions
2. **Augmentation**: Random flips, crops, color jitter
3. **Loss Function**: BCE for classification + MSE for regression
4. **Optimization**: Adam optimizer
5. **Evaluation**: Precision, recall, localization error

## Future Enhancements

### Phase 1: Core Functionality
- [ ] Video upload API
- [ ] Video stitching pipeline
- [ ] Basic ball tracking
- [ ] Simple playback UI

### Phase 2: Advanced Features
- [ ] Player tracking and identification
- [ ] Multi-object tracking
- [ ] Real-time processing
- [ ] Advanced analytics (heatmaps, trajectories)

### Phase 3: Production Features
- [ ] User authentication
- [ ] Video sharing and collaboration
- [ ] Mobile apps (iOS/Android)
- [ ] Live streaming support

## Security Considerations

- S3 buckets use encryption at rest
- API Gateway with authentication
- Lambda functions with minimal IAM permissions
- No credentials in code (use AWS Secrets Manager)
- HTTPS only for all endpoints

## Performance Optimization

- S3 Transfer Acceleration for uploads
- CloudFront CDN for video delivery
- Lambda provisioned concurrency for ML inference
- Batch processing for non-real-time analysis
- Progressive video encoding for streaming

## Monitoring and Observability

- CloudWatch Logs for all services
- CloudWatch Metrics for performance tracking
- X-Ray tracing for distributed requests
- Cost monitoring with AWS Cost Explorer
- Alert setup for error rates and latency

## Contributing

This is a monorepo. When contributing:
1. Make changes in the appropriate package
2. Run tests locally before committing
3. Update documentation if needed
4. Follow existing code style and patterns
