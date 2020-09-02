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
