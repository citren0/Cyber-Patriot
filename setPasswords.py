import subprocess
import os
from time import sleep


if not os.geteuid() == 0:
    exit("\nOnly root can run this script\n")


#Stack overflow section

def setPassword(userName:str, password:str):
    p = subprocess.Popen([ "/usr/sbin/chpasswd" ], universal_newlines=True, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate(userName + ":" + password + "\n")
    assert p.wait() == 0
    if stdout or stderr:
        raise Exception("Error encountered changing the password!")


#My section
command = os.popen('awk -F: \'($3>=1000)&&($1!="nobody"){print $1}\' /etc/passwd') #UID should be greater than 1000
userList = command.read().split()
print('What password should be applied? ')
passwrd = input()
print("Do you want to change the password of: \n", passwrd, "\n to ", userList, "?")
choice1 = input()
if not 'y' in choice1.lower():
    exit("Not changing passwords...")

for userInd in userList:
    setPassword(userInd, passwrd)
