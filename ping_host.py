import ping3 
import os
import asyncio
import time

# Для вывод в консоли используемой системы кодировки используется команда chcp, для русского текста может быть 688 или 1251, для вывода в на латинице используется 65001. При выводе в даной программе лучше использовать кодировку 65001.

# Для получение имени компьютера по ip используется команда nslookup т.е. nslookup 192.168.8.1


start_time = time.time()
def main_chcp():
    print(os.popen('chcp 65001').read()) # Перевод терминала в английский текст

def ping_1(range_address:int):
    for i in range (range_address):
        ip = f'192.168.9.{i}'
        # try:        
        for _ in range(3):
            otvet = ping3.verbose_ping(ip)
            print(f'{ip}:{otvet}')
            if not (otvet == False ):
                break
        # except:
            # res = os.popen(f'ping {ip}').read()
            # print('Ошибка')

def ping_ip(ip:str, res:str = ''):
    res = os.popen(f'ping -w 500 -n 1 {ip}').read()
    list_d = res.split()
    for d in list_d:
        if d == 'TTL=128':
            return True        
    else:
        return False

def host_ip(ip:str):
    os.popen('chcp 866').read() # Перевод терминала в английский текст
    data = os.popen(f'nslookup {ip}').read()
    os.popen('chcp 65001').read() # Перевод терминала в английский текст
    new_data = data.split()
    if len(new_data) == 4:
        return
    else:
        name_host,*_ = new_data[5].split('.')
        return(name_host)

    

def ping_2(range_address:int):
    os.popen('chcp 65001').read() # Перевод терминала в английский текст
    filename = 'ping_adress.txt'
    number = 1
    with open(filename, "w", encoding='utf-8') as f:
        j = 0
        for j in range(12):
            i = 0
            ip = f'192.168.{j}.{i}'
            f.write(f'\n\t-----{ip}-----\n') 
            for i in range (range_address):
                ip = f'192.168.{j}.{i}'
                res =  ping_ip(ip)
                if res:
                    name_host =  host_ip(ip)          
                    text_ip = f'{ip} Имя: {name_host}'
                    f.write(f'№{number} {text_ip}\n')
                    print(f'{text_ip}: Enable')
                    number +=1
                else:
                    print( f'{ip}: Disable')                               
    print(f"Время работы программы {time.time()-start_time:.2f} секунд.")

if __name__ == '__main__':
    # asyncio.run(ping_2(256))
    ping_2(256)    
    # main_chcp()