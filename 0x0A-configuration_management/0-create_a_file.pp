# File for creating a file using puppet
# The file (School) has permissions 0744, belonging to the user and group

file { '/tmp/school':
  ensure  => file,
  mode    => '0074',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}