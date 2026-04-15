#generating the triples
# m > n > 0
# a = m**2 - n**2
# b = 2*m*n 
# c = m**2 + n**2  


for n in range(1, 100):
    for m in range(n, 100):
        a = m**2 - n**2
        b = 2*m*n 
        c = m**2 + n**2  

        if a + b + c == 1000:
            print(f"a={a}, b={b}, c={c}")
            print(a*b*c)

