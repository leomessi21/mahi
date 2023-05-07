import random
def b2d(s1):
    l=len(s1)
    f=0
    sd=""
    for i in range(0,l):
        if(s1[i]=='0' or s1[i]=='1'):
            continue
        else:
            print(s1[i])
            f=1
            break
    if(f==1):
        print("Invalid binary")
    else:
        import math
        f2=8
        f1=0
        while(f2<=l):
            z=s1[f1:f2]
            p=0
            sum=0
            for i in range(7,-1,-1):
                sum+=int(z[i])*(math.pow(2,p))
                p+=1
            sd+=str(int((sum)))+"."
            f1=f2
            f2+=8
        print(sd[0:len(sd)-1])
def main():
    s=""
    for i in range(0,32):
        x=random.random()
        if(x>0.5):
            s+="1"
        else:
            s+="0"
    print(s)
    print(len(s))
    b2d(s)
if __name__=='__main__':
    main()
