#!/bin/python

# Download Census india data from data.gov.in

"""
# Example urls
# https://data.gov.in/node/974421/download
# https://data.gov.in/node/973261/download

# generated source url patterns 
# https://data.gov.in/catalog/primary-census-abstract-census-2001-india-and-states?title=&file_short_format=
# https://data.gov.in/catalog/primary-census-abstract-census-2001-india-and-states?title=&file_short_format=&page=2

On each page, use beautiful soup to extract the docid 
dd = document.getElementsByClassName("download-confirmation-box")[0]
docid = dd.classList[2].replace("confirmation-popup-", "")
doc_url = https://data.gov.in/node/<docid>/download

doc_url returns an html that has a <meta> tag
extract final link to xls file from that tag e.g.

<meta content="1;url=http://www.censusindia.gov.in/datagov/2001_files/PCA/PCA1703_South_Garo_Hills_-2001.xls" http-equiv="refresh"/>

"""
import os
from bs4 import BeautifulSoup
import requests

DOC_URL = "https://data.gov.in/node/%s/download"
DATA_GOV_IN_PAGE_URL = "https://data.gov.in/catalog/primary-census-abstract-census-2001-india-and-states?title=&file_short_format=&page=%d"
NUMBER_OF_PAGES = 106

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":
	for count in range(NUMBER_OF_PAGES):
		data_gov_in_page_url = DATA_GOV_IN_PAGE_URL % count
		response = requests.get(data_gov_in_page_url)
		soup = BeautifulSoup(response.text, "html.parser")
		divs = soup.find_all("div", class_="download-confirmation-box")
		for div in divs:
			doc_id = div["class"][2].strip("confirmation-popup-")
			doc_url = DOC_URL % doc_id
			print(doc_url)
			resp = requests.get(doc_url)
			meta_soup = BeautifulSoup(resp.text, "html.parser")
			document_final_url = meta_soup.find_all("meta")[1]["content"].split("=")[1]
			local_file_name = document_final_url.split("/")[-1:][0]
			if os.path.exists(os.path.join(CURRENT_DIR, local_file_name)):
				print("Already downloaded at %s. Skipping it." % (os.path.join(CURRENT_DIR, local_file_name)))
			else:
				print("downloading %s as %s" % (document_final_url, local_file_name))
				fc = requests.get(document_final_url)
				with open("%s" % local_file_name, "wb") as output:
					output.write(fc.content)
