# 2-execute_a_command.pp
# Description: Kills a process named 'killmenow' using the exec resource.

exec { 'killmenow':
  command     => 'pkill killmenow',
  refreshonly => true,
}
