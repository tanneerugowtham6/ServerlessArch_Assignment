import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # TODO implement

    # Get instance with tag Action=Auto-Stop
    stop_response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Action',
                'Values': [
                    'Auto-Stop',
                ]
            },
        ]
    )

    stop_instances = []
    for reservation in stop_response['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'running': # Get the Instance ID of only stopped instances
                stop_instances.append(instance['InstanceId'])

    for stop_instance in stop_instances:
        ec2.stop_instances(InstanceIds=[stop_instance])
        print("Stopping instance: " + stop_instance)

    # Get instance with tag Action=Auto-Start
    start_response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Action',
                'Values': [
                    'Auto-Start',
                ]
            },
        ]
    )

    start_instances = []
    for reservation in start_response['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'stopped': # Get the Instance ID of only stopped instances
                start_instances.append(instance['InstanceId'])

    for start_instance in start_instances:
        ec2.start_instances(InstanceIds=[start_instance])
        print("Starting instance: " + start_instance)

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda executed Successfully!')
    }
