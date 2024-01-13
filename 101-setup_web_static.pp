#!/usr/bin/puppet apply
# Puppet script to set up web servers for deployment

package { 'nginx':
  ensure => 'installed',
}

# Creating the directories
file { ['/data', '/data/web_static', '/data/web_static/releases',
        '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create fake HTML file
file { '/data/web_static/releases/test/index.html':
  content => '<html>
    <head>
    </head>
    <body>
      Holberton School
    </body>
  </html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create personalized 301 page
file { '/data/web_static/releases/test/redirect_me':
  content => 'https://www.holbertonschool.com',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create personalized 404 page
file { '/data/web_static/releases/test/404.html':
  content => "Ceci n'est pas une page",
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create nginx configuration
file { '/etc/nginx/sites-enabled/default':
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;

    root /data/web_static/current;
    index index.html index.htm index.nginx-debian.html;

    location /hbnb_static {
        alias /data/web_static/current;
    }

    location / {
	try_files $uri $uri =404;
        add_header X-Served-By $hostname;
        proxy_set_header Host $host;
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
  }",
  notify => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure    => 'running',
  enable    => 'true',
  subscribe => File['/etc/nginx/sites-enabled/default'],
}
