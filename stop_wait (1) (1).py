import random
def send_packet(packet_num):
    print("____________________________________")
    print(f"Sender: Sending packet {packet_num}")
    return packet_num

def send_ack(ack_num):
    print(f"Receiver: Packet {ack_num} recieved!")
    print(f"Receiver: Sending acknowledgement for packet {ack_num}")

def simulate_stop_and_wait(num_packets):
    packet_num = 1
    successful_transmissions = 0
    while packet_num <= num_packets:
        packet = send_packet(packet_num)
        
        # Simulating delayed acknowledgement
        acknowledgement_received = False
        timer_start = 0
        while not acknowledgement_received:
            if random.random() < 0.3:
                print(f"Receiver: Packet {packet_num} recieved!")
                print(f"Receiver: Sending acknowledgement for packet {packet_num}")
                print("____________________________________")
                print(f"Acknowledgement for packet {packet_num} delayed!")
                print("____________________________________")
                print(f"Sender: Timer expired for packet {packet_num}! Retransmitting...")
                break
            
            if timer_start == 0:
                timer_start = packet_num
            
            if packet_num >= timer_start+2:
                print("____________________________________")
                print(f"Acknowledgement for packet {packet_num} lost!")
                break
            
            # Simulating acknowledgement received
            if random.random() < 0.7:
                send_ack(packet_num)
                successful_transmissions += 1
                print(f"Sender: Acknowledgement for packet {packet_num} received!")
                packet_num += 1
                acknowledgement_received = True
        
        if not acknowledgement_received:
            # Simulating retransmission of packet
            retransmit_successful = False
            retransmission_start = 0
            while not retransmit_successful:
                if random.random() < 0.7:
                    print(f"Sender: Retransmitting packet {packet_num}!")
                    break
                
                if retransmission_start == 0:
                    retransmission_start = packet_num
                
                if packet_num >= retransmission_start + 3:
                    print(f"Sender: Retransmission of packet {packet_num} lost!")
                    break
                
                # Simulating acknowledgement received after retransmission
                if random.random() < 0.5:
                    send_ack(packet_num)
                    successful_transmissions += 1
                    print(f"Receiver: Packet {packet_num} received after retransmission!")
                    packet_num += 1
                    retransmit_successful = True
            
            if not retransmit_successful:
                print(f"Sender: Timer expired for packet {packet_num}! Retransmitting...")
                print(f"Packet {packet_num} lost!")
    
    print(f"Total successful transmissions: {successful_transmissions}/{num_packets}")



# Simulate 10 packets
simulate_stop_and_wait(10)