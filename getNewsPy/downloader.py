from lxml import html
import requests

# Gets web page source
pageSource = requests.get('https://www.haberturk.com/')

# Gets page content from page source as html
pageContent = html.fromstring(pageSource.content)

# This will create a list of titles
# TODO: add some logic that remove extra special characters from titles
titles = pageContent.xpath('//span[@class="title"]/text()')

# Prints all titles in web page
print 'titles: ', titles
