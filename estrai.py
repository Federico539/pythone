import urllib.request
url = "https://www.comuni-italiani.it/province.html"
response = urllib.request.urlopen(url)
theBytes = response.read()
text = theBytes.decode(encoding="iso-8859-1")

import bs4
doc = bs4.BeautifulSoup(text)
elems = doc.find_all("table")
table = elems[3]
for tr in table.contents[2:-2]:
    if type(tr) == bs4.element.Tag:
        tds = tr.contents
        sigla = tds[7].get_text()
        nome = tds[1].get_text()
        res = int(tds[2].get_text().replace(".",""))
        sup = int(tds[4].get_text().replace(".",""))
        print(f"{sigla} {nome} {res} {sup}")

print()
print()

for tr in table.contents[2:-2]:
    if type(tr) == bs4.element.Tag:
        tds = tr.contents
        sigla = tds[7].get_text()
        res = int(tds[2].get_text().replace(".",""))
        sup = int(tds[4].get_text().replace(".",""))
        dens = float(tds[5].get_text().replace(",","."))
        myDens = round(res/sup , 1)
        print(f"{sigla} {dens} {myDens}")