# ====================================================
#                  BRUTE FORCE SOLUTION
# ====================================================

# import numpy as np
# import sys

# def next_collatz(n):
#     # print('called')
#     return int(n/2) if (n%2==0) else int(3*n+1)

# if __name__=='__main__':
#     chains = []
#     lengths = []
#     for i in range(1, 1_000_000+1):
#         sys.stdout.flush()
#         sys.stdout.write(f"\r{i}")
        
#         chain = []
#         m = next_collatz(i)
#         chain.append(i)
        
#         while m != 1:
#             chain.append(m)
#             m=next_collatz(m)

#         chain.append(1)
#         chains.append(chain)
#         lengths.append(len(chain))

#     print()
#     print(len(lengths))
#     print('==----------==')
#     print(np.argmax(lengths)+1)
# ====================================================



# ====================================================
#                  OPTIMIZED SOLUTION
# ====================================================

# FUNCTION countChain(n)
#     IF EXISTS(values[n]) THEN
#         RETURN values[n]
#     IF n MOD 2 = 0 THEN
#         values[n] = 1 + countChain(n / 2)
#     ELSE
#         values[n] = 2 + countChain((3 * n + 1) / 2)
#     ENDIF
#   RETURN values[n]
# ENDFUNCTION

# longest_chain <- 0
# answer <- -1
# values <- {1: 1}
# FOR number <- 500000 TO 10^6 - 1
#   IF countChain(number) > longest_chain THEN
#       longest_chain <- countChain(number)
#       answer <- number
#   ENDIF
# ENDFOR
# OUTPUT answer


# The smart idea is to use dictionaries to store all the last seen chains. 
# We store the starting point of the chain as the key of the dictionary 
# therefore making it easy and efficient to check if a specific chain already 
# exists so that we don't have to recalculate it. If the chain starting point is
# not seen then we just add it to the dictionary with the value being 1 + Collatz(n/2) if n is even 
# or 2 + Collatz(n) if it is odd. The reason being that if n is even then Collatz(n) = 1 + Collatz(n/2)
# and Collatz(n/2) is surely calculated. Similarly if n is odd then 3n+1 is even and thus 
# Collatz(n) = 1 + Collatz(3n+1) = 2 + Collatz((3n+1)/2).

def count_chain(n, values):
    if n in values.keys(): return values[n] 

    if (n%2)==0: values[n] = 1 + count_chain(n/2, values)
    else: values[n] = 2 + count_chain((3*n+1)/2, values)
    
    return values[n]


longest_chain = 0
answer = -1
values = {1:1}

for i in range(50000, 1_000_000):
    if count_chain(i, values) > longest_chain:
        longest_chain = count_chain(i, values)
        answer = i

print(answer)
