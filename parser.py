import requests
import fake_useragent
import random
from bs4 import BeautifulSoup as BS

def get_html(html, rnd):

	global r
	r = requests.get(f'{html}{rnd}').text
	print(f'{html}{rnd}')

def parse(obj, rnd):
	try:

			soup = BS(r, 'lxml')
			block = soup.find('div', class_ = obj)
			img = block.find('img').get('src')
			split = img.split('?', 1)
			print(split[0])
			byte = requests.get(split[0], allow_redirects=True)
			return byte.content
	
	except Exception as a:
		print(str(a))

