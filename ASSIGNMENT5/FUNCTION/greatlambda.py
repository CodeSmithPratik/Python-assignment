
find_max = lambda x, y, z: (x if (x > y and x > z) else y if y > z else z)

num1 = 14
num2 = 15
num3 = 16

result = find_max(num1, num2, num3)

print("Maximum number is:", result)
