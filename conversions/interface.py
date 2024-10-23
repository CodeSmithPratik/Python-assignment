import convertor as c
p = int(input("what kind of no u have \n 1 octal \n 2 binary \n 3 decimal \n 4 hexa \n"))

um = input("to which format??\n\n 1 octal \n 2 binary \n 3 decimal \n 4 hexa \n")
if p == 1:
        w = int(input('enter octal no'))  
        c.convert_to_digit(um,p)
elif p == 2:
        w = int(input('enter binary no'))
        c.convert_to_digit(um,p)
   
       
elif p == 3:
        w = int(input('enter decimal no'))
        c.convert_to_digit(um,p)
elif p == 4:
        w = int(input('enter hexa no'))
        c.convert_to_digit(um,p)
else:
        print('invalid input')
        

