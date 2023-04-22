# Using Puppet, create a manifest that kills a process, killmenow.

exec {'pkill killmenow':
  onlyif   => 'test `pgrep killmenow`',
  provider => 'shell',
  }
