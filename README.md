# Sports Tracker

A sports tracking application like Veo or Trace using dual iPhone cameras in a 3D printed holder. This app provides video stitching, automatic ball/player tracking, and video storage capabilities.

## Architecture

This is a monorepo containing multiple microservices managed as a single repository:

- **Infrastructure** (`packages/infra`): AWS CDK infrastructure as code
- **Frontend** (`packages/frontend`): SvelteKit web application
- **ML Ball Tracking** (`packages/ml-ball-tracking`): PyTorch-based machine learning service for ball detection and tracking

## Getting Started

### Prerequisites

- Node.js 20+ and npm
- Python 3.12+
- AWS CLI (for deployment)
- AWS CDK CLI: `npm install -g aws-cdk`

### Installation

```bash
# Install all dependencies
npm install

# Install dependencies for all workspaces
npm run build:all
```

### Development

```bash
# Run frontend in development mode
npm run dev:frontend

# Train ML model (when data is available)
cd packages/ml-ball-tracking
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/train.py
```

### Deployment

```bash
# Deploy infrastructure to AWS
npm run deploy:infra
```

## Project Structure

```
sports-tracker/
├── packages/
│   ├── infra/              # AWS CDK infrastructure
│   │   ├── src/
│   │   │   └── main.ts     # CDK stack definition
│   │   └── .projenrc.ts    # Projen configuration
│   ├── frontend/           # SvelteKit frontend
│   │   ├── src/
│   │   │   ├── routes/     # SvelteKit routes
│   │   │   └── lib/        # Shared components
│   │   └── package.json
│   └── ml-ball-tracking/   # ML service
│       ├── src/
│       │   ├── model.py    # Model architecture
│       │   └── train.py    # Training script
│       ├── requirements.txt
│       └── README.md
├── .projenrc.ts           # Root projen configuration
└── package.json           # Root package.json with workspaces

```

## Features

### Current
- ✅ Monorepo structure with workspaces
- ✅ AWS CDK infrastructure with S3 video storage
- ✅ SvelteKit frontend application
- ✅ ML model architecture for ball tracking

### Planned
- [ ] Video stitching from dual cameras
- [ ] Real-time ball tracking
- [ ] Player tracking and identification
- [ ] Video upload and storage
- [ ] Video playback and analysis UI
- [ ] CI/CD pipeline with GitHub Actions
- [ ] API Gateway for backend communication
- [ ] Lambda functions for video processing
- [ ] SageMaker endpoint for ML inference

## Technology Stack

- **Frontend**: SvelteKit, TypeScript
- **Infrastructure**: AWS CDK, TypeScript
- **ML**: PyTorch, Python
- **Cloud**: AWS (S3, Lambda, API Gateway, SageMaker)
- **Build Tools**: Projen, npm workspaces

## Contributing

This is a monorepo managed with npm workspaces. Each package has its own README with specific instructions.

## License

Apache-2.0
