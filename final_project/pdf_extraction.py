import os
import pdfminer

for a in range(2009,2010):
	
	directory = "data/%s" % str(a)	
	files = os.listdir(directory)

	for file in files:

		output = os.path.splitext(os.path.basename(file))[0] + ".txt"

		input_file = "data/%s/%s" % (str(a), file)

		output_file = "data/%s/%s" % (str(a), output)

		os_call = '"' + str("pdf2txt.py -o %s %s" % (output_file, input_file)) + '"'
		# print os_call
		os.system(os_call)
