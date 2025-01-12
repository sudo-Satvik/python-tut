# Bitwise operators are used to perform bit-level operations on integers.

'''
&	AND operation	5 & 3 → 1
|	OR operation    5 | 3 → 7
^	XOR (exclusive OR) operation	5 ^ 3 → 6
~	NOT operation (bitwise negation)	~5 → -6
<<	Left shift	5 << 1 → 10
>>	Right shift	5 >> 1 → 2
'''


a = 5       # 101
b = 3       # 011

print(a & b)    # 001
print(a | b)    # 111
print(a ^ b)    # 110
print(~a)       # 010
print(a >> b)
print(a << b)