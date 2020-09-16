sudo yum install -y python-setuptools
sudo easy_install pip
sudo pip install shadowsocks
sudo ssserver -c /home/ec2-user/shadowsocks.json -d start