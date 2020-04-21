from bs4 import BeautifulSoup
import requests

with open('Example of a simple HTML page.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml') #creating an instance

#to print all of the content of the html page
#print(soup.prettify())      prettify adds required indents that are there in the file


#to print the title of the html page
title = soup.title       #will include the title tag too
print(title)

title=soup.title.text      #includes only the text and excludes the title tag
print(title)

#this post tells how one can scrap the popular websites , so we will scrap this post hahahahahahahahahahahahaha !!!!
source = requests.get('https://towardsdatascience.com/scraping-the-internets-most-popular-websites-a4c6f0be382d').text

soup = BeautifulSoup(source,'lxml')
print(soup.prettify())