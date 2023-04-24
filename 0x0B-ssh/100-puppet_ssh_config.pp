#Using Puppet to make changes.

$fileContent = inline_epp("
PasswordAuthentication no
IdentityFile ~/.ssh/school
")

file {'/etc/ssh/ssh_config':
  ensure  => present,
  content => $fileContent,
}
