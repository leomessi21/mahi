import random
def sender(num,probability):
	def Event_One(num):
		print("Packet",num,"Sent Successfully!")
		print("Timer Started!")
	def Event_Two(num):
		print("Acknowledgement for ",num,"Recieved!")
		print("Sending Next Packet!")
		Event_One(num)
	def Event_Three(num):
		print("Timer Out! for Packet",num)
		print("Retransmitting Packet")
		Event_One(num)

	if probability<0.33:
		Event_One(num)
	elif probability<0.66:
		Event_Two(num)
	else:
		Event_Three(num)

def reciever(num,probability):
	def Event_One(num):
		print("Packet",num,"Recieved!")
		print("Acknowledgement for ", num," Sent!")
	def Event_Two(num):
		print("Packet arrived corrupted!, Discarded!")
	def Event_Three(num):
		print("Duplicate Packet arrived!,Discarded!")
		print("Acknowledgement for Packet",num," Resent!")

	if probability<0.33:
		Event_One(num)
	elif probability<0.66:
		Event_Two(num)
	else:
		Event_Three(num)

probability=random.random()
num=1
sender(num,probability)
reciever(num,probability)