# creates a file in /tmp

file { '/tmp/schcool':
  ensure   => file,
  checksum => 'md5',
  content  => 'I love Puppet',
  mode     => '0744',
  owner    => 'www-data',
  group    => 'www-data',
}
