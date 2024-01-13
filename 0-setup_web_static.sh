#!/usr/bin/env bash
# script that sets up web servers for deployment of web_static

# install Nginx if not installed
sudo apt-get -y update
sudo apt-get -y install nginx

# create necessary folders
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create or recreate the symbolic link
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownsership to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# set ownership to ubuntu
sudo chown -R ubuntu:ubuntu /data/web_static/releases/test/

# Personalized 301 page
echo "https://www.holbertonschool.com" | sudo tee /data/web_static/releases/test/redirect_me

# Personalized 404 page
echo "Ceci n'est pas une page" | sudo tee /data/web_static/releases/test/404.html

# sudo cp /etc/nginx/sites-enabled/default /etc/nginx/sites-enabled/default.bak

# Update Nginx configuration
config_content="
server {
	listen 80;
	listen [::]:80 default_server;
	server_name _;

	root /data/web_static/current;
	index index.html index.htm 0-index.html index.nginx-debian.html;

	location /hbnb_static {
		alias /data/web_static/current;
	}

	location / {
		add_header X-Served-By \$hostname;
		proxy_set_header Host \$host;
		proxy_pass http://127.0.0.1:5000;
	}

	error_page 404 /404.html;
	location /404 {
		internal;
		alias /data/web_static/releases/test/404.html;
	}

	location /redirect_me {
		rewrite ^/redirect_me http://www.holbertonschool.com redirect;
	}

	error_page 500 502 503 504 /50x.html;
	location /50x.html {
		alias /data/web_static/releases/test;
	}
}
"
echo "$config_content" | sudo tee /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart
