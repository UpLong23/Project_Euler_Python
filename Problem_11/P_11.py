import numpy as np
from typing import Literal, Union, Tuple
from rich import print

l = []
with open('./Problem_11/data.txt', encoding='utf-8') as file: 
    for line in file:
        l.append([int(s) for s in line.split()])
m = np.array(l)

if __name__=='__main__':
    print(f'[chartreuse2 dim]{m}[chartreuse2 dim]')
    rows, columns = m.shape # rows = columns = 20
    # print(adjacent_numbers(m, 'diagonal', 4, [1,2]))

    downs     = []
    rights    = []
    diagonals = []
    anti      = []

    for i in range(rows):
        for j in range(columns):
            # down
            if i <= rows - 4:
                downs.append(np.prod(m[i:i+4, j]))
            # right  
            if j <= columns - 4:
                rights.append(np.prod(m[i, j:j+4]))
            # down-right diag
            if i <= rows - 4 and j <= columns - 4:
                diagonals.append(np.prod(m[i:i+4, j:j+4].diagonal()))
            # down-left anti-diag
            if i <= rows - 4 and j >= 3:
                anti.append(np.prod(np.diag(np.fliplr(m[i:i+4, j-3:j+1]))))
                # or manual: m[i,j] * m[i+1,j-1] * m[i+2,j-2] * m[i+3,j-3]


    max_downs = max([np.prod(s) for s in downs])
    max_rights = max([np.prod(s) for s in rights])
    max_diagonals = max([np.prod(s) for s in diagonals])
    max_anti = max([np.prod(s) for s in anti])

    print(max(max_downs, max_rights, max_diagonals, max_anti))
                    

            



