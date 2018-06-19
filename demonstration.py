import urllib2
from bs4 import BeautifulSoup



quote_page = 'https://www.espn.com/nba/team/roster/_/name/phx/phoenix-suns'

print quote_page

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('td', attrs={'class': 'sortcell'})

name = name_box.text.strip()

print(name)


