# bitwise_operators.py

a = 10  # Binary: 1010
b = 4   # Binary: 0100

print("Bitwise AND:", a & b)   # Output: 0
# Performs a bitwise AND operation between a and b.
# Binary: 1010 & 0100 = 0000, which is 0 in decimal.

print("Bitwise OR:", a | b)    # Output: 14
# Performs a bitwise OR operation between a and b.
# Binary: 1010 | 0100 = 1110, which is 14 in decimal.

print("Bitwise XOR:", a ^ b)   # Output: 14
# Performs a bitwise XOR operation between a and b.
# Binary: 1010 ^ 0100 = 1110, which is 14 in decimal.

print("Bitwise NOT (~a):", ~a) # Output: -11
# Performs a bitwise NOT operation on a.
# Binary: ~1010 = -(1010 + 1) = -1011, which is -11 in decimal.

print("Bitwise LEFT SHIFT:", a << 2)  # Output: 40
# Performs a left shift operation on a by 2 positions.
# Binary: 1010 << 2 = 101000, which is 40 in decimal.

print("Bitwise RIGHT SHIFT:", a >> 2) # Output: 2
# Performs a right shift operation on a by 2 positions.
# Binary: 1010 >> 2 = 0010, which is 2 in decimal.
