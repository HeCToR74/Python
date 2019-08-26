import csv
import requests
from bs4 import BeautifulSoup

def parser_category(url, data_tl_id):
	'''
	За даною адресою (в даному випадку "https://www.walmart.com/all-departments")
	отримуємо список всіх категорій сайту
	'''
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')	
	category = soup.find_all('a', {"data-tl-id": data_tl_id})
	list_categories = []
	for item in category:
		data = {}		
		data["name"] = item.text
		url = item["href"].split("?")[0]
		data["href"] = url
		page = requests.get(url)
		soup = BeautifulSoup(page.text, 'html.parser')
		pagination = soup.find_all('div', {"class": "paginator outline"})
		pagination_links = pagination[0].find_all('a', )
		n = int(pagination_links[len(pagination_links)-1].text)
		list_links = [url + "?page=" + str(i) for i in range(1, n+1)]
		data["links"] = list_links
		list_categories.append(data)
	return(list_categories)

def parser_url(url):
	'''
	Парсинг конретної сторінки.
	Отримуємо необхідні дані по товарам.
	'''
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	wares = soup.find_all('script', {"id": "searchContent"})	
	dict_parse_data = eval(wares[0].text.replace("false", "False").replace("true", "True")
			.replace("null", "None"))
	list_item = dict_parse_data["searchContent"]["preso"]["items"]
	result_list_product = []
	for item in list_item:
		product = {}
		product["productId"] = item["productId"]
		product["title"] = item["title"]		
		product["productPageUrl"] = "https://www.walmart.com" + item["productPageUrl"]
		product["imageUrl"] = item["imageUrl"]
		if "offerPrice" in item["primaryOffer"].keys():
			product["offerPrice"] = item["primaryOffer"]["offerPrice"]
		elif "maxPrice" in item["primaryOffer"].keys():
			product["offerPrice"] = item["primaryOffer"]["maxPrice"]
		elif "minPrice" in item["primaryOffer"].keys():
			product["offerPrice"] = item["primaryOffer"]["minPrice"]
		else:
			product["offerPrice"] = None
		if "numReviews" in item.keys():
			product["numReviews"] = item["numReviews"]
		else:
			product["numReviews"] = None
		if "customerRating" in item.keys():
			product["customerRating"] = item["customerRating"]
		else:
			product["customerRating"] = None
		if "upc" in item.keys():
			product["upc"] = item["upc"]
		else:
			product["upc"] = None
		if "quantity" in item.keys():
			product["quantity"] = item["quantity"]
		else:
			product["quantity"] = None
		result_list_product.append(product)
	return result_list_product	

def data_to_csv(data, filename):
	'''
	Функція для запису списку словників в csv-файл.
	'''
	fieldnames = ["productId", "title", "productPageUrl", "imageUrl", "offerPrice",
					"numReviews", "customerRating", "upc", "quantity"]
	with open(filename+'.csv', 'w', newline='', encoding="utf-8") as out_file:
		writer = csv.DictWriter(out_file, delimiter=';', fieldnames=fieldnames)
		writer.writeheader()
		writer.writerows(data)
	print("Saved successfully!")

def start(list_products, list_ids, filename):
	'''
	За списком ID записуємо дані про відповідні товари в заданий файл.
	'''
	data = []
	for item_id in list_ids:
		for item in list_products:
			if item_id == item["productId"]:
				data.append(item)
	data_to_csv(data, filename)
		
def main():
	url = "https://www.walmart.com/all-departments"
	data_tl_id = "AllDepartments-superdept-0-column-2-department-0-categoryLink-1"
	print("List of categories:")
	list_categories = parser_category(url, data_tl_id)
	for category in list_categories:
		print("{}.".format(list_categories.index(category)+1), category["name"])
	while True:
		try:
			number_category = int(input("Select category (enter the number of category): ")) - 1
			if number_category in range(len(list_categories)):
				break
			else:
				print("Incorrect! Select from 1 to {}".format(len(list_categories)))
		except:
			print("Incorrect! Select from 1 to {}".format(len(list_categories)))

	select_category = list_categories[number_category]
	list_products = []
	for link in select_category["links"]:
		print("Page {} is being parsed".format(select_category["links"].index(link)+1))
		list_products += parser_url(link)

	data_to_csv(list_products, select_category["name"])

	if input("Would You like to save data by ID (y/n)?") == "y":
		list_ids = input("Input list of ID (usinq spaces): ").split()
		filename = input("Input file name: ")
		start(list_products, list_ids, filename)


if __name__ == '__main__':
	main()