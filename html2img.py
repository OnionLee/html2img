import os
import codecs
from bs4 import BeautifulSoup
import urllib.request

while True:
    try:
        print("type filename")
        filename = input()
        dic = os.path.dirname( os.path.abspath( __file__ ) )
        path = dic + "/" + filename
        f = codecs.open(path, "r", "utf-8")
        break
    except Exception as e:
        print(e)
    
html_doc = f.read()
f.close()

soup = BeautifulSoup(html_doc, "html.parser")
page_images = [image["src"] for image in soup.findAll("img")]
count = 0
for img in page_images:
    count = count + 1
    split = img.split("?")
    try:
        urllib.request.urlretrieve(split[0], split[0].split('/')[-1])
        print("[{0}/{1}]{2}".format(count, len(page_images), split[0]))
    except Exception as e:
        print("[{0}/{1}]{2}".format(count, len(page_images), e))

input()
