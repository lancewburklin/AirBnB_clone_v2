#!/usr/bin/env bash
# This is for setting up a web server on nginx
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo "This is some content" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
cd /etc/nginx/sites-available
sudo sed -i "45a \\\n" default
sudo sed -i "46a \\\tlocation /hbnb_static {\\n" default
sudo sed -i "47a \\\t\\talias /data/web_static/current/;\\n\\t}\\n" default
service nginx restart
