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

command = os.popen('awk -F: \'($3>=1000)&&($1!="nobody"){print $1}\' /etc/passwd') #UID should be greater than 1000
userList = command.read().split()
print('Current users on system:', userList)

f = open('authUsers', 'r')
if f.mode == 'r':
	authedUsers = f.read().split()
	print('\nAuthorized users:', authedUsers)
else:
	exit('File authUsers not available. Exiting.')

unauthedUsers = []
for user in userList:
	if user in authedUsers:
		print()
	else:
		unauthedUsers.append(user)

print('\nUnauthorized users:', unauthedUsers, '\n')

if not unauthedUsers:
	exit('No unauthorized users found. Exiting.')

yesorno = input('Would you like to remove these unauthorized users? (y/n)')

if yesorno == 'y' or yesorno == 'Y':
	print('Removing users...')
	remUsers(unauthedUsers)
else:
	exit('Not removing users. Exiting.')

exit('Finished. Exiting.')