import hashlib

def hash(temp_input): #SHA256 encodes
  bytes_input=str.encode(str(temp_input)) #convert input to string to binary
  # if type(bytes_input).__name__!='bytes':
  #   raise Exception('Needs to be a bytes')
  return hashlib.sha256(bytes_input).hexdigest()


if __name__=="__main__": #testing
  print(hash("hi"))
  print(hash(3))