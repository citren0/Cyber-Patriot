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

print('')
