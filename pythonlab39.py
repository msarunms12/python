test_list = ['gf\ng', 'i\ns', 'b\nest', 'fo\nr', 'geeks\n']
 

print("The original list : " + str(test_list))
 

res = []
for sub in test_list:
    res.append(sub.replace("\n", ""))
print("List after newline character removal : " + str(res))