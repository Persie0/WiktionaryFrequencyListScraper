# importing the modules
import requests
from bs4 import BeautifulSoup
import sys

# providing url
url = sys.argv[1]

# creating requests object
html = requests.get(url).content

# creating soup object
data = BeautifulSoup(html, 'html.parser')

# get h1 with list name
listname = data.select('h1')[0].text.strip().replace("Wiktionary:Frequency lists/", "") + ".txt"
file1 = open(listname, "w", encoding="utf8")

# finding parent <ol> tag
parent = data.find("body").find("ol")
for entry in parent:
    link = entry.find("a")
    if type(link) != int:
        file1.write(link.contents[0]+"\n")

file1.close()
