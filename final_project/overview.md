Comments: This looks really cool. I think the insights gained here would be of general iterest to the community. 
I suggest also bulding a classifier using the metrics from your NLP analysis to try an predict what year an OOS 
description was generated.

## General Assembly Data Science course - Final project

### How has the field of machine learning changed since 2005?

**Abstract**

I'm planning to investigate how the field of machine learning has evolved over the last 8 years by analyzing the text of all of the available final projects from the Stanford CS229 Machine Learning course (around 1,000 final project reports from the CS229 course covering the period 2005 to 2012). 

**Motivation**

According to Thomas H. Davenport and D.J. Patil, Data Scientist is the "Sexiest Job of the 21st Century" (Harvard Business Review, October 2012). Given the significant amount of interest in the field of data science, I thought it would be interesting (and kind of *meta*) to use the tools I've learned in this data science class to analyze changes in the tools used by students of one of the world's leading machine learning programs.  

While the potential insights could be interesting and possibly *infographicable*, I'm mostly hoping to use this final project as an opportunity to learn more about many of the tools and techniques that we use internally at Science Exchange. Specifically:

* Web scraping techniques
* NoSQL databases, mostly likely Redis
* MapReduce via Amazon Elastic MapReduce (Amazon EMR)
* NLTK and other natural language processing tools
* d3.js and other visualization tools

**Proposed project**

1. **Obtain data**
Write a script to download and store all of the available final projects from the Stanford CS229 Machine Learning course (Status: *Done, 950 PDFs stored*)

2. **Clean and reformat data** 
Extract text from PDFs using PyPDF2, pdf2txt or something similar and store data in a Redis key-value format (Status: *Started, text extraction using pdf2txt tested*) 

3. **Perform NLP-style analysis to identify interesting trends**
Use a number of NLP techniques to analyze the content of the projects (e.g. tokenizing, ngrams, word count). Create a dictionary of machine learning concepts and see how use of machine learning tools and techniques has changed since 2005 (Status: *Not started*)

4. **Visualization**
Depending on the results of the NLP analysis, use modern visualization tools to showcase 2-3 interesting insights (Status: *Not started*)
