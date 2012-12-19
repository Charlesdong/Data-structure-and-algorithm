#encoding: utf-8

import subprocess

Ping = subprocess.Popen(args='ls', shell=True, stdout=subprocess.PIPE)
#Ping.wait() #等待子进程结束
#print Ping.stdout.read()
PingOut, PingErr = Ping.communicate()
#print "Ping id is:", Ping.pid
#print Ping.returncode
print "pingOut:", PingOut, PingErr
