import urllib2
from bs4 import BeautifulSoup

quote_page = 'https://www.basketball-reference.com/teams/PHO/2018.html'

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

#Webscrape from basketball-reference.com to obtain the player's name and weight
name_box = soup.find_all('td', attrs={'data-stat': 'player'})
weight_box = soup.find_all('tr', attrs={'csk': '$'})


#trials

#for _ in range(len(name_box)):
#    print(name_box[_].text.strip())

for _ in range(len(weight_box)):
    print(weight_box[_].text.strip())





