import urllib.request
url = "https://drgnslyr.tripod.com/startrek/startrek.htm"
result = urllib.request.urlopen(url)
bytes = result.read()
texting = bytes.decode()
import bs4
document = bs4.BeatifulSoup(texting)
print(document.prettify())
