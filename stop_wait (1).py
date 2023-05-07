import random

def sender(num,flag):
	print("Packet",num,"Sent Successfully!")
	print("Timer Started!")
	print("---------------------")
	if flag:
		check=reciever(num)
		if check:
			print("Acknowledgement Recieved!")
			if num<10:
				print("Sending next Packet!")
	return True

def reciever(num):
	print("Packet",num,"Recieved!")
	print("Acknowledgement Sent!")
	print("---------------------")
	return True

def error(num):
	flag=False
	sender(num,flag)
	print("Packet arrived corrupted!,Packet Discarded!!")
	print("---------------------")
	print("Time Out!")
	print("Retransmitting Packet",num)
	sender(num,True)

prob=random.randint(0,10)
for i in range(10):
	if i==prob:
		error(i+1)
	else:
		sender(i+1,True)