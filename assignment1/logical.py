a = True
b = False
c = True

result_and = a and b
print(f"a and b: {result_and}") 
result_or = a or b
print(f"a or b: {result_or}")  
result_not_a = not a
print(f"not a: {result_not_a}")  
result_not_b = not b
print(f"not b: {result_not_b}")  
result_combined = (a and b) or (not c)
print(f"(a and b) or (not c): {result_combined}")  

x = 5
y = 10
z = 15

result_comparison_and = (x < y) and (y < z)
print(f"(x < y) and (y < z): {result_comparison_and}")  
result_comparison_or = (x > y) or (y < z)
print(f"(x > y) or (y < z): {result_comparison_or}") 
result_comparison_not = not (x > y)
print(f"not (x > y): {result_comparison_not}")  
