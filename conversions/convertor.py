#have to make a module for digit conversion
def convert_to_digit(um,num):
    if um==1:
        def bina(num):
            print(bin(num))
 
    elif um==2:
        def octa(num):
            print(int(num))
    elif um==3:
       def deca(num):
            print(dec(num))
    elif um==4:
       def hexa(num):
            print(bin(num))   
    else:
        print("invalid input")
     