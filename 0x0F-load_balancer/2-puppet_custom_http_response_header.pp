# Install Nginx and adds redirection custom error and header

exec { 'update':
    command => '/usr/bin/apt-get update -y',
}

package { 'nginx':
    ensure  => installed,
    require => Exec['update']
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'redirection-301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.google.com permanent;',
}

file_line {'addHeader':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'listen 80 default_server;',
    line    => 'add_header X-Served-By $HOSTNAME;',
    require => Package['nginx'],
}

service {'nginx':
    ensure  => running,
    require => Package['nginx'],
}
