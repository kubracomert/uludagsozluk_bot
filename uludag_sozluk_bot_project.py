import requests
import json
from bs4 import BeautifulSoup

pages=[1,2,3,4,5]
datas=[]
for i in pages:
    req=requests.get("https://www.uludagsozluk.com/k/denizli/{}/".format(i))

    soup=BeautifulSoup(req.content,"html.parser")
    capsuls=soup.find_all("div",attrs={"class":"entry"})
 
    for capsul in capsuls:
        textt=capsul.find("div",attrs={"entry-p"})
        down=capsul.find("span",attrs={"class":"eksi_sayi"})
        up=capsul.find("span",attrs={"class":"arti_sayi"})
        datas.append({"entry":textt.text,"down":down.text if down.text else 0,"up":up.text if up.text else 0})
print(datas)

