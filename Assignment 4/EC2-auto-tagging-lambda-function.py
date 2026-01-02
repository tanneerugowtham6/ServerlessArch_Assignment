import json
import boto3
from datetime import datetime

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # TODO implement
    #1 Get Instance ID from the event
    instance_id = event['detail']['instance-id']

    #2 Get current date
    launch_date = datetime.now().strftime("%Y-%m-%d")

    #3 Create tags for the instance
    ec2.create_tags(
        Resources=[instance_id],
        Tags=[
            {
                'Key': 'LaunchDate',
                'Value': launch_date
            },
            {
                'Key': 'AutoTagged',
                'Value': 'True'
            }
        ]
    )

    print(f"Tags added to instance: {instance_id}")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
