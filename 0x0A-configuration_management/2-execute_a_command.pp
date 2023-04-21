# Execute a command
exec { 'pkill killmenow':
  path     => '/usr/bin',
  command  => 'pkill killmenow',
  provider => 'shell',
  returns  => [0, 1]
}
