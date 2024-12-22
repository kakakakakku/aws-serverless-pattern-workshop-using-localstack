import os
import uuid

import boto3

OUTPUT_BUCKET_NAME = os.environ['OUTPUT_BUCKET_NAME']

transcribe = boto3.client('transcribe', endpoint_url='http://localhost.localstack.cloud:4566')


def lambda_handler(event, context):
    for record in event['Records']:
        transcribe.start_transcription_job(
            TranscriptionJobName=f'job-{str(uuid.uuid4())}',
            Media={
                'MediaFileUri': f's3://{record['s3']['bucket']['name']}/{record['s3']['object']['key']}',
            },
            LanguageCode='en-US',
            OutputBucketName=OUTPUT_BUCKET_NAME,
        )
