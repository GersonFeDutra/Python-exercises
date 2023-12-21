'''
ARP (Adress Resolution Protocol)

Mensagem: Who has 192.168.1.1
'''
from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp1 # Send-Receive Package 1

#MAC_ADDRESS = '1c:39:47:0b:79:a2' # Ethernet
MAC_ADDRESS = '94:65:9c:6f:be:5e' # Wireless
BROADCAST = 'ff:ff:ff:ff:ff:ff'
SERVER_IP = '192.168.1.1'

# Permite a conversão do pacote num formato transferível na rede
frame = Ether(src=MAC_ADDRESS, dst=BROADCAST) # Frame Ethernet

packet = ARP(pdst=SERVER_IP) # ARP packet: pdst = packet destination

final_packet = frame/packet
final_packet.show()

#answer = srp1(final_packet) # Ethernet
answer = srp1(final_packet, iface='wlan0') # Wireless
answer.show()


#import scapy.all as scapy
#from threading import Timer
#
#
#class RepeatTimer(Timer):
#    def run(self):
#        while not self.finished.wait(self.interval):
#            self.function(*self.args, **self.kwargs)
#
#
#def scan(ip):
#    print(f"[+] Scanning {ip}....")
#    arp_request = 
#    BROADCAST = 
#    arp_request_BROADCAST = broadcast/arp_request
#    answered_list = 
#    client_list = []
#
#    for packet in answered_list:
#        client_dict = 
#        client_list.append(client_dict)
#        print (client_list)
# 
##Faça aqui parte do código que dar ao usuário poder de decidir quando parar o script.
#subnet = 
#timer = RepeatTimer(1.0, scan, [subnet])
#timer.start()

