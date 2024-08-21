a = 0b1100  # 12 in binary
b = 0b1010  # 10 in binary

result_and = a & b
print(f"a & b: {bin(result_and)}") 
result_or = a | b
print(f"a | b: {bin(result_or)}") 
result_xor = a ^ b
print(f"a ^ b: {bin(result_xor)}") 
result_not_a = ~a
print(f"~a: {bin(result_not_a & 0b1011)}") 
result_lshift = a << 2
print(f"a << 2: {bin(result_lshift)}")
result_rshift = a >> 2
print(f"a >> 2: {bin(result_rshift)}")  