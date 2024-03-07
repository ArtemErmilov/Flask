# Задание №4
# �Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить результаты в консоль.
# �Используйте потоки.

# Загрузка в 5 потоков с использованием модуля threading:

import threading
import time
import os
adress =    [r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Flask\Practice\P_Lesson004\P_Les004_task4\text.txt',
            r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Flask\Practice\P_Lesson004\P_Les004_task4\text1.txt',
            r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Flask\Practice\P_Lesson004\P_Les004_task4\text2.txt']


threads = []
start_time = time.time()

def reading_words(adres:str):
    
    for _ in range (1):
        try:
            with open(adres, 'r', encoding='utf-8') as f: 
                text = f.read()
                len_d = len(text.split())
                break
        except UnicodeDecodeError as a:
            continue
    *_, a = adres.split('\\')
    print(f"Количество слов {len_d}. Обработка Файла {a} in {time.time()-start_time:.2f} seconds")

def count_words(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f: 
                text = f.read()
                words = text.split()
                *_, a = file_name.split('\\')
                print(f'В файле {a} количество слов : {len(words)}')
    except :
        *_, a = file_name.split('\\')
        print(f'Ошибка чтения файла {a}')


def count_direct(directoty):
    for root, dirs, files in os.walk(directoty):
        for file in files:
            file_name = os.path.join(root, file)
            thread = threading.Thread(args=(file_name, count_words(file_name)))
            threads.append(thread)
            thread.start()


count_direct(r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Flask\Practice\P_Lesson004')

for thread in threads:
    thread.join()
print(f"Загрузка по времени {time.time()-start_time:.2f} секунд.")

# if __name__ == '__main__':
#     adress = r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Flask\Practice\P_Lesson004\P_Les004_task4\text1.txt'
#     reading_words(adress)