import os 
# rename it to c.py to privde configuration to code
aws_id='' # your aws access id
aws_key='' # your aws access key
aws_region='ap-east-1' # aws hongkong region, if in mainland china, this is fast
ami_id='ami-6cf0b31d' #amazon linux ami
key_path='' # aws key pair, need to chmod to 500
security_group_id='' #security group id, maybe name is a better option here, but I don't want to change
code_path=os.path.dirname(os.path.abspath(__file__))
