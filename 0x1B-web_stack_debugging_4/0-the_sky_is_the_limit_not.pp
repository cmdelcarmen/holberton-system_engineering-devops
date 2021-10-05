# Script allows multiple petitons at the same time in a nginx server

exec{'sed':
  path    => '/bin',
  command => "sed -i '5s/.*/ULIMIT=\"-n 2000\"/' /etc/default/nginx"
}
