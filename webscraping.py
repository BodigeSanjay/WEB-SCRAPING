import requests
from bs4 import BeautifulSoup
import html
import csv
URL="https://www.bikewale.com/yamaha-bikes/"
page=requests.get(URL)
soup= BeautifulSoup(page.content, 'html.parser')
image=soup.findAll('div',class_="imageWrapper")
img1=[]
for x in image:
    y=x.img["src"]
    img1.append(y)
print(img1)