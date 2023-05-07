def cclass(s):
    l=len(s)
    beg=0
    for i in range(0,l):
        if(s[i]=="."):
            end=i-1
            s1=""
            s1=s[beg:end+1]
            r=int(s1)
            if(r<127):
                print("Class A")
            elif(r>127 and r<=191):
                print("Class B")
            elif(r>191 and r<=223):
                print("Class C")
            elif(r>223 and r<=239):
                print("Class D")
            elif(r>239 and r<=247):
                print("Class E")
            else:
                print("Invallid")
def check(s):
    s+="."
    beg=end=0
    z=""
    f=0
    for i in range(0,len(s)):
        if(s[i]=="."):
            end=i-1
            z=s[beg:end+1]
            if(int(z)>=0 and int(z)<=255):
                beg=i+1
            else:
                f=1
                break
    if(f==0):
        cclass(s)
    else:
        print("Invalid")
def main():
    s=input("Enter coded decimal")
    check(s)
            
if __name__=='__main__':
    main()
    
