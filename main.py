import generation as gen
import training as train
import submission as sub

while True :
	# Write a post and save to post
	post = gen.writePost( 0.85 )
	
	# Print the post for comedic effect
	print(post)
	
	# Submit the post
	sub.submit(post)































