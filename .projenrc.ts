import { typescript, javascript } from 'projen';

const project = new typescript.TypeScriptProject({
  name: 'sports-tracker',
  defaultReleaseBranch: 'main',
  projenrcTs: true,
  packageManager: javascript.NodePackageManager.NPM,

  devDeps: [
    'projen',
  ],

  gitignore: [
    'node_modules/',
    'dist/',
    'lib/',
    '.DS_Store',
    '.env',
    '.env.local',
    'cdk.out/',
    '.svelte-kit/',
    'build/',
    '.venv/',
    '__pycache__/',
    '*.pyc',
    '.pytest_cache/',
    'models/*.pth',
    'models/*.pt',
    'coverage/',
  ],

  scripts: {
    'build:all': 'npm run build --workspaces --if-present',
    'test:all': 'npm run test --workspaces --if-present',
    'deploy:infra': 'npm run deploy --workspace=@sports-tracker/infra',
    'dev:frontend': 'npm run dev --workspace=@sports-tracker/frontend',
  },

  // Don't create sample code since we're building a monorepo
  sampleCode: false,
});

// Add workspaces to package.json for monorepo structure
project.package.addField('workspaces', ['packages/*']);
project.package.addField('private', true);

project.synth();
