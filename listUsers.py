import os

if not os.geteuid() == 0:
    exit("\nOnly root can run this script\n")

def remUsers(usersDel):
	print('Removing Users...')
	for iduser in usersDel:
		fullCommand = 'deluser ' + iduser
		command2 = os.popen(fullCommand)
		result = command2.read()
		print(result, "\n")
#Function which removes users from the system based on the array which is input.

command = os.popen('awk -F: \'($3>=1000)&&($1!="nobody"){print $1}\' /etc/passwd')
#Grab all users from the passwd file with uid greater than 1000 which is all the nonsystem users.

userList = command.read().split()
#Split the results of the passwd file into an array of user names.

print('Current users on system:', userList)

f = open('authUsers', 'r')
if f.mode == 'r':
	authedUsers = f.read().split()
	print('\nAuthorized users:', authedUsers)
else:
	exit('File authUsers not available. Exiting.')
#Open the authorized users file and return an error if it is not available.

unauthedUsers = []
for user in userList:
	if user in authedUsers:
		print()
	else:
		unauthedUsers.append(user)
#Compare the users found in the passwd file to the authorized users file.

print('\nUnauthorized users:', unauthedUsers, '\n')

if not unauthedUsers:
	exit('No unauthorized users found. Exiting.')

print('Would you like to remove these unauthorized users? (y/n)')
yesorno = input()

if yesorno == 'y' or yesorno == 'Y':
	print('Removing users...')
	remUsers(unauthedUsers)
else:
	exit('Not removing users. Exiting.')

exit('Finished. Exiting.')
