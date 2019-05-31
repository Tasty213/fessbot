# Program to automatically generate Leeds fess posts (needs a 
# pre-trained model)
from textgenrnn import textgenrnn
import time

print('Loading model')

textgen = textgenrnn('fessbot.hdf5')

fessbotSignature = '  ---Fessbot ;)'

# DON'T RESET textgen.reset()
# This will ensure that the model is used

# Open the training set file in read only mode
trainingSet = open('fesses.txt', 'r')
# Double check that the file is in read only mode
if trainingSet.mode == 'r':
	# If it is then read all the data from it and save it into
	# a string
	check = trainingSet.read()

# When called will return a post
def writePost( temperature ):
	while True:
		# Generate a post and save as a list, this is different to a
		# string and must be converted before it can be used to check
		# if it's an original fess, tried with return_as_string but
		# there's no argument for it
		postList = textgen.generate(temperature=temperature, return_as_list=True) 
		
		# Converts the list to a string
		# https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
		post = ''.join(postList)
		
		# Checks if the post is not in the training set
		if post not in check:
			# If it isn't the append signature to the post and return
			finalPost = post + fessbotSignature
			return finalPost



