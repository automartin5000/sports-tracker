# Getting Started with Sports Tracker

This guide will help you set up and run the Sports Tracker monorepo locally.

## Prerequisites

- **Node.js**: v20 or higher
- **npm**: v10 or higher
- **Python**: 3.12 or higher
- **AWS CLI**: For infrastructure deployment (optional for local development)
- **Git**: For version control

## Initial Setup

### 1. Clone the Repository

```bash
git clone https://github.com/automartin5000/sports-tracker.git
cd sports-tracker
```

### 2. Install Dependencies

```bash
# Install all workspace dependencies
npm install
```

This will install dependencies for:
- Root project
- Infrastructure package
- Frontend package
- ML package (Node.js scripts only)

### 3. Build All Packages

```bash
npm run build:all
```

This builds:
- Infrastructure CDK stack
- Frontend SvelteKit application

## Running the Frontend

### Development Mode

```bash
npm run dev:frontend
```

This will start the SvelteKit development server, typically at `http://localhost:5173`.

### Production Build

```bash
cd packages/frontend
npm run build
npm run preview
```

## Working with Infrastructure

### Synthesize CloudFormation Template

```bash
cd packages/infra
npm run synth
```

This generates the CloudFormation template in `cdk.out/`.

### Deploy to AWS

**Prerequisites:**
- AWS credentials configured
- AWS CDK CLI installed: `npm install -g aws-cdk`

```bash
# From the infra package
cd packages/infra
npm run deploy

# Or from root
npm run deploy:infra
```

### Destroy Infrastructure

```bash
cd packages/infra
npm run destroy
```

## ML Model Development

### Setup Python Environment

```bash
cd packages/ml-ball-tracking
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Test the Model

```bash
python src/model.py
```

Expected output:
```
Model created successfully!
Input shape: torch.Size([2, 3, 224, 224])
Presence output shape: torch.Size([2, 1])
Position output shape: torch.Size([2, 2])
```

### Train the Model

When you have training data:

```bash
python src/train.py --data-dir data/ --output-dir models/ --epochs 50
```

## Running Tests

### All Tests

```bash
npm run test:all
```

### Individual Package Tests

```bash
# Infrastructure tests
cd packages/infra
npm test

# Frontend tests (when added)
cd packages/frontend
npm test
```

## Project Structure

```
sports-tracker/
├── packages/
│   ├── infra/              # AWS CDK Infrastructure
│   │   ├── src/main.ts     # Main CDK stack
│   │   └── test/           # Infrastructure tests
│   ├── frontend/           # SvelteKit Web Application
│   │   ├── src/routes/     # Pages and routes
│   │   └── src/lib/        # Components (to be added)
│   └── ml-ball-tracking/   # PyTorch ML Model
│       ├── src/            # Model and training code
│       ├── data/           # Training data (not committed)
│       └── models/         # Trained models (not committed)
├── .projenrc.ts           # Root projen configuration
├── package.json           # Workspace configuration
├── README.md             # Project overview
└── ARCHITECTURE.md       # Architecture documentation
```

## Common Tasks

### Add a New Package

1. Create package directory: `mkdir -p packages/new-package`
2. Initialize with `npm init` or projen
3. The workspace will automatically detect it

### Update Dependencies

```bash
# Update all dependencies
npm update

# Update specific workspace
npm update --workspace=@sports-tracker/frontend
```

### Lint Code

```bash
# Lint root project
npx projen eslint

# Lint infrastructure
cd packages/infra
npm run eslint
```

## Troubleshooting

### Build Failures

1. Ensure all dependencies are installed: `npm install`
2. Clean and rebuild: `rm -rf node_modules && npm install`
3. Check Node.js version: `node --version` (should be v20+)

### AWS Deployment Issues

1. Verify AWS credentials: `aws sts get-caller-identity`
2. Ensure CDK is bootstrapped: `cdk bootstrap`
3. Check AWS region is set

### ML Model Issues

1. Ensure Python virtual environment is activated
2. Verify all dependencies are installed: `pip list`
3. Check PyTorch installation: `python -c "import torch; print(torch.__version__)"`

## Next Steps

1. **Frontend Development**: Add video upload UI and playback
2. **Infrastructure**: Add Lambda functions and API Gateway
3. **ML Model**: Add data loading and training pipeline
4. **Integration**: Connect all components

## Resources

- [SvelteKit Documentation](https://kit.svelte.dev/)
- [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [Projen Documentation](https://projen.io/)

## Getting Help

- Check the [ARCHITECTURE.md](./ARCHITECTURE.md) for system design
- Review individual package READMEs
- Open an issue on GitHub for bugs or questions
