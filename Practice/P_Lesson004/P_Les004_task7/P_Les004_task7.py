# Задание №7
# �Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# �Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# �Массив должен быть заполнен случайными целыми числами от 1 до 100.
# �При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# �В каждом решении нужно вывести время выполнения вычислений.
# Погружение в Python

import threading
import time
import os
import random


threads = []
start_time = time.time()


def add_are_rand(arr:list):
    return arr.append(random.randint(1,100))
def are_sum(amount):
    arey = [] 
    for _ in range(amount):
        thread = threading.Thread(args=(arey, add_are_rand(arey)))
        threads.append(thread)
        thread.start()
    print(f'Сумма чисел равняется {sum(arey)}')


are_sum(1000000)
for thread in threads:
    thread.join()
print(f"Загрузка по времени {time.time()-start_time:.2f} секунд.")
# print(sum(ar))
# if __name__ == '__main__':
#     (add_are_rand(10000000))
#     print('Всё!')