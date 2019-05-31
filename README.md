# fessbot
A python program and AI model that automatically posts to the website LeedsFess.

LeedsFess is a website run by uni-truths.com and is the confessions page for the University of Leeds, the facebook page where the posts end up is followed by the majority of the students at the university (or at least all of my friends).

The program is composed of three modules; training.py, generation.py, submission.py

The program generates new LeedsFess posts having been trained off a dataset of 999 fess's over a course of 500 epochs. It does this using the https://github.com/minimaxir/textgenrnn textgenrnn python module (a sample model is include in the repo but there is also a training script if you wish to update the model). 

Having done this is then submits then too LeedsFess by mimicking a web user. This is achieved in two main ways.
* Reccieving the two cookies that the site provides to users when they first visit and getting a new pair for each new fess
* Using BeutifulSoup4 https://www.crummy.com/software/BeautifulSoup/ to scan the HTML of the webpage in order to acquire a token from the site's form

With these it can send off fess's as if it where a standard web user.
