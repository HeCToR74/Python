import urllib.request
from urllib.error import HTTPError 
from bs4 import BeautifulSoup
import re
import sys

def find_email(url):
	'''
	Поиск емейлов за даным url адресом
	'''
	try:
		site = urllib.request.urlopen(url)
		html = site.read()
		mails = re.findall(r'[A-Za-z0-9\._+]+@[A-Za-z]+\.[A-Za-z]+', str(html))
		return mails
	except HTTPError as e:
		return [] 	

def find_link(url):
	'''
	Собираем все ссылки по url адрусу
	'''
	list_link = []
	try:
		# отбрасываем pdf-файлы
		if url.find("pdf") < 0:
			page = urllib.request.urlopen(url)
			soup = BeautifulSoup(page, 'html.parser')
			page_urls = soup.findAll('a')
			list_link = [link['href'] for link in page_urls if link.get('href') and link['href'][:4] == 'http']

			return list_link	

	except HTTPError as e:
		return [] 

if __name__ == "__main__":
	# считываем даные с командной строки
	url = sys.argv[1]
	n = int(sys.argv[2])

	# стартуем с url страницы
	list_url = [url]
	
	# формирум списак всех ссылок
	for i in range(n):
		new_list_url = []
		for url in list_url:
			for u in find_link(url):
				if u is not new_list_url:
					new_list_url.append(u)

		list_url = new_list_url
	
	# печать всех ссылок
	# print(list_url)

	result = []			
	# формируем список емейлов
	for url in list_url:
		for mail in find_email(url):
			if mail not in result:
				result.append(mail)

	for mail in result:
		print(mail)
		
