import socket
import os
import time

time.sleep(1)
os.system('clear')
time.sleep(1)
os.system('figlet Scanner')
time.sleep(3)

print("""

《=====================Willian==================》

           CRIADOR: WILLIAN DE OLIVEIRA

                 DATA:11/10/2022

           PORTSCANNER - ETHICAL HACKER

           CRIADO PARA FINS DIDATICOS

《====================Willian===================》
""")
time.sleep(7)

time.sleep(1)
os.system('clear')
print("""
AGUARDE
■■20%""")
time.sleep(1)
os.system('clear')
print("""
AGUARDE
■■■■40%""")
time.sleep(1)
os.system('clear')
print("""
AGUARDE
■■■■■■60%""")
time.sleep(1)
os.system('clear')
print("""
AGUARDE
■■■■■■■■80%""")
time.sleep(1)
os.system('clear')
print("""
AGUARDE
■■■■■■■■■■100%""")
time.sleep(2)
os.system('clear')

IP = input('Digite o IP: ')
Ports = [22,80,144,777,8080]
print('22', '80', '144', '777', '8080')

for port in Ports:
         client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         client.settimeout(1.0)
         code = client.connect_ex((IP, port))
         if code == 0:
                 print('Porta aberta')
         else:
                 print('Porta fechada')





