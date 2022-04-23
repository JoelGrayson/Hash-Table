# HashTable Documentation
## Getting Started
```py
from HashTable import HashTable
ht=HashTable()
```

## Methods
get, set, clear, remove, size, is_empty, has, keys, values, inspect

### get(key) -> value
    Returns the HashMap's value of the key

### set(key, value) -> None
    Sets the HashMap to your value at the key

### clear() -> None
    Removes all the key-value pairs, emptying the HashMap.

### remove(key) -> value
    Removes the key-value pairs at the specified key. Returns the removed value.

### size() -> int
    Returns the number of key-value pairs.

### is_empty() -> bool
    Returns whether or not the HashMap has no key-value pairs.

### has(key) -> bool
    Returns whether or not the HashMap has a key-value pair of the specified key.

### keys() -> array[any]
    Returns all the keys of the HashMap in an array.

### values() -> array[any]
    Returns all the values of the HashMap in an array.

### inspect() -> str
    Returns the raw self.data for development purposes


## Example
```py
>>> ht=HashTable()
>>> ht.set('hi', 'world')
>>> ht.get('hi')
'world'
>>> ht.set('authors', ['joel', 'david'])
>>> print(ht)
HashTable {
	authors: ['joel', 'david'],
	hi: world
}
>>> ht.has('hi')
True
>>> ht.size()
2
>>> ht.keys()
['authors', 'hi']
>>> ht.values()
[['joel', 'david'], 'world']
>>> ht.remove('authors')
['joel', 'david']
>>> print(ht)
HashTable {
	hi: world
}
>>> ht.clear()
>>> print(ht)
{}
```
