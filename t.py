from c import *
import boto3

ec2 = boto3.client('ec2', region_name=aws_region,aws_access_key_id=aws_id,aws_secret_access_key=aws_key)
resp = ec2.describe_instances(
    Filters=[
        {
            'Name': 'image-id',
            'Values': [
                ami_id,
            ]
        },
    ],
)
# print(len(resp['Reservations'][0]['Instances']))
for item in resp['Reservations'][0]['Instances']:
    print(item['InstanceId'])
    response = ec2.terminate_instances(
        InstanceIds=[
            item['InstanceId'],
        ],
    )
    print(response)