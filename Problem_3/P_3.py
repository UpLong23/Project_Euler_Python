i, j = 100, 100
l=[]
for i in range(100,1000):
    for j in range(100,1000):
        l_1 = list(str(i*j))
        l_2 = list(reversed(l_1))
        if l_1== l_2:
           l.append(i*j)
print(max(l))

    
