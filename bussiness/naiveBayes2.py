import io
import string
import re

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

#from stemming.porter2 import stem
def validWord(word):
	invalidChars = set(string.punctuation.replace("_", ""))
	if any(char in invalidChars for char in word):
		return False
	if(len(word)<=2  or len(word)>15):
		return False
	if (' ' in word):
		return False
	if (hasNumbers(word)==True):
		return False
	return True
count=0
text_file = open("vocabulary.txt", "w")
for i in range (1, 2760):
	x=str(i) +".txt"
	try:
		with open(x,'r') as f:
		    for line in f:
		        for word in line.split():
		        	#stem(word)
		        	print(word)
		           	if (validWord(word)==True): 
		        		text_file.write(word+"\n")
		        		count=count+1
	except IOError:
		continue
print count
text_file.close()


