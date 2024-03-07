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
import asyncio


start_time = time.time()

async def aradd(arr:list):
    return arr.append(random.randint(1,10))

async def are_sum(amount):
    arey = [] 
    for _ in range(amount):
        await  aradd(arey)
    print('Массив заполнен')
    num = sum(arey)        
    print(f'Сумма чисел равняется {num}')
    return(num)



if __name__ == '__main__':
    ar = []
    for _ in range(10):
        start_time = time.time()
        new_num = asyncio.run(are_sum(10000000))
        print(f"Загрузка по времени {time.time()-start_time:.2f} секунд.")
        ar.append(new_num)
    num_min = min(ar)
    max_num = max(ar)
    sum_num = sum(ar)
    dev_sum = sum_num/10
    num_ras_min = abs(dev_sum - num_min)
    num_ras_max = abs(dev_sum - max_num)
    print(f'Среднее значение из 10 равняется {dev_sum}, разброс от минимального {num_ras_min} разброс от максимального {num_ras_max}')
    