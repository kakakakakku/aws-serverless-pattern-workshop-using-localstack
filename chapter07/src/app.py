from rich import print


def lambda_handler(event, context):
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            id = record['dynamodb']['NewImage']['id']['S']
            notify(
                {
                    'message': f'A coupon `{id}` has been added.',
                    'id': id,
                    'title': record['dynamodb']['NewImage']['title']['S'],
                    'expired_at': record['dynamodb']['NewImage']['expired_at']['N'],
                }
            )
        if record['eventName'] == 'REMOVE':
            id = record['dynamodb']['OldImage']['id']['S']
            analyze(
                {
                    'message': f'A coupon `{id}` has been removed.',
                    'id': id,
                    'title': record['dynamodb']['OldImage']['title']['S'],
                    'expired_at': record['dynamodb']['OldImage']['expired_at']['N'],
                }
            )


def notify(payload):
    print(payload)


def analyze(payload):
    print(payload)
