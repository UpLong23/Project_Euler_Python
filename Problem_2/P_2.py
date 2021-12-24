f_n = [1,2]
s=0
while f_n[-1]+f_n[-2] <= 4000000:
    f_n.append(f_n[-1]+f_n[-2])
for i in f_n:
    if i%2==0:
        s += i
print(s)
