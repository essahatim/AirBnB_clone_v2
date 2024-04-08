#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

sudo apt-get update
sudo apt-get install -y nginx

web_static_root="/data/web_static"
test_release_dir="$web_static_root/releases/test"
shared_dir="$web_static_root/shared"

sudo mkdir -p "$test_release_dir" "$shared_dir"
sudo echo "Holberton School" > "$test_release_dir/index.html"
sudo ln -sf "$test_release_dir" "$web_static_root/current"
sudo chown -R ubuntu:ubuntu "$web_static_root"
sudo sed -i "/^}$/i \\\tlocation /hbnb_static {\n\t\talias $web_static_root/current;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
