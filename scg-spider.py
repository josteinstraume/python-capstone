import csv, requests
from BeautifulSoup import *
url = "http://sales.starcitygames.com//deckdatabase/deckshow.php?t%5BT3%5D=3&event_ID=&feedin=&start_date=01%2F01%2F1993&end_date=02%2F12%2F2017&city=&state=&country=&start=&finish=&exp=&p_first=&p_last=&simple_card_name%5B1%5D=&simple_card_name%5B2%5D=&simple_card_name%5B3%5D=&simple_card_name%5B4%5D=&simple_card_name%5B5%5D=&w_perc=0&g_perc=0&r_perc=0&b_perc=0&u_perc=0&a_perc=0&comparison%5B1%5D=%3E%3D&card_qty%5B1%5D=1&card_name%5B1%5D=&comparison%5B2%5D=%3E%3D&card_qty%5B2%5D=1&card_name%5B2%5D=&comparison%5B3%5D=%3E%3D&card_qty%5B3%5D=1&card_name%5B3%5D=&comparison%5B4%5D=%3E%3D&card_qty%5B4%5D=1&card_name%5B4%5D=&comparison%5B5%5D=%3E%3D&card_qty%5B5%5D=1&card_name%5B5%5D=&sb_comparison%5B1%5D=%3E%3D&sb_card_qty%5B1%5D=1&sb_card_name%5B1%5D=&sb_comparison%5B2%5D=%3E%3D&sb_card_qty%5B2%5D=1&sb_card_name%5B2%5D=&card_not%5B1%5D=&card_not%5B2%5D=&card_not%5B3%5D=&card_not%5B4%5D=&card_not%5B5%5D=&order_1=finish&order_2=&limit=100&action=Show+Decks&p=1"

r = requests.get(url)

soup = BeautifulSoup(r.content)

#decklists = soup.find_all("td", {"class":"deckdbbody"})
decklists = soup.find_all("td")
pagelists = soup.find_all("a", {"class":"href"})

for deck in decklists:
	try:
		print deck.contents[1].find_all("td", {"class":"deckdbbody"})[0].text
	except:
		pass

