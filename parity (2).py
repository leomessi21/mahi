import random
original = input("Enter the message to be sent: ")
n = len(original)

count=0
for i in range(n):
    if(original[i]=='1'):
        count+=1

ch = input("Enter the even parity(e) or odd parity(o): ")

if (ch=="e"):
    if (count%2==0):
        message = original+'0'
    else:
        message = original+'1'
if (ch=="o"):
    if (count%2==0):
        message = original+'1'
    else:
        message = original+'0'

print("Message will be sent as ", message)


def error(x):
    change_in = random.randint(0,len(x)-1)
    
    result = ''
    for i in range(len(x)):
        if (i!=change_in):
            result=result + x[i]
        else:
            if x[i]=='1':
                result = result + '0'
            else:
                result = result + '1'

    return result


choice = input("Enter y for error and n for error free: ")
if (choice=='y'):
    final = error(message)
else:
    final = message

print("Message received as ",final)
def check(x):
    global ch
    c = 0
    for i in range(len(x)):
        if(x[i]=='1'):
            c=c+1
    if (ch=='e'):
        if (c%2==0):
            print("Error free")
        else:
            print("There was an error")
    elif (ch=='o'):
        if (c%2==0):
            print ("There was an error")
        else:
            print ("Error free")

check(final)
            







    
