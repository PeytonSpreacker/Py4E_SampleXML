import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
# puts all the data under a users/user tag path in lst
lst = stuff.findall('users/user')
# prints the length of the list, or the number of users
print('User count:', len(lst))

# iterates through the items in the list to parse data
for item in lst:
    # parses the text under the name tag
    print('Name:', item.find('name').text)
    # parses the text under the id tag
    print('ID:', item.find('id').text)
    # parses the value of the given attribute
    print('Attribute:', item.get('x'))