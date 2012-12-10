#encoding: utf-8

import subprocess

Ping = subprocess.Popen(args='ping -c 4 sina.com.cn', shell=True, stdout=subprocess.PIPE)
Ping.wait() #等待子进程结束
print Ping.stdout.read()
print "Ping id is:", Ping.pid
print Ping.returncode
