from c import *
import boto3
import time
import os
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
    
# create_resp = ec2.create_instances(
#     ImageId=ami_id,
#     InstanceType='t3.micro',
#     MaxCount=1,
#     MinCount=1,
#     SecurityGroupIds=[
#         security_group_id
#     ],
#     TagSpecifications=[
#         {
#             'ResourceType': 'instance',
#             'Tags': [
#                 {
#                     'Key': 'Name',
#                     'Value': 'hk-gfw'
#                 },
#             ]yes

#         },
#     ],
#     KeyName='kh'
# )
# instance_id = create_resp[0].id
# wait_running(client,instance_id)
# ip = get_ip(client,instance_id)
ip='18.163.119.25'
print(ip)
print(key_path)
time.sleep(10)# make sure instance can be connected via ssh
subprocess.run(["scp", "-i", key_path, code_path+"/shadowsocks.json", "ec2-user@"+ip+":/home/ec2-user/shadowsocks.json"])
subprocess.run(["scp", "-i", key_path, code_path+"/startss.sh", "ec2-user@"+ip+":/home/ec2-user/startss.sh"])

cmd = 'ssh -i '+key_path+' ec2-user@'+ip+' "sudo sh /home/ec2-user/startss.sh"'
os.system(cmd)
print(ip)