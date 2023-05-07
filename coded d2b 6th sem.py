def d2b(s):
    s=s+"."
    l=len(s)
    f=0
    s1=""
    beg=0
    for i in range(0,l):
        if(s[i]=="."):
            end=i-1;
            s1=s[beg:end+1]
            if(int(s1)<0 or int(s1)>255):
                f=1
                break
            else:
                beg=i+1
    if(f>0):
        print("invalid string",s)
    else:
        beg=0
        s1=""
        for i in range(0,l):
         if(s[i]=="."):
            end=i-1
            n=int(s[beg:end+1])
            sb=""
            while(n!=0):
                r=n%2
                
                n//=2
                sb=str(r)+sb
            print(sb)
            s1+=sb
            beg=i+1
        print(s1)
def b2d(s1):
    l=len(s1)
    print(s1)
    print(len(s1))
    f=0
    sd=""
    for i in range(0,l):
        print(type(s1[i]))
        if((s1[i]==str(0)) or (s1[i]==str(1))):
            print(s1[i],i)
            f=0
            continue
        else:
            f=1
            print(s1[i])
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
    s=input("Enter coded decimal")
    print(s)
    d2b(s)
    b=input("Enter binary")
    if(len(b)!=32):
        print("Invalid entry")
    else:
        b2d(b)
if __name__=='__main__':
    main()
