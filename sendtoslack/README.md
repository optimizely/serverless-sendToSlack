# SendToSlack

# WARNING

Serverless uses AWS Cloudformation to manage the services contained in serverless.yml.  
*YOU MUST NOT EDIT THESE VIA ANY METHOD OTHER THAN AS DESCRIBED HERE* or Cloudformation will no longer properly manage them.

## Description
This is a AWS Lambda function, deployed with Serverless. The function is designed to monitor a given SNS topic and push to a Slack web integration hook. The SNS topic name is "sendToSlack", and any functions or applications with the correct access could push a message to the topic. These messages will be treated as plain-text strings.

## Purpose
We wanted to have a central place to send messages from.

## Lambda Configuration
The script is controlled through environment variables passed to Lambda at runtime. These can be set in a YAML file for each environment deployed through this process.

Key | Value
---|---
SLACK_HOOK_URL   | Slack webhook integration URL
SLACK_CHANNEL    | Slack channel to report to

## Environment File
You can control environment specific values through the env.yml file. `default_env` can be overridden by placing duplicate keys in a environment code block later in the file. The blocks can be named whatever you like, just use the new name as the `--stage` argument in the deploy command below.

## Run Serverless

See: ../README.md for information on setting up Serverless.

To create or update the resources contained here, just run:

`serverless deploy --stage devops`

Be sure to update the stage to the appropriate one for your currently logged in session!
