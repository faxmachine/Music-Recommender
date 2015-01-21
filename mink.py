# this function is what calculates the account that has the most similar rating 
# to the account logged in.
from file_manip import *
import constants as c

def get_similar(account_name):
	# declare variables
	filename = 0
	sorted_distances = []

	#distances
	distance = 0
	distances = []

	# 2d lists 
	variant = 0
	i = 0
	j = 0

	# get songs from account file
	user_songs = get_songs(account_name)
	
	#print('got songs')

	# gets the file names it has to compare it to
	files = get_filenames()

	#print('got filenames')

	# alright, so this loop will open each account file get the songs, compare it to
	# the user's account and then add it to the manhatten distance.
	# NOTE: 'filename' is the account name. ex: ben hannah, shannon

	variant = get_songs('ben')
	
	for filename in files:
		
		if filename != account_name: # get songs from the accounts that are not itself
			
			# get the songs from what it is comparing the user to 
			variant = get_songs(filename)
			
			# cycles through all of the users songs
			for i in range(len(user_songs)):
					
					# for each song in the user_songs it compares it to each one of the songs
					# in the other account (variant)
					for j in range(len(variant)):
						if user_songs[i][c.TITLE] == variant[j][c.TITLE]:

							#Calculate manhattan distance using Mink distance metric
							distance += taxicab(int(user_songs[i][c.RATING]),int(variant[j][c.RATING]))
							
			# add the new distance to the 'distances list' 
			variant = []
			distances.append([distance,filename])		
			distance = 0
	# sort the accounts form least to greatest

	sorted_distances = sorted(distances, key = lambda pair: pair[0])
	
	# return most similar account
	
	return(sorted_distances[0][1])
	









