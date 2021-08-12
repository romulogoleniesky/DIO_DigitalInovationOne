import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Conexão criado com sucesso!')
host = "localhost"
porta = 5432

s.bind((host, porta))
mensagem = "Olá cliente!"

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)
