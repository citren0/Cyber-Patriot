import os

if not os.geteuid() == 0:
	exit("\nOnly root can run this script\n")

print("-----  | /    |----| -----  |---|  ----- ")
print("|      |/     |    |   |    |   |    |   ")
print("-----  |-\    |----|   |    |---|    |   ")
print("    |  |  \   |-\      |    |        |   ")
print("-----  |   \  |  \   __|__  |        |   ")

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
                elif 'sh' in currentCom:
                        command = os.popen('sudo bash ' + currentCom)
                        command2 = command.read()

exit("Exiting.")
