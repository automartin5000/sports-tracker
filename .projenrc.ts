import { typescript } from 'projen';

const project = new typescript.TypeScriptProject({
  name: 'sports-tracker',
  defaultReleaseBranch: 'main',
  projenrcTs: true,
  packageManager: typescript.NodePackageManager.NPM,

  // Monorepo configuration
  workspaces: [
    'packages/*',
  ],

  devDeps: [
    'projen',
  ],

  gitignore: [
    '*.js',
    '*.d.ts',
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
    '!.projenrc.ts',
  ],

  scripts: {
    'build:all': 'npm run build --workspaces --if-present',
    'test:all': 'npm run test --workspaces --if-present',
    'deploy:infra': 'npm run deploy --workspace=@sports-tracker/infra',
    'dev:frontend': 'npm run dev --workspace=@sports-tracker/frontend',
  },
});

project.synth();
