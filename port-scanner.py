GNU nano 6.2                                        meu_scanner.py                                        Modified
import socket
import os
import time

time. sleep(3)
os.system('clear')
time.sleep(1)

print("""
●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●

> BEM VINDO HA MAIS UMA EXCELENTE
FERRAMENTA PORT-SCANNER

> DESENVOLVIDO POR WILLIAN DE OLIVEIRA

> 31/03/2022

> PROIBIDO O MAU USO DA FERRAMENTA

●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
""")

time.sleep(12)
os.system('clear')

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

print('INICIANDO VARREDURA')

time.sleep(5)

ports = [21,22,80,443,8080,8483]

for port in ports:
         client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         client.settimeout(0.1)
         code = client.connect_ex(("bancocn.com", port))
         if code == 0:
                 print('Porta Aberta')
         else:
                 print('Porta Fechada')
