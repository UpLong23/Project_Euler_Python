from sympy.ntheory.factor_ import smoothness, factorint

"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""
# print(smoothness(600851475143))

print(factorint(600851475143, verbose=True))