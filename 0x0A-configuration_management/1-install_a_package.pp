# 1-install_a_package.pp
# Description: Installs Flask package from pip3.

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
