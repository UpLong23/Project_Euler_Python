from sympy.ntheory.factor_ import divisor_count

def generate_triangle_numbers(n:int) -> int:
    """Generate the n-th triangle number

    Args:
        n (int): the index of the triangle number we want

    Returns:
        int: the triangle number
    """    
    return int((n * (n+1)) / 2)


if __name__=='__main__':
    n=1
    while True:
        tr = generate_triangle_numbers(n)
        n+=1

        if divisor_count(tr) >= 500:
            print(tr)
            break

