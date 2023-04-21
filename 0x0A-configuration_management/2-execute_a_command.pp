# Execute a command
exec { 'pkill killmenow':
  path     => '/usr/bin',
  command  => 'pkill killmenow',
  provider => 'pip3',
  returns  => [0, 1]
}
