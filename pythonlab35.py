from turtle import done


names = ['Jessa', 'Eric', 'Bob']


with open(r'test.txt', 'w') as fp:
    for item in names:
        
        fp.write('\n'.join(names))
print(names)