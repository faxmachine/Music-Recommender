#Ben Carroll
#CS021 Jackie Horton
#11/30/14
# get read functions
from file_manip import *
from mink import *
import constants as c

def main():
	file_name = 0
	most_similar = 0
	similar_songs = 0
	good_input = False

	while good_input == False:
		try:
			file_name = input('enter an account to log in to: ')
			most_similar = get_similar(file_name)
			similar_songs = get_similar_songs(most_similar)

			print(most_similar,'has a very similar taste in music \n')
			print('Here are some songs you might like :')
			for i in range(3):
				print('\t' + similar_songs[i][0] + ' - ' + similar_songs[i][1])

			good_input = True
		except:
			print('ERROR: Please enter a valid account')

main()