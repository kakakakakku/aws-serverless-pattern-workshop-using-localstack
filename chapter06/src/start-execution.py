import json
import os

import boto3

stepfunctions = boto3.client('stepfunctions', endpoint_url='http://localhost.localstack.cloud:4566')


def lambda_handler(event, context):
    stepfunctions.start_execution(
        stateMachineArn=os.environ['STATE_MACHINE_ARN'],
        input=json.dumps(event),
    )
