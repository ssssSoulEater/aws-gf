from c import *
import boto3
import time
import subprocess
ec2 = boto3.resource('ec2', region_name=aws_region,aws_access_key_id=aws_id,aws_secret_access_key=aws_key)

client = boto3.client('ec2', region_name=aws_region,aws_access_key_id=aws_id,aws_secret_access_key=aws_key)


def get_instance_status(client, id):
    resp = client.describe_instances(
        Filters=[
            {
                'Name': 'instance-id',
                'Values': [
                    id,
                ]
            },
        ],
    )
    return resp

def get_status(client, id):
    resp = get_instance_status(client, id)
    return resp['Reservations'][0]['Instances'][0]['State']['Name']

def wait_running(client, id):
    while True:
        status = get_status(client, id)
        if status == "running":
            return
        time.sleep(5)
        print("wait for running")
        

def get_ip(client, id):
    resp = get_instance_status(client, id)
    return resp['Reservations'][0]['Instances'][0]['PublicIpAddress']
    
create_resp = ec2.create_instances(
    ImageId=ami_id,
    InstanceType='t3.micro',
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        'sg-05c65aa0f3fb01532'
    ],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'hk-gfw'
                },
            ]
        },
    ],
    KeyName='kh'
)
# print(create_resp)
instance_id = create_resp[0].id
# print(instance_id)
# instance_id = 'i-0fe9c15cf312a87e6'
# get_instance_status(client,instance_id)
# print(get_status(client,instance_id))
wait_running(client,instance_id)
ip = get_ip(client,instance_id)
print(ip)
# subprocess.run(["scp", "-l"])