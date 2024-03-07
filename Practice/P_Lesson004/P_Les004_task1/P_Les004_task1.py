# Задание №1
# �Написать программу, которая считывает список из 10 URL-адресов и одновременно загружает данные с каждого адреса.
# �После загрузки данных нужно записать их в отдельные файлы.
# �Используйте потоки.

# Загрузка в 5 потоков с использованием модуля threading:
import requests
import threading
import time
urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://www.ozon.ru/',
        'https://www.avito.ru/',
        'https://owen.ru/product/',
        'https://www.wildberries.ru/'                        
        ]
def download(url):
    response = requests.get(url)
    filename = 'Practice\P_Lesson004\P_Les004_task1/'+'threading_' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html' 
    with open(filename, "w", encoding='utf-8') as f: 
        f.write(response.text)
    print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")

threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print(f"Downloaded in {time.time()-start_time:.2f} seconds")