import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
# finds the tag 'name' and prints the text within that tag
print('Name:', tree.find('name').text)
# searches the attribute hide in email and gets the value of the attribute
print('Attr:', tree.find('email').get('hide'))