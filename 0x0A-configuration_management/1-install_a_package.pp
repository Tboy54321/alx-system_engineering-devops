exec { '1-install_a_package':
  command => 'usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/bin/bin:$PATH',
  unless  => '/usr/bin/pip3 show Flask | grep Version | grep 2.1.0',
}
