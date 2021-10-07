# Script increases the nginx user limit

file {'fix-nginx':
  ensure  => present,
  path    => '/etc/default/nginx',
  content => 'ULIMIT="-n 4096"'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
