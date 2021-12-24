l = []
b = True
n=2

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

while b:
    if isPrime(n):
        l.append(n)
    n+=1
    if len(l)==10001:
        b=False
print(l[-1])

