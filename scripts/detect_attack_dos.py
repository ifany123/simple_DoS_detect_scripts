import time
from scapy.all import *
import csv

count = 0  # 接收到的封包數量
start_time = 0  # 開始時間
flag=False
attack_count=0
stime = time.time()
tcp_start_time=time.time()
TCP_count=0

def count_packets(pkt):
    global start_time, count,flag,attack_count,TCP_count,tcp_start_time
    if IP in pkt and (UDP in pkt or TCP in pkt):
        if start_time == 0:
            start_time = time.time()
        if tcp_start_time == 0:
            tcp_start_time = time.time()
        count += 1
        if TCP in pkt and len(pkt[TCP].payload)>1000: TCP_count+=1
        elapsed_time = time.time() - start_time 
        el_time_TCP=time.time() - tcp_start_time
        if count >= 15000:
            attack_count+=1
            flag=True
              
        if flag:
            print(f'We got {count} udp+tcp packets.')
            print(f"Alert: DoS attack from {pkt[IP].src}")
            with open('Detect_record.csv', "a",newline='') as f:
                writer = csv.writer(f)
                now = time.time()
                local_time = time.localtime(now)
                now_time = time.strftime("%H:%M:%S",local_time)
                writer.writerow([now_time,(str)(count),(str)(attack_count)])
            flag=False
            count = 0
            start_time = 0
        
        if el_time_TCP>=3:
            # print(f'got {TCP_count} of TCP packet.')
            TCP_count=0
            tcp_start_time=0
        if elapsed_time >= 10:
            # print(f'We got {count} udp+tcp packets, safe envir.')
            count = 0
            start_time = 0

# print(f'start detect.')
sniff(iface="your_interface_name", prn=count_packets,timeout=60)
