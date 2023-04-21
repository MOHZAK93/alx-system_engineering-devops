# Install a package
file { 'flask':
  ensure  => '2.1.0',
  content => 'pip3'
}
