import os

import boto3
from PIL import Image

s3 = boto3.client('s3', endpoint_url='http://localhost.localstack.cloud:4566')


def lambda_handler(event, context):
    for record in event['Records']:
        upload_key = record['s3']['object']['key']
        upload_file = f'/tmp/{os.path.basename(upload_key)}'

        s3.download_file(
            Bucket='chapter06-upload-bucket',
            Key=upload_key,
            Filename=upload_file,
        )

        img = Image.open(upload_file)
        rotated_img = img.rotate(180)
        processing_file = f'/tmp/rotated-{os.path.basename(upload_key)}'
        rotated_img.save(processing_file)

        s3.upload_file(
            Bucket='chapter06-processing-bucket',
            Key=f'rotated-{os.path.basename(upload_key)}',
            Filename=processing_file,
        )
