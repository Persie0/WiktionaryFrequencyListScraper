# importing the modules
import time

import requests
from bs4 import BeautifulSoup

def create_text_file(url :str):
    html = requests.get("https://en.wiktionary.org"+url).content

    # creating soup object
    data = BeautifulSoup(html, 'html.parser')

    # get h1 with list name
    listname = data.select('h1')[0].text.strip().replace("Wiktionary:Frequency lists/", "").replace(" ", "_") + ".txt"
    file1 = open(listname, "w", encoding="utf8")

    # finding parent <ol> tag
    parent = data.find("body").find("ol")
    for entry in parent:
        link = entry.find("a")
        if type(link) != int:
            file1.write(link.contents[0] + "\n")

    file1.close()




# providing url
url = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists"

# creating requests object
html = requests.get(url).content

# creating soup object
data = BeautifulSoup(html, 'html.parser')

# finding parent <ol> tag
parent = data.select('a')
for entry in parent:
    try:
        text=entry.contents[0]
        if text != int:
            if "A Frequency Dictionary" in text:
                create_text_file(text.parent.get('href'))
    except:
        print()

