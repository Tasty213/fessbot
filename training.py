# Program to train an AI to generate Leeds Fess posts and
# save the model to a file

# Import the necessery libraries
from textgenrnn import textgenrnn
import time

def train():
	
	# Establish a useful abbreviation
	textgen = textgenrnn()

	# Reset the current state of the model
	textgen.reset() 

	# Train the model from the file fesses.txt over the course
	# of 500 epochs (complete passes of the data set)
	textgen.train_from_file('fesses.txt',num_epochs=500)

	# Save the new state of model to a file called fessbot.hdf5
	textgen.save("./fessbot.hdf5")

