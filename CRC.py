import random

def xor_function(a,b):
    n = len(a)
    m = len(b)
    if(m!=n):
        if n<m:
            a = "0"*(m-n)+a
        else:
            b = "0"*(n-m)+b
    g=''
    for i in range(n):
        c = int(a[i])
        d = int(b[i])
        f = c^d
        g = g+str(f)
    return g 

def ans(k):
    if(k[0]== '0'):
        p = xor_function(k,'0'*n)
    else:
        p = xor_function(k,divisor)
    return p

def generate_error(x):
    if random.random()<0.5:
        patch=""
        e = random.randint(0,len(x)-1)
        error=int(x[e])^1
        for j in range(len(x)):
            if j==e:
                patch=patch+str(error)
            else:
                patch=patch+str(x[j])
        return patch
    else: 
        return x

def get_rem(div,divisor):
    i = 0
    k = div[i:n]
    l = len(div)
    for i in range(len(div)):
        y = ans(k)
        i = i +len(divisor)
        if(i>=l):
            y = ans(k)
            k=y
            break
        k = y[1:]+div[i]
    rem = k[1:]
    return rem


dividend = input("Enter the dividend: ")
divisor = input("Enter the divisor: ")
n = len(divisor)
div = dividend + (n-1)*'0' 
print(div)
rem = get_rem(div,divisor)
print("Remainder",rem)
trans = dividend+rem
print("Transmitted message ",trans)


sent = generate_error(trans)
# sent = div
print("Message received by reciever",sent)
check = get_rem(sent,divisor)
print("New remainder",check)
if(check =='0'*(n-1)):
    print("No error message received correctly")
else:
    print("Error in message")





	
