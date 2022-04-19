from HashTable import HashTable

h=HashTable()
h.set('joel', 'grayson')
h.set('david', 'kanovich')
h.set('number of people', 2)
h.set('key', 'value')

print(h)
print('Size', h.getSize())
print(h.get('joel'))
print(h.get('david'))
print(h.get('number of people'))
print(h.remove('key'))
print(h)
h.clear()
print(h)
