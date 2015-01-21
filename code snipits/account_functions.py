############ ACCOUNT FUNCTIONS ############
# logs the user in. takes in the file name. returns the data in a 2d list
def get_songs(file_name):
	# open the account data file
	account = open('data/' + file_name + '.dat', 'r')

	# delcare variables
	song = 0
	song_list = []

	# for each line in account 
	for song in account:
		song = song.rstrip('\n')
		song_list.append(song.split(', '))

	# close the file
	account.close()

	# returns all of data in a 2d list
	return(song_list)

# creates a new account (new data file). 
def new_account(account_name):
	account = open(account_name + '.dat', 'w')

########## MINK FUNCTIONS ###########
import os 

def get_filenames():
	# constants and variables
	data = './data'
	file_list = []
	i = 0

	# get names of what is in the directory
	file_list = os.listdir(data)

	# search the list for 'DS_Store' (some proprietary apple thing)
	for name in file_list:
		if name == '.DS_Store':
			print(name)
			file_list.remove('.DS_Store')

	# remove '.dat'
	for i in range(len(file_list)):
		file_list[i] = file_list[i].rstrip('.dat')
	
	# returns a list of the filenames
	return(file_list)


