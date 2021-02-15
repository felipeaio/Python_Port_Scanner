#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Inserir o host que sera escaneado
remoteServer    = raw_input("Digite o host: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Imprima um banner legal com info sobre qual host estamos prestes a digitalizar
print "-" * 60
print "Aguarde, verificando host remoto", remoteServerIP
print "-" * 60

# Verifica que horas a verificacao comecou
t1 = datetime.now()

# Usando a funcao de intervalo para especificar portas (aqui, ela verifica todas as portas entre 1 e 1024)

# Tambem incluimos algum tratamento de erros para detectar erros

try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Porta {}: 	 Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "Voce pressionou Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Nao foi possivel conectar ao servidor"
    sys.exit()

# Checando a hora de novo
t2 = datetime.now()

# Calcula a diferenca de tempo, para ver quanto tempo levou para executar o script
total =  t2 - t1

# imprimindo as informacoes na tela
print 'Scanning Completed in: ', total
