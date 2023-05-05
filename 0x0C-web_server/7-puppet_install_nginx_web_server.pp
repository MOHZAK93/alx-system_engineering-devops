#!/usr/bin/env bash
# Install and confifure nginx web server using puppet

exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  content => 'Ceci n\'est pas une page',
}

file { '/etc/nginx/sites-available/default':
  content => "
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html;

	error_page 404 /404.html;
	location = /404.html {
		root /var/www/html;
		internal;
	}


	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
}
"
}
exec { 'Restart nginx':
  command => '/usr/sbin/service nginx restart',
}
