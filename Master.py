import os
from sys import platform

#Perform Checks for OS and UID
elif platform == "win32":
    #Script is not made to run on Windows.
    exit("This script is not made for windows and only for Linux use. Exiting.")
if not os.geteuid() == 0:
	exit("\nOnly root can run this script\n")


def scriptRun():
        commandls = os.popen('ls')
        list = commandls.read().split()
        print(list)

        yorn = input("Would you like to run all the scripts? (Y or N) ")
        if 'y' in yorn.lower():
                print('Running:')
                for currentCom in list:
                        if 'py' in currentCom:
                                command = os.popen('sudo python3 ' + currentCom)
                                command2 = command.read()
                                print(command2)
                        elif 'sh' in currentCom:
                                command = os.popen('sudo bash ' + currentCom)
                                command2 = command.read()
                                print(command2)


def checklist():
        print("Checklist of things to do:")
        print("1. Check unauthorized users.")
        print("2. Check for unauthorized admin accounts.")
        print("3. Delete all media files.")
        print("4. Disable ssh root login.")
        print("5. install the program 'bum' and run to check services.")
        print("6. Check PAM lockout policies per the updated masterlist.")
        print("7. Check password rememberance policies per updated masterlist.")


print("      ::::::::::::::::::::::::::::::::::::::: ::::::::::: :::    ::::   :::::: ")
print("    :+:    :+:   :+:        :+:    :+:    :+: :+:        :+:+:   :+:  :+:   :+: ")
print("   +:+          +:+        +:+    +:+    +:+ +:+        :+:+:+  +:+  +:+   +:+  ")
print("  +#+          +#+        +#+    +#++:++#:  +#++:++#   +#+ +:+ +#+  +#+   +:+   ")
print(" +#+          +#+        +#+    +#+    +#+ +#+        +#+  +#+#+#  +#+   +#+    ")
print("#+#    #+#   #+#        #+#    #+#    #+# #+#        #+#   #+#+#  #+#   #+#     ")
print("###################    ###    ###    ### ########## ###    ####   #######       ")

print("1. Run Scripts")
print("2. View Checklist")
print("3. Quit")
choice1 = input("What would you like to do? ")

if choice1.toString() == "1":
	scriptRun()
elif choice1.toString() == "2":
        checklist()
else:
        exit("Exiting.")
exit("Exiting.")
