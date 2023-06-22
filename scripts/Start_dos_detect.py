import subprocess
import time
import csv
import random
import datetime

count=0
while count<200:
    st_date=datetime.datetime.now()
    st_time = st_date.strftime("%H:%M:%S")
    print(f'Starting detect attack.')
    proce_1=subprocess.Popen("python detect_attack_dos.py",shell=True)
    print(f'Starting catch usage and check success rate.')
    proce_2=subprocess.Popen("python network_usage.py",shell=True)

    proce_1.wait()
    proce_2.wait()
    print(f'****************************')
    print(f'**************Round {count} end**************')
    print(f'****************************')
    count+=1
    