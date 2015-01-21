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


