import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

uppercaseLetter1=chr(random.randint(65,90)) 
uppercaseLetter2=chr(random.randint(65,90)) 
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
digit1=chr(random.randint(48,57))
digit2=chr(random.randint(48,57))
punctuationSign1=chr(random.randint(32,152))

password = uppercaseLetter1 + lowercaseLetter1 + uppercaseLetter2 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1
password = shuffle(password)

print(password)