import requests
from bs4 import BeautifulSoup


url = "https://race.netkeiba.com/?pid=odds&id=c201901020411"
response = requests.get(url)
response.encoding = response.apparent_encoding
bs = BeautifulSoup(response.text, "html.parser")

horse_list = []
for i in bs.select('.txt_l'):
    horse_list.append(i.getText())
    with open("keiba.txt", mode="w", encoding='utf-8') as f:
        f.write("\n".join(horse_list))
