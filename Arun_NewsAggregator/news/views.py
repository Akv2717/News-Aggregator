from os import replace
from django.shortcuts import render

import requests
from bs4 import BeautifulSoup


#getting news from times of india
toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')
toi_headings = toi_soup.find_all('h2')
toi_headings = toi_headings[0:-13] # removing footers
toi_news = []
for th in toi_headings:
     toi_news.append(th.text)

#Getting news from republic bharat

#Getting news from Hindustan times

pr2 = requests.get("https://ndtv.com/business")
psoup2 = BeautifulSoup(pr2.content, 'html5lib')
newsDivs_eco = psoup2.findAll("p",{"class":"headline"})
ndtv_news_eco =[]
newsDivs_eco=newsDivs_eco[0:4]
for n in newsDivs_eco:
   t = (n.text)
   ndtv_news_eco.append(t[29:])
print(len( ndtv_news_eco))
#for h in ndtv_news_eco:
  #  print(h)
def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, ' ndtv_news_eco':  ndtv_news_eco})