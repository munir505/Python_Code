#!/bin/python
import os

install_java = os.system("sudo yum install -y java")
java_EC = os.WEXITSTATUS(install_java)
wget_EC = 1;
wget_c_EC = 1;

if java_EC == 0:
	install_wget = os.system("sudo yum install -y wget")
	wget_EC = os.WEXITSTATUS(install_wget) 

if wget_EC == 0:
	wget_command = os.system("sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo")
	wget_c_EC = os.WEXITSTATUS(wget_command))

#rpm_command = os.system("sudo yum install -y java")
#java_EC = os.WEXITSTATUS(install_java))
