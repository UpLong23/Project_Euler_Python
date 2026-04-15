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
