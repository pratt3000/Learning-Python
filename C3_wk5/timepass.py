import xml.etree.ElementTree as ET
data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
    7755922985 11
    </phone>
    <email hide="yes" />
</person>
'''

tree = ET.fromstring(data)
print("Name  : ", tree.find("name").text)
print("Attr. : ", tree.find("email").get('hide'))