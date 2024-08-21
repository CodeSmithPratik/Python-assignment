numbers = [1, 2,    3, 4, 5]
for num in numbers:
    if num == 3:
        break #break
    print(num)

# 1
# 2
for num in range(1, 6):
    if num % 2 == 0:
        continue
    print(num)
# 1
# 3
# 5

def my_function():
    pass  # pass *does nothing
