import urllib.request
from bs4 import BeautifulSoup
u = urllib.request.urlopen("https://www.imdb.com/movies-coming-soon/2019-04/")
x = u.read().decode("UTF-8")
soup = BeautifulSoup(x,"html.parser")
f = open("april_coming.txt","w")
f.write(soup.text)
f.close()
