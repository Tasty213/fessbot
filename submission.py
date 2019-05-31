# Used for parsing the web page to get a _token
from bs4 import BeautifulSoup
# Used to send and reccieve HTTP requests
import requests

# Set the url of leedsfess
url = 'https://leedsfess.uni-truths.com/'

# Set a testing fess to be submited (will normaly be passed into the function)
# fess = 'sooo, this works???'

def submit( fess ):
	# Begins a requests session used to ensure the cookies are always the same
	client = requests.session()

	# Downloads the actual html of leedsfess and extracts a token from the form field
	page = client.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	token = soup.input['value']

	# Prepare the payload of the POST request
	data = [('_token', token), ('text', fess)]

	#pint out the info that will be sent
	#print(data)
	#print(client.cookies)

	# send a post request to leedsfess with the data an cookies
	response = requests.post(url, data = data, cookies = client.cookies)

	# Prints out the url that the request was sent too
	#print(response.url)

	#print(response.text)

	# if statement to notify whether the posting succeeded
	if 'Sorry, your session has expired. Please refresh and try again.' in response.text:
		print('Session has expired')
	elif 'Post already submitted!' in response.text:
		print('Post has already been submitted')
	elif 'Confession Submitted' in response.text:
		print('Confession Submitted')
	else:
		print('No applicable criteria')
