
import urllib.request
import os

import datetime
import time

if not os.path.exists("html_files"):
	os.mkdir("html_files")



for i in range(1):
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)

	for j in range(5):
		page_num=j+1
		f = open("html_files/coinmarketcap" + "_" + str(page_num) + "_" + current_time + ".html", "wb")

		response = urllib.request.urlopen("http://coinmarketcap.com/?page=" + str(page_num))
		html = response.read()


		f.write(html)
		f.close()
		time.sleep(60)
	time.sleep(300)