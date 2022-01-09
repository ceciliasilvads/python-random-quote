import random

def primary():
	last = 16
	f = open("quotes.txt")
	quotes = f.read().splitlines()
	f.close()

	print('"%s"' %quotes[random.randint(0, last)])
	print('"%s"' %quotes[random.randint(0, last)])

if __name__== "__main__":
  	primary()