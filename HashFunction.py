def getMax():
  return 223 #standard
  # return 2 #for collisions

def hashFunction(i):
    o=17 #prime number best
    max=getMax()
    
    if type(i) is float or type(i) is int or type(i) is bool: #number or boolean
        o+=i
    elif type(i) is str: #string
        for char_num in bytes(i, 'utf-8'): #multiply by char code of every character
            o=(o*char_num) % max
    else:
        pass

    return int(o % max)


#Hash function generates unique indices
def test():
    print(hashFunction('hi'))
    print(hashFunction('joel'))
    print(hashFunction(False))
    print(hashFunction(True))
    print(hashFunction(3))


if __name__=='__main__':
  test()