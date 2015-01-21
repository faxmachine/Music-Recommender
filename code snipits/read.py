# takes in the file name
def log_in(file_name,command):
	# open the account data file
	account = open(file_name + '.dat', 'r')

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

