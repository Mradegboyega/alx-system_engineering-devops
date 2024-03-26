# Filename: nginx_setup.pp

# Ensure the Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running and enabled to start at boot
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => Package['nginx'],
}

# Define the root HTML file content
file { '/var/www/html/index.html':
  ensure  => file,
  content => '<html><body>Hello World!</body></html>',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define the Nginx server configuration for redirect
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('modulename/nginx_default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}
