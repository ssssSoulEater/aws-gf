you know how does it works
1. configure aws:
create a free tier personal aws account
create a key pair
create security group with 8000 -10000 tcp open, name it as, get the security group id 
2. rename c_temp.py to c.py
and input the configuration

3. pip3 install boto3
4. start a ss server:
python3 p.py
5. stop and ternimate the resource, this will ternmiate all instance with AMI id, so be careful
python3 t.py

TODO
1. provide docker env for env setup.
2. create security group to improve the automation rate. 
