# CdkGoat - Vulnerable AWS CDK Infrastructure

[![Maintained by Bridgecrew.io](https://img.shields.io/badge/maintained%20by-bridgecrew.io-blueviolet)](https://bridgecrew.io/?utm_source=github&utm_medium=organic_oss&utm_campaign=cdkgoat)
[![slack-community](https://slack.bridgecrew.io/badge.svg)](https://slack.bridgecrew.io/?utm_source=github&utm_medium=organic_oss&utm_campaign=cdkgoat)

CdkGoat is Bridgecrew's "Vulnerable by Design" AWS CDK repository.
CdkGoat is a learning and training project that demonstrates how common configuration errors can find their way into production cloud environments.

It also shows how Bridgecrew can be used with the AWS CDK to provide CloudFormation template vulnerability scanning at build time, even though no CloudFormation templates exist in the source repository.

## Table of Contents


## Introduction

CdkGoat was built to enable DevSecOps design and implement a sustainable misconfiguration prevention strategy. It can be used to test a policy-as-code framework like [Bridgecrew](https://bridgecrew.io/?utm_source=github&utm_medium=organic_oss&utm_campaign=cdkgoat) & [Checkov](https://github.com/bridgecrewio/checkov/), inline-linters, or other code scanning methods executed at build / deploy time.

CdkGoat follows the tradition of existing *Goat projects that provide a baseline training ground to practice implementing secure development best practices for cloud infrastructure.

## Important notes

* **Where to get help:** the [Bridgecrew Community Slack](https://codified-security.herokuapp.com/)

Before you proceed please take a not of these warning:
> :warning: CdkGoat creates intentionally vulnerable AWS resources into your account. **DO NOT deploy CdkGoat in a production environment or alongside any sensitive AWS resources.**

## Requirements

This project uses the following software versions, but older versions should generally work.

* Python 3.8.4 with virtualenv
* Node 14.5.0
* NPM 6.14.5
* AWS CLI v2, configured with credentials

To prevent vulnerable infrastructure from arriving to production see: [checkov](https://github.com/bridgecrewio/checkov/), the open source static analysis tool for infrastructure as code.

## Getting started

### Installation
Clone this repository. Then run the following commands:

```bash
npm install -g aws-cdk
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

### Generate and scan a template

Run the following commands to generate a CloudFormation template and scan it with the Bridgecrew CLI:

```bash
cdk synth
bridgecrew -f cdk.out/cdkgoat.template.json
```

### Deploy a CloudFormation stack

Run the following command to deploy the infrastructure into your AWS account. **Warning: This will create vulnerable resources. Deploy with care into a non-prod account, and consider deleting the stack each time you finish your work.** The best use of this capability is to compare these results to a [runtime scanner](https://bridgecrew.cloud).

```bash
cdk deploy
```

Note that you will probably need to change some resource names, especially S3 bucket names, to be unique.

### Destroy a CloudFormation stack

Run the following command to destroy the stack and its resources. You can also delete the stack from the AWS Console.

```bash
cdk destroy
```

## Bridgecrew's IaC herd of goats

* [CfnGoat](https://github.com/bridgecrewio/cfngoat) - Vulnerable by design Cloudformation template
* [TerraGoat](https://github.com/bridgecrewio/terragoat) - Vulnerable by design Terraform stack
* [CDKGoat](https://github.com/bridgecrewio/cdkgoat) - Vulnerable by design CDK application

## Contributing

Contribution is welcomed!

We would love to hear about more ideas on how to find vulnerable infrastructure-as-code design patterns.

## Support

[Bridgecrew](https://bridge.dev/2WBms5Q) builds and maintains CdkGoat to encourage the adoption of policy-as-code.

If you need direct support you can contact us at [info@bridgecrew.io](mailto:info@bridgecrew.io).

## Existing misconfigs (Auto-Generated)
|    | check_id   | file                          | resource                            | check_name                                                        | guideline                                                           |
|----|------------|-------------------------------|-------------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------------|
|  0 | CKV_AWS_57 | cdk.out/cdkgoat.template.json | AWS::S3::Bucket.mycdkbucketC801BBDD | Ensure the S3 bucket does not allow WRITE permissions to everyone | https://docs.bridgecrew.io/docs/s3_2-acl-write-permissions-everyone |
|  1 | CKV_AWS_54 | cdk.out/cdkgoat.template.json | AWS::S3::Bucket.mycdkbucketC801BBDD | Ensure S3 bucket has block public policy enabled                  | https://docs.bridgecrew.io/docs/bc_aws_s3_20                        |
|  2 | CKV_AWS_55 | cdk.out/cdkgoat.template.json | AWS::S3::Bucket.mycdkbucketC801BBDD | Ensure S3 bucket has ignore public ACLs enabled                   | https://docs.bridgecrew.io/docs/bc_aws_s3_21                        |
|  3 | CKV_AWS_20 | cdk.out/cdkgoat.template.json | AWS::S3::Bucket.mycdkbucketC801BBDD | Ensure the S3 bucket does not allow READ permissions to everyone  | https://docs.bridgecrew.io/docs/s3_1-acl-read-permissions-everyone  |
|  4 | CKV_AWS_21 | cdk.out/cdkgoat.template.json | AWS::S3::Bucket.mycdkbucketC801BBDD | Ensure the S3 bucket has versioning enabled                       | https://docs.bridgecrew.io/docs/s3_16-enable-versioning             |
|  5 | CKV_AWS_56 | cdk.out/cdkgoat.template.json | AWS::S3::Bucket.mycdkbucketC801BBDD | Ensure S3 bucket has 'restrict_public_bucket' enabled             | https://docs.bridgecrew.io/docs/bc_aws_s3_22                        |
|  6 | CKV_AWS_18 | cdk.out/cdkgoat.template.json | AWS::S3::Bucket.mycdkbucketC801BBDD | Ensure the S3 bucket has access logging enabled                   | https://docs.bridgecrew.io/docs/s3_13-enable-logging                |
|  7 | CKV_AWS_53 | cdk.out/cdkgoat.template.json | AWS::S3::Bucket.mycdkbucketC801BBDD | Ensure S3 bucket has block public ACLS enabled                    | https://docs.bridgecrew.io/docs/bc_aws_s3_19                        |
|  8 | CKV_AWS_19 | cdk.out/cdkgoat.template.json | AWS::S3::Bucket.mycdkbucketC801BBDD | Ensure the S3 bucket has server-side-encryption enabled           | https://docs.bridgecrew.io/docs/s3_14-data-encrypted-at-rest        |
|  9 | CKV_AWS_3  | cdk.out/cdkgoat.template.json | AWS::EC2::Volume.vol100D23AE3       | Ensure all data stored in the EBS is securely encrypted           | https://docs.bridgecrew.io/docs/general_3-encrypt-eps-volume        |
| 10 | CKV_AWS_24 | cdk.out/cdkgoat.template.json | AWS::EC2::SecurityGroup.sg15CEFF4E3 | Ensure no security groups allow ingress from 0.0.0.0:0 to port 22 | https://docs.bridgecrew.io/docs/networking_1-port-security          |
| 11 | CKV_AWS_7  | cdk.out/cdkgoat.template.json | AWS::KMS::Key.kms1045C8EFE          | Ensure rotation for customer created CMKs is enabled              | https://docs.bridgecrew.io/docs/logging_8                           |
| 12 | CKV_AWS_17 | cdk.out/cdkgoat.template.json | AWS::RDS::DBInstance.rds1E1302D19   | Ensure all data stored in the RDS bucket is not public accessible | https://docs.bridgecrew.io/docs/public_2                            |
| 13 | CKV_AWS_16 | cdk.out/cdkgoat.template.json | AWS::RDS::DBInstance.rds1E1302D19   | Ensure all data stored in the RDS is securely encrypted at rest   | https://docs.bridgecrew.io/docs/general_4                           |


---


