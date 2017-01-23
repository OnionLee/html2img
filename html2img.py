import os
import codecs
from bs4 import BeautifulSoup
import urllib.request

print("type filename")
filename = input()
dic = os.path.dirname( os.path.abspath( __file__ ) )
path = dic + "/" + filename
f = codecs.open(path, "r", "utf-8")

html_doc = f.read()
f.close()

soup = BeautifulSoup(html_doc, "html.parser")
page_images = [image["src"] for image in soup.findAll("img")]
count = 0
for img in page_images:
    split = img.split("?type")
    print(split[0])
    urllib.request.urlretrieve(split[0], split[0].split('/')[-1])
   
