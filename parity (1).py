import random
def check_bin(x):
	if int(x)>-1 and int(x)<2:
		return True
	return False

def check_parity(x):
	res=int(x[0])
	for i in range(len(x)-1):
		if check_bin(x[i]):
			res=res^int(x[i+1]) # Xor operation res and integer value of x[i+1]
		else:
			print("Not a binary string!!!")
			exit()
	return res

def transmission(x):
	if option==1:
		if check_parity(x):
			x=x+"1"
		return x+"0"
	else:
		if not(check_parity(x)):
			x=x+"1"
		return x+"0"
	
def generate_error(x):
	# prob=random.random()
	patch=""
	e=random.randint(0,len(x)-1)
	error=int(x[e])^1
	f=random.randint(0,len(x)-1)
	f_error=int(x[f])^1
	for j in range(len(x)):
		if j==e:
			patch=patch+str(error)
		elif j==f:
			patch=patch+str(f_error)
		else:
			patch=patch+str(x[j])
	return patch

def final_check(num,option):
	if option==1:
		if check_parity(num):
			return True
		return False
	else:
		if check_parity(num):
			return False
		return True

num=input("Enter the Message String\n")
option=int(input("To choose Even Parity enter 1 else enter 0\n"))
msg=transmission(num)
print("Transmission Message :",msg)
error=generate_error(msg)
print("Message after effected :",error)
# error=msg
if final_check(error,option):
	print("Message Corrupted!!")
else:
	print("Message is Correct!!")
