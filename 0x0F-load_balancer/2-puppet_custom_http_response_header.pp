# 2-puppet_custom_http_response_header.pp
# Puppet manifest to configure Nginx to add a custom HTTP header
class nginx_custom_header {

  # Ensure nginx is installed
  package { 'nginx':
    ensure => installed,
  }

  # Ensure nginx service is running
  service { 'nginx':
    ensure     => running,
    enable     => true,
    require    => Package['nginx'],
    subscribe  => File['/etc/nginx/conf.d/custom_http_header.conf'],
  }

  # Define the custom header configuration
  file { '/etc/nginx/conf.d/custom_http_header.conf':
    ensure  => file,
    content => template('nginx/custom_http_header.conf.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }
}

# Apply the nginx_custom_header class
include nginx_custom_header
