# Задание №6
# �Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить результаты в консоль.
# �Используйте асинхронный подход.

import asyncio
import threading
import time
import os
from multiprocessing import Process, Pool


adress =    [r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Flask\Practice\P_Lesson004\P_Les004_task4\text.txt',
            r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Flask\Practice\P_Lesson004\P_Les004_task4\text1.txt',
            r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Flask\Practice\P_Lesson004\P_Les004_task4\text2.txt']


threads = []
start_time = time.time()


async def count_words(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f: 
                text = f.read()
                words = text.split()
                *_, a = file_name.split('\\')
                print(f'В файле {a} количество слов : {len(words)}')
    except :
        *_, a = file_name.split('\\')
        print(f'Ошибка чтения файла {a}')


async def count_direct_mul(directoty):
    for root, dirs, files in os.walk(directoty):
        for file in files:
            file_name = os.path.join(root, file)
            await count_words(file_name) #target=print,

          



if __name__ == '__main__':
    asyncio.run(count_direct_mul(r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Flask\Practice\P_Lesson004'))

    print(f"Загрузка по времени {time.time()-start_time:.2f} секунд.")