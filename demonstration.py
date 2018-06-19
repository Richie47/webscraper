import urllib2
from bs4 import BeautifulSoup

quote_page = 'https://www.espn.com/nba/team/roster/_/name/phx/phoenix-suns'

print quote_page

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

#This makes an array of all the rows
row_box = soup.find_all('tr', attrs={'class': 'oddrow'})

#This makes an array of all elements in the first row
units = row_box[0].find_all('td')


#Examples
print (units[7].text.strip())

row = row_box[1].text.strip()

print(row)

name_box = soup.find('td', attrs={'class': 'sortcell'})

name = name_box.text.strip()

print(name)
