import psutil
import time
import datetime
import csv

success_cout=0
st_time=time.time()
csv_file = "Success_record.csv"

def calculate_network_usage(interface_name):
    io_counters = psutil.net_io_counters()
    global bytes_sent,bytes_recv

    bytes_sent = io_counters.bytes_sent
    bytes_recv = io_counters.bytes_recv
    time.sleep(1)

    new_io_counters = psutil.net_io_counters(pernic=True)[interface_name]
    new_bytes_sent = new_io_counters.bytes_sent
    new_bytes_recv = new_io_counters.bytes_recv

    sent_per_sec = new_bytes_sent - bytes_sent
    recv_per_sec = new_bytes_recv - bytes_recv

    total_bandwidth = 60 * 8 * (267 + 350)  # 60 秒 x 8 bits/byte x (上傳 + 下載) = 總流量 (bits)
    usage_percent = (sent_per_sec + recv_per_sec) / total_bandwidth * 100
    return usage_percent

count =0
while (time.time()-st_time<60):
    try:

        interface_name = your_interface_name
        network_usage = calculate_network_usage(interface_name)
        cpu_usage = psutil.cpu_percent()
        # print(f'bytes_sent: {bytes_sent}, bytes_recv:{bytes_recv}, network usage: {network_usage}% ,CPU usage: {cpu_usage}%')

        if(network_usage>2700):
            success_cout+=1
            print(f'{datetime.datetime.now()} Nt usage boomm!')
            with open(csv_file, "a",newline='') as f:
                writer = csv.writer(f)
                now = datetime.datetime.now()
                now_time = now.strftime("%H:%M:%S")
                writer.writerow([now_time,network_usage,cpu_usage,success_cout])
            time.sleep(1)
    except KeyboardInterrupt:
        break