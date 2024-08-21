d = {'a': 1, 'b': 2}
value = d.setdefault('c', 3)
print(value) 
print(d)


 # Output: 3
  # Output: {'a': 1, 'b': 2, 'c': 3}
