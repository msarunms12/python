data = data2 = ""
  

with open('test.txt') as fp:
    data = fp.read()
  
with open('second.txt') as fp:
    data2 = fp.read()
data += "\n"
data += data2
  
with open ('third.txt', 'w') as fp:
    fp.write(data)