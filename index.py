import requests
import time
from threading import Thread

f = open("ips.txt","w")

def checkIPs(ip):
    try:
        rq = requests.get(f'http://{ip}/', timeout=1)
        if (rq.text.find("<title>Web Control</title>") != -1):
            print(f'http://{ip}/')
            f.write(f'http://{ip}/\n')
    except:
        pass

def loop(start):
    print(f'Starting loop {start}')
    for b in range(1, 255):
        Thread(target=checkIPs, args=(f'10.14.{start}.{b}',)).start()

if __name__ == "__main__":

    threads = list()
    for index in range(127,256):
        x = Thread(target=loop, args=(index,))
        threads.append(x)

    for i in threads:
        i.start()
