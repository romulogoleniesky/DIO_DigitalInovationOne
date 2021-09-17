import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Conexão estabelecida!')
host = "localhost"
porta = 5433
mensagem = "Servidor OK!"

try:
    print('Cliente:' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente' + dados)
finally:
    print("processo ok")
    s.close()
