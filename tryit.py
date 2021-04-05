import requests
from bs4 import BeautifulSoup
url = "https://www.mypetrolprice.com/petrol-price-in-india.aspx"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
all_states = soup.find_all("div",{"class":"sixteen columns row"})
s = all_states[3]
states = s.find_all("h2")
state_to_districts = {}
place_url = {}
for elem in states: 
	temp = []
	print(elem.text)
	tctx = elem.find_next("div",{"class":"txtC"})
	districts = tctx.find_all("div",{"class":"SF"}) if tctx else []
	for district in districts: 
		ch = district.find("div",{"class":"CH"}) if district else []
		print(ch)
		a_link = ch.find_all("a")
		if a_link:
			url = a_link[-1]["href"]
			num = url.split("/")[-2]
			ap_text = "?FuelType=0&LocationId="+num
			url += ap_text
			temp.append([url,a_link[-1].text])
			place_url[a_link[-1].text] = url
	state_to_districts[elem.text] = temp
	print("#"*30)
print(state_to_districts)

import json
data_file = open("districts","a")
data_file.write(json.dumps(place_url))
data_file.close()
