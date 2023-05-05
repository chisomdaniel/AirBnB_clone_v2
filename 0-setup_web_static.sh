#!/usr/bin/env bash
# Setting up a web server
# make sure you run the file with sudo priviledges
# shellcheck disable=SC2154
# shellcheck disable=SC2230

check=$(which nginx | grep '/usr/bin/nginx')
if [ -z "$check" ]; then
	# update and upgrade the shell
	apt update -y && sudo apt upgrade -y
	
	# install nginx
	apt install nginx -y
fi


# adjust the fire wall
ufw allow 'Nginx HTTP'

# create the files if they don't exist
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

check2=$(grep 'location /hbnb_static/' /etc/nginx/sites-available/default)
if [ -z "$check2" ]; then
	string="server_name _;\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\ttry_files $uri $uri/ =404;\n}\n"
	sed -i "s|server_name _;|$string|" /etc/nginx/sites-available/default
fi

#chmod -R 755 /data

# restart nginx
service nginx restart

exit 0
