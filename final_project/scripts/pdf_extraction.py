import pdfminer
import os

os.system("pdf2txt.py -o output.txt 'research_2.pdf'")

"""
for a in range(2005,2013):
	# go to directory
	directory = "data/%s" % str(a)

	# for each file in directory
	#run pdf2txt function outputing to txt

	# add all articles from one year to a single file
	# separate articles into different chapters
"""
