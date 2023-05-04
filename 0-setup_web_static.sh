#!/usr/bin/env bash
# Setting up a web server
# make sure you run the file with sudo priviledges

# update and upgrade the shell
apt update -y && sudo apt upgrade -y

# install nginx
apt install nginx -y

# adjust the fire wall
ufw allow 'Nginx HTTP'


if [ ! -d "/data/web_static/releases/test/" ]; then
	mkdir -p /data/web_static/releases/test/
fi

if [ ! -d "/data/web_static/shared" ]; then
	mkdir -p /data/web_static/shared/
fi

echo "Test file #01" > ~/new_test001
cp ~/new_test001 /data/web_static/releases/test/index.html
rm ~/new_test001

if [ ! -d "/data/web_static/current" ]; then
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current
else
	rm -rf /data/web_static/current
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current
fi

chown -R ubuntu:ubuntu /data/
#sudo chmod -R 755 /var/www



# restart nginx
service nginx restart
