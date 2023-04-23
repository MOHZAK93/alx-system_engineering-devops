# Client configuration file
exec {'configfile':
  command => "echo 'IdentityFile ~/.ssh/school' >> /etc/ssh/ssh_config; echo 'PasswordAuthentication no' >> /etc/ssh/ssh_config",
  path    => ['/usr/bin', '/bin'],
}
