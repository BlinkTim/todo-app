#!/bin/bash -ex
PMGR=yum
$PMGR update -y 
# https://tecadmin.net/how-to-install-mysql-8-on-amazon-linux-2/
#sudo $PMGR install https://dev.mysql.com/get/mysql80-community-release-el7-5.noarch.rpm
$PMGR install -y git
#https://linux.how2shout.com/installing-mariadb-on-amazon-linux-2023/
sudo yum install -y mariadb105-server # läuft nur unter aws, nicht lokal !
#$PMGR install mysql-server -y
sudo systemctl start mariadb
sudo systemctl enable mariadb
$PMGR install python3 python3-pip -y
# download zipfile and unzip and cd in the new folder
#wget https://todolist-bucket-1.s3.eu-central-1.amazonaws.com/todo-app.zip
#unzip todo-app.zip
git clone https://github.com/BlinkTim/todo-app.git
cd todo-app
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
sudo mysql -u root -p < sql-scripts/01-prepare-db.sql
cd src
uvicorn main:app --reload --port 8000 --host 0.0.0.0
