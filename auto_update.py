import os
import subprocess
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 8080))

subprocess.run(['nohup', 'python3', 'main.py', '>', 'nohup.out'])

while True:
    data, addr = sock.recvfrom(4096)
    data = data.decode()
    if data.isdigit():
        bot_pid = data
    elif data == "update":
        print("Wait for bot off")
        time.sleep(1)
        os.popen('git reset --hard HEAD')
        os.popen("git pull github master")
        time.sleep(5)
        subprocess.run(['nohup', 'python3', 'main.py', '>', 'nohup.out'])
        del bot_pid
