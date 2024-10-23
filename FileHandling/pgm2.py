with open('test.txt','w')as file1, open('test.txt','a') as file2:
    file1.write("This is the write command")
    file1.write("It allows us to write in a particular file")

    file = open('test.txt','a')
    file2.write("This will add this line")
    print
    file2.close()
