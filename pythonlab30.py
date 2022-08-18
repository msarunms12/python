f = open("test.txt","r")
array = []
data = f.read()
l = data.split()
for line in l:
    array.append(line)
print(array)