# Create a file
file { '/tmp/school':
  ensure  => present,
  content => 'I lobe Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
