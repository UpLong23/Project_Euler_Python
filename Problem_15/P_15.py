from math import factorial
def count_paths(n):
    """Count the paths from top-left to right-bottom corner
    of an n*n grid. 

    Args:
        n (int): dimension of the grid
    """    
    return int(factorial(2*n) / (factorial(n)**2))

if __name__=='__main__': 
    print(count_paths(20))