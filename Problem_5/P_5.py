
    # Python Program to find the L.C.M. of two input number

def lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 11
num2 = 12
num3 = 13
num4 = 14
num5 = 15
num6 = 16
num7 = 17
num8 = 18
num9 = 19
num10 = 20
num = 2520

print(lcm(num,lcm(num1,lcm(num2,lcm(num3,lcm(num4,lcm(num5,lcm(num6,lcm(num7,lcm(num8,lcm(num9,num10)))))))))))


