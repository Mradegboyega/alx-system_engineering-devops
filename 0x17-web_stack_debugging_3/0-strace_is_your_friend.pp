# 0-strace_is_your_friend.pp

# Step 1: Identify the problem using strace

# strace -p <PID of Apache process>

# Step 2: Fix the problem

exec { 'restart_apache':
  command     => '/usr/sbin/service apache2 restart',
  refreshonly => true,
}

# Step 3: Apply the fix

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Exec['restart_apache'],
}
