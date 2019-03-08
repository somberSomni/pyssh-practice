import os.path
import sys

#Checking IP address file and content validity
def ip_file_valid():

    #Does file exist?
    ip_file = input("\nEnter IP file path and name (Ex: C:\\User\\Document\\test.txt): ")
    if os.path.isfile(ip_file):
        print("\nIP file is valid\n")
    else:
        print("\nFile %s not found\n" % ip_file)
        sys.exit()
 
    #open file of ips
    with open(ip_file, 'r') as f:
        f.seek(0)
        ips = f.readlines()
        #return list of ips
        return ips
