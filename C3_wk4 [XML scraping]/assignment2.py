from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Bayley.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags

# Look at the parts of a tag
for i in range(0, 7):
    tags = soup("a")
    tag = tags[17]
    print(tag.contents[0])

    url = tag.get("href", None)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
