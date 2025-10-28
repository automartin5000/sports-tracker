import { App, Stack, StackProps, Duration } from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';
import { Construct } from 'constructs';

export class SportsTrackerStack extends Stack {
  constructor(scope: Construct, id: string, props: StackProps = {}) {
    super(scope, id, props);

    // S3 bucket for video storage
    new s3.Bucket(this, 'VideoStorageBucket', {
      bucketName: `sports-tracker-videos-${this.account}`,
      versioned: false,
      encryption: s3.BucketEncryption.S3_MANAGED,
      lifecycleRules: [
        {
          // Move to infrequent access after 30 days
          transitions: [
            {
              storageClass: s3.StorageClass.INFREQUENT_ACCESS,
              transitionAfter: Duration.days(30),
            },
          ],
        },
      ],
    });

    // TODO: Add Lambda functions for video processing
    // TODO: Add API Gateway for frontend communication
    // TODO: Add SageMaker endpoint for ML model inference
  }
}

// for development, use account/region from cdk cli
const devEnv = {
  account: process.env.CDK_DEFAULT_ACCOUNT,
  region: process.env.CDK_DEFAULT_REGION,
};

const app = new App();

new SportsTrackerStack(app, 'sports-tracker-dev', { env: devEnv });
// new SportsTrackerStack(app, 'sports-tracker-prod', { env: prodEnv });

app.synth();