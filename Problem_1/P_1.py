l=[]
s=0
for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        l.append(i)
for i in l:
    s += i
print(s)
        
