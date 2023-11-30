#!/bin/bash -ex
PMGR=apt
$PMGR update -y 
# https://tecadmin.net/how-to-install-mysql-8-on-amazon-linux-2/
#sudo $PMGR install https://dev.mysql.com/get/mysql80-community-release-el7-5.noarch.rpm
$PMGR install -y git
#https://linux.how2shout.com/installing-mariadb-on-amazon-linux-2023/
sudo yum install mariadb105-server # läuft nur unter aws, nicht lokal !
#$PMGR install mysql-server -y
sudo systemctl start mysqld
sudo systemctl enable mysqld
$PMGR install python3 python3-pip -y
# download zipfile and unzip and cd in the new folder
wget https://todolist-bucket-1.s3.eu-central-1.amazonaws.com/todo-app.zip
unzip todo-app.zip
# cd todo-app
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
sudo mysql -u root -p < sql-scripts/01-prepare-db.sql
cd src
uvicorn main:app --reload
