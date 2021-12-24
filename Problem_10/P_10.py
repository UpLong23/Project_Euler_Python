from timeit import default_timer
start= default_timer()

s=0
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for i in range(2,2*10**6):
    if isPrime(i): s+=i
print(s)
print("Time: " + str(default_timer()-start))
