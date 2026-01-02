import json
import boto3
from datetime import datetime, timezone, timedelta

volume_id = "vol-0903729e6e2b8b96a"
# uncomment the below line and comment the retention_days line to use minutes as retention time 
retention_time = 1 # in minutes
# retention_days = 30
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # TODO implement

    #1 Create EBS Snapshot
    snapshot_response = ec2.create_snapshot(
        VolumeId=volume_id,
        Description=f"Automated snapshot created by Lambda function"
    )

    snapshot_id = snapshot_response['SnapshotId']
    print(f"Created snapshot: {snapshot_id} for volume: {volume_id}")

    #2 Calculating the cleanup date/time
    # uncomment the below line and comment the retention_days line to use minutes as retention time
    cleanup_time = datetime.now(timezone.utc) - timedelta(minutes=retention_time)
    #cleanup_date = datetime.now(timezone.utc) - timedelta(days=retention_days)

    #3 List the snapshots of the specified volume
    snapshots = ec2.describe_snapshots(
        Filters=[
            {
                'Name': 'volume-id',
                'Values': [volume_id]
            }
        ],
        OwnerIds=['self']
    )['Snapshots']

    print(f"Found {len(snapshots)} snapshots for volume: {volume_id}")

    #4 Delete snapshots older than retention period
    for snapshot in snapshots:
        start_time = snapshot['StartTime']
        snapshot_id = snapshot['SnapshotId']
        if start_time < cleanup_date:
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted snapshot: {snapshot_id}")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
