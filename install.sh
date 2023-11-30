#!/bin/bash -ex
PMGR=apt
$PMGR update -y 
$PMGR install mysql-server -y
$PMGR install python3 python3-pip -y
# download zipfile and unzip and cd in the new folder
wget https://todolist-bucket-1.s3.eu-central-1.amazonaws.com/todo-app.zip
unzip todo-app.zip
# cd todo-app
python3 -m venv env
pip install -r requirements.txt
sudo mysql -u root -p < sql-scripts/01-prepare-db.sql
cd src
uvicorn main:app --reload
