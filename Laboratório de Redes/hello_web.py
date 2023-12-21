import scapy.all as scapy
from threading import Timer


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


def scan(ip):
    print(f"[+] Scanning {ip}....")
    arp_request = 
    broadcast = 
    arp_request_broadcast = broadcast/arp_request
    answered_list = 
    client_list = []

    for packet in answered_list:
        client_dict = 
        client_list.append(client_dict)
        print (client_list)
 
#Faça aqui parte do código que dar ao usuário poder de decidir quando parar o script.
subnet = 
timer = RepeatTimer(1.0, scan, [subnet])
timer.start()
