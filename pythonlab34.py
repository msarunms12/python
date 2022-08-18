import os

file_stat = os.stat('test.txt')
print(file_stat.st_size)