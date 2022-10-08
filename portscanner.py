#!/usr/bin/env python #shebang line
import socket 
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True) #clears the commadline

# Ask for input
remoteServer = input("Enter a remote host: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print("-" * 60)
print(f"Please wait, scanning remote host {remoteServerIP}")
print("-" * 60)

timeBeforeScan = datetime.now()
try:
    for port in range(1,6025):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print(f"Port {port}: open")
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

timeAfterScan = datetime.now()
total = timeAfterScan - timeBeforeScan
print(f"Scanning completed in: {total}")
