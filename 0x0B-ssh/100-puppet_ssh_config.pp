#!/usr/bin/env bash
# using puppet to make changes to our configuration file
file { 'etc/ssh_config':
	ensure => present,
content =>"
	SSH client configuaration
	host*
	Identity ~/.ssh/school
	PasswordAuthentication no"
}
