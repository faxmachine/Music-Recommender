def get_songs(file_name):
	# open the account data file
	account = open('data/' + file_name + '.dat', 'r')
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

def new_account(account_name):
	account = open(account_name + '.dat', 'w')

def save(account_name, song_list):
	account = open('data/' + account_name + '.dat', 'w')
	i = 0
	j = 0

	for i in range(len(song_list[i])):
		for j in song_list[i]:
			account.write(j + ', ')
		account.write('\n')

	account.close()