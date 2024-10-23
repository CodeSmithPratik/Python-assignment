# #all file handling concepts
# # f1= open("file3.txt","w+")
# #     f1.write("file3.txt","Hey Hello this is the new file ")
# #     print(f1)
# # file = open("example.txt", "r")
# #         with open("file2.py", 'r') as f1:
# #             content = file.read()
# #             print(content)

# f1= open("f1.txt",'w+') 

# readH=f1.readlines()
# print(readH)
# f1.seek(3)
# f1.write("this is an interrupt \n")
# t=f1.tell()
# print(t)
# print(f1.readlines())


f1=open('new.txt','w+')
f1.write("this is a new file")
f1.seek(10)
print(f1.readlines())
f1.seek(10)
print(f1.readlines())

f1.close()  # close the file
f2= open('new.txt','w+')
f2.seek(44) 
f2.write("this is a new file \n")
print(f2.readlines())
