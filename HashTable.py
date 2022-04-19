"""
set(), get(), remove(), size(), clear()

# Examples:
ht=HashTable()
ht.set('hi', 'world')
ht.get('hi') -> 'world'
"""

from HashFunction import hashFunction, getMax
from LinkedList import LinkedList

class HashTable:
  def __init__(self):
    self.size=0
    self.clear()

  def set(self, key, value): # Assign to [key, value] if not exists, otherwise append to LinkedList
    hkey=hashFunction(key)
    if self.get(hkey) is not None: #if the value does not exist yet, increase size
      self.size+=1
      self.data[hkey]=[key, value]
    else: #already value there
      if type(self.get(hkey)) is LinkedList: #already linked list, so set
        lst: LinkedList=self.get(hkey)
        node=lst.get_head()
        while True:
          if node.get_value() is not None:
            if node.get_value()[0]==hkey:
              node.set_value([hkey, value])
          node=node.get_next()
        
      else: #create LinkedList because value is not there yet
        pass
      # LinkedList()
    pass

  def get(self, key): #returns value
    fetched=self.data[hashFunction(key)]
    if fetched is None: #nothing at that index
      return None
    return fetched[1] #value of fetched

  def remove(self, key) -> any:
    self.size -= 1
    val=self.get(key) #return the removed value
    self.data[hashFunction(key)]=None
    return val
  
  def getSize(self) -> int: #getter
    return self.size
  
  def clear(self): #remove all items
    self.data=[None for i in range(getMax())]

  def __str__(self): #format like a python array
    isEmpty=True
    string='{\n' #open brace
    for item in self.data:
      if item is not None: #add every item in {key}: {value}, format
        string+=f'\t{item[0]}: {item[1]},\n'
        isEmpty=False
    string+='}' #close brace

    if isEmpty:
      return '{}'
    
    return string
