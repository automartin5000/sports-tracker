import { awscdk, javascript } from 'projen';
const project = new awscdk.AwsCdkTypeScriptApp({
  cdkVersion: '2.1.0',
  defaultReleaseBranch: 'main',
  name: '@sports-tracker/infra',
  projenrcTs: true,
  packageManager: javascript.NodePackageManager.NPM,

  // CDK configuration
  appEntrypoint: 'main.ts',
  cdkVersionPinning: false,

  deps: [
    'dotenv',
  ],

  devDeps: [
    '@types/node',
  ],

  tsconfig: {
    compilerOptions: {
      types: ['node', 'jest'],
      isolatedModules: true,
    },
  },

  gitignore: [
    'cdk.out/',
    '.env',
  ],
});
project.synth();