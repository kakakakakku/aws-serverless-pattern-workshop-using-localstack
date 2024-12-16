import json

import boto3

s3 = boto3.client('s3', endpoint_url='http://localhost.localstack.cloud:4566')


def lambda_handler(event, context):
    body = json.loads(event['body'])
    filename = body['filename']

    url = s3.generate_presigned_url(
        ClientMethod='put_object',
        Params={
            'Bucket': 'chapter05-upload-bucket',
            'Key': filename,
        },
        ExpiresIn=300,
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'url': url}),
    }
