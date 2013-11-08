import pdfminer
import os


"""
for a in range(2005,2013):
	
	directory = "data/%s" % str(a)

	for file in directory:
"""

filename = '"../data/2005/proj2005-chang-DecodingCognitiveStatesFromFMRITimeseries.pdf"'
output = '../data/2005/proj2005-chang-DecodingCognitiveStatesFromFMRITimeseries.txt'
os_call = "pdf2txt.py -o %s %s" % (output, filename)
print os_call
os.system(os_call)



"""
for a in range(2005,2013):
	# go to directory
	directory = "data/%s" % str(a)

	# for each file in directory
	#run pdf2txt function outputing to txt

	# add all articles from one year to a single file
	# separate articles into different chapters
"""
