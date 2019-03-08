import paramiko
import os.path
import time
import sys
import re

#Checking username/password
user_file = input("\n Enter user file path and name (Ex: C:\\User\\Document\\test.txt): ")

if os.path.isfile(user_file):
    print("\nUser file found!\n")
else:
    print("\nFile %s doesn't exist. Check your file path" % user_file)
    sys.exit()

cmd_file = input("\n Enter commands file path and name (Ex: C:\\User\\Document\\test.txt): ")

if os.path.isfile(cmd_file):
    print("\nCommand file found!\n")
else:
    print("\nFile %s doesn't exist. Check your file path" % user_file)
    sys.exit()

def ssh_connection(ip):

    global user_file
    global cmd_file

    try:
        #define ssh parameters
        selected_user_file = open(user_file, 'r')

        selected_user_file.seek(0)
        content = selected_user_file.readlines()[0].split(',')

        username = content[0].rstrip("\n")
        password = content[1].rstrip("\n")
        print("username %s, password: %s" % (username, password))
        #close user file
        selected_user_file.close()
        #log into device
        session = paramiko.SSHClient()
        
        #for testing purposes, this allows auto-accepting host keys
        #Do not use for production! Default to RejectPolicty
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #connect to device with username and password
        session.connect(ip.rstrip("\n"), username=username, password=password)
        
        #start an interactive shell session on router
        connection = session.invoke_shell()

        #setting terminal length for entire output, disable pagination
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        #enter global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)
        
        selected_cmd_file = open(cmd_file, 'r')

        selected_cmd_file.seek(0)

        for line in selected_cmd_file.readlines():
            connection.send(line + '\n')
            time.sleep(2)
        

        #close cmd file
        selected_cmd_file.close()

        router_output = connection.recv(65535) #bits of data 16bits

        if re.search(b"% Invalid input", router_output):
            print("There was at least one IOS syntax error on device %s \n" % ip)
        else:
            print("Done for device %s \n" % ip)

        #test for eading command output
        print(str(router_output) + "\n")
        
        #close connection
        session.close()
    except paramiko.AuthenticationException:
        print("Invalid username or password. Check username/password file in device configuration\n")
        print("Closing program...")
        sys.exit()