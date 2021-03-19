#Web Scraping
import requests #call package
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
#page user defined object
print(page)
#our request, we get a Response object. This object has a status_code property,
#which indicates if the page was downloaded successfully:'''


print(page.status_code)
'''A status_code of 200 means that the page downloaded successfully.
We won’t fully dive into status codes here, but a status code starting with a 2
generally indicates success,and a code starting with a 4 or a 5 indicates an error.'''


#We can print out the HTML content of the page using the content property:
print(page.content)

from bs4 import BeautifulSoup #bs4 inbuilt package and BeautifulSoup inbuilt class of bs4
soup = BeautifulSoup(page.content, 'html.parser')
#soup user defined object of BeautifulSoup()
print(soup.prettify()) #prettify() inbuilt function  of BeautifulSoup class


'''We can now print out the HTML content of the page, formatted nicely,
using the prettify method on the BeautifulSoup object:'''

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('p')) #FIND ALL <P> OF HTML FILE and hold in list

print(soup.find_all('p')[0].get_text()) #to print only data of 0th index from list

print(soup.find('p')) #only print first <p>

print(list(soup.children))


#<img> : image
#<h1>
#<b> bold , <i> italic 





