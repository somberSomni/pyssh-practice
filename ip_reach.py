#Checking if IP can be reached
import sys
import subprocess

def ip_reach(ips):
    for ip in ips:
        ip = ip.rstrip("\n")

        pinged = subprocess.call('ping %s /n 2' % ip, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if pinged == 0:
            print("%s is open\n" % ip)
        else:
            print("%s is not available. Check connection" % ip)
            sys.exit()

    