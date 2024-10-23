file = open('test.txt', 'r+')
for each in file:
    print(each)
#write into test.txt

file.write("Hello World")
print (file.read(5),"\n")
file.seek(0)

for each in file:
    print(each)

file.close()