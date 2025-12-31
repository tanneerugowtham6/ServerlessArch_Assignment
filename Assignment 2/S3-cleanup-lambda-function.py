import json
import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')
cleanup_date = datetime.now(timezone.utc) - timedelta(days=30)

def lambda_handler(event, context):
    # TODO implement

    bucket_name = 'gowtham-s3-bucket-001'
    s3_response = s3.list_objects_v2(Bucket=bucket_name)

    for object in s3_response['Contents']:
        last_modified = object['LastModified']
        if last_modified < cleanup_date:
            s3.delete_object(
                Bucket=bucket_name,
                Key=object['Key']
            )
            print(f"Deleted object: {object['Key']}")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }