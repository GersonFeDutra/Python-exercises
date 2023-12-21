# ARP (Adress Resolution Protocol)

## `ip addr`

Get ip address info.

Ex.:

```bash
➜  ~ ip addr                                                                            [1m 26s566]
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp2s0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether 1c:39:47:0b:79:a2 brd ff:ff:ff:ff:ff:ff
3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 94:65:9c:6f:be:5e brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.7/24 brd 192.168.1.255 scope global dynamic noprefixroute wlan0
       valid_lft 3611sec preferred_lft 3611sec
    inet6 2804:29b8:5027:1b2a:f16c:739a:daac:2f69/64 scope global dynamic noprefixroute
       valid_lft 259199sec preferred_lft 172799sec
    inet6 fe80::1ae3:9ae8:ea93:8d1e/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
```

* `2: enp2s0` -> Placa de rede
* `1c:39:47:0b:79:a2` -> Endereço físico da placa


## Criando um pacote ARP

```python
from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp1 # Send-Receive Package 1

#mac_address = '1c:39:47:0b:79:a2' # Ethernet
mac_address = '94:65:9c:6f:be:5e' # Wireless
broadcast = 'ff:ff:ff:ff:ff:ff'

# Permite a conversão do pacote num formato transferível na rede
frame = Ether(src=mac_address, dst=broadcast)

# Endereço de destino
packet = ARP(pdst='192.168.1.1') # pdst = packet destination

final_packet = frame/packet # Construção do pacote

final_packet.show() # Apresentação

```

Saída:

```bash
➜  Laboratório de Redes git:(main) ✗ python 01_arp.py                                                                                         [0s006]
###[ Ethernet ]###
  dst       = ff:ff:ff:ff:ff:ff
  src       = 1c:39:47:0b:79:a2
  type      = ARP
###[ ARP ]###
     hwtype    = Ethernet (10Mb)
     ptype     = IPv4
     hwlen     = None
     plen      = None
     op        = who-has
     hwsrc     = 94:65:9c:6f:be:5e
     psrc      = 192.168.1.7
     hwdst     = 00:00:00:00:00:00
     pdst      = 192.168.1.1

```

* `###[ Ethernet ]###` -> Frame Ethernet
* `type` -> Tipo (ARP)
* `src` -> Endereço físico de remetente

* `###[ ARP ]###` -> Frame ARP
* `op` -> Mensagem (who-has)
* `pdst` -> Packet destination
* `psrc` -> Packet source
* `hwsrc` -> Hardware source

## Pacote final

```python
#answer = srp1(final_packet) # Ethernet
answer = srp1(final_packet, iface='wlan0') # Wireless

answer.show()

```

```bash
[root@nexus Laboratório de Redes]# python 01_arp.py
###[ Ethernet ]###
  dst       = ff:ff:ff:ff:ff:ff
  src       = 1c:39:47:0b:79:a2
  type      = ARP
###[ ARP ]###
     hwtype    = Ethernet (10Mb)
     ptype     = IPv4
     hwlen     = None
     plen      = None
     op        = who-has
     hwsrc     = 94:65:9c:6f:be:5e
     psrc      = 192.168.1.7
     hwdst     = 00:00:00:00:00:00
     pdst      = 192.168.15.1

Begin emission:
Finished sending 1 packets.
.........................................................................................................................................................^C
Received 153 packets, got 0 answers, remaining 1 packets
```

