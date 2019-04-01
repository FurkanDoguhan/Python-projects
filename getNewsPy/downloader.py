"""import urllib2

url ='http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response =urllib2.urlopen(url)
webContent = response.read()

print(webContent[0:100])"""

from lxml import html
import requests

page = requests.get('https://www.haberturk.com/')
tree = html.fromstring(page.content)

#This will create a list of buyers:
titles = tree.xpath('//span[@class="title"]/text()')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')

print 'titles: ', titles
#print 'Prices: ', prices
