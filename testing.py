from hash import hash
from HashTable import HashTable

def demo():
    ht=HashTable()
    
    ht.set('joel', 'grayson')
    ht.set('david', 'kanovich')
    ht.set(3, 14159)
    ht.set(False, ['opposite of True'])
    
    print(ht)
    print('Size:', ht.size())
    print('joel:', ht.get('joel'))
    print('david:', ht.get('david'))
    print('3:', ht.get(3))
    print('Removing 3', ht.remove(3))
    print(ht)
    print('clearing')
    ht.clear()
    print(ht)

def has_test():
    ht=HashTable()
    ht.set('hi', 'world')
    ht.set(0, 1)
    print(ht)
    print(ht.has('hi'))
    print(ht.has('no'))

def keys_values_test():
    ht=HashTable()
    ht.set('hello', 'world')
    ht.set(2, 4)
    ht.set(4, 8)
    ht.set(8, 16)
    ht.set(True, False)
    print(ht.keys())
    print(ht.values())
    

def high_collisions_test():
    ht=HashTable(max_registers=3)
    ht.set('key1', 'value1')
    ht.set('key2', 'value2')
    assert 2==ht.size()
    ht.set('key3', 'value3')
    ht.set('key4', 'value4')
    ht.set('key5', 'value5')
    assert 5==ht.size()
    
    print(ht.inspect())
    assert ht.get('key1')=='value1'
    assert ht.get('key2')=='value2'
    assert ht.get('key3')=='value3'
    assert ht.get('key4')=='value4'
    assert ht.get('key5')=='value5'
    
    ht.remove('key3')
    print(ht.inspect())
    print(ht.size())

def remove_test():
    ht=HashTable()
    ht.set('hi', 'there')
    ht.set('joel', 'grayson')
    ht.set('david', 'kanovich')
    print(ht)
    assert ht.remove('joel')=='grayson' #remove returns removed value
    ht.remove('david')
    print(ht)

def size_test():
    ht=HashTable()
    assert ht.size()==0
    ht.set('hi', 'world')
    ht.set(3, 14159)
    ht.set(False, True)
    ht.set('my array', [1, 2, 3])
    assert ht.size()==4
    ht.remove('my array')
    assert ht.size()==3

#Hash function generates unique indices
def hash_test(): #hash function test
    print(hash('hi'))
    print(hash('joel'))
    print(hash(False))
    print(hash(True))
    print(hash(3))

def test_all():
    demo()
    high_collisions_test()
    remove_test()
    size_test()
    has_test()
    keys_values_test()
    hash_test()
    print('✅ All tests past') #reach here no asserts were violated
