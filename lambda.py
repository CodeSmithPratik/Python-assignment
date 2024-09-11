#lambda function

find_max =lambda x,y,z:(x if (x>y and x>z)else y if y >z else z)
print(f"Maximum out of the numbers u entered is {find_max(10,20,30)}") # Output: 30
findMin = lambda x,y,z :(x if (x<y and x<z)else y if y <z else z)
print(f"Minimum out of the numbers u entered is {findMin(10,20,30)}") # Output: 10


#ArithMatic Operations using lambda function

add =lambda a,b:a+b
print(f"addition of the no u enteredis {add(5,7)}")  # Output: 12

sub = lambda a,b : a-b
print(f"Sub of numbers is {sub(5,7)}")  # Output: -2


mul = lambda a,b : a*b
print(f"mul of numbers is {sub(5,7)}") 

div = lambda a,b : a/b
print(f"Div of numbers is {div(5,7)}")


