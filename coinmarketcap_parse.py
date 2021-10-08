from bs4 import BeautifulSoup
import os
import pandas
import glob

df = pandas.DataFrame()

if not os.path.exists("parsed_files"):
    os.mkdir("parsed_files")
for file_name in glob.glob("html_files/*.html"):
	# file_name = "html_files/coinmarketcap20210928145827.html"
	# print(file_name)

	scrape_time = os.path.basename(file_name).replace("coinmarketcap","").replace(".html","")
	print(scrape_time)
	f = open(file_name, "r")

	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()
	currencies_table = soup.find("tbody")
	currency_rows = currencies_table.find_all("tr")
	for currency_row in currency_rows: 
		# currency_row = currency_rows[0]
		# print(currency_row)
		currency_columns = currency_row.find_all("td")
		if len(currency_columns)>5:
			currency_price = currency_columns[3].find("a", {"class": "cmc-link"}).text.replace("$","").replace(",","")
			currency_name = currency_columns[2].find("p").text
			currency_symbol = currency_columns[2].find("p", {"class": "coin-item-symbol"}).text
			currency_marketcap = currency_columns[6].find("p").find("span", {"class": "sc-1ow4cwt-1"}).text.replace("$","").replace(",","")
			currency_link = currency_columns[2].find("a")["href"]
			currency_img = currency_columns[2].find("img")["src"]

			df = df.append({
				'time': scrape_time,
				'name': currency_name,
				'price': currency_price,
				'symbol': currency_symbol,
				'marketcap': currency_marketcap,
				'link': currency_link,
				'img':currency_img
				}, ignore_index=True)
df.to_csv("parsed_files/coinmarketcap_dataset.csv") 
