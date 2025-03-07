import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print("Retrieving ", url)

html = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(html)

total = 0
for r in tree.findall("./comments/comment"):
    total += int(r.find("count").text)
print("Sum: ", total)
