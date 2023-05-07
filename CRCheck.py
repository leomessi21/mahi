import random

dividend = input("Enter the dividend: ")
divisor = input("Enter the divisor: ")

n = len(divisor)

div = dividend + (n-1)*'0' 

k=0


def xor_function(a,b):
    global n
    g=''
    for i in range(n):
        c = int(a[i])
        d = int(b[i])

        f = c^d
        g = g+str(f)
    return g  


def finding_bits(r):
    global k
    global n
    a=''
    for i in range(n):
        if r[i]=='0':
            pass
        elif r[i]=='1':
            a=r[i::]
            break

   
    while(len(a)!=n and k<len(div)):
        a = a+div[k]
        k=k+1 
           
    return a


 
dividing_bits = finding_bits((n*'0'))


while(k!=len(div)):
    res = xor_function(dividing_bits,divisor)
    dividing_bits = finding_bits(res)

remainder = dividing_bits
message = dividend + (n-1-len(remainder))*'0' + remainder
print("Message will be sent as ",message)
