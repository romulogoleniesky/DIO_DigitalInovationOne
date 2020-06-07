# GERAR , COPIAR, MOVER, ECREVER E LER INFORMAÇÕES DE ARQUIVOS EXTERNOS.

#CRIANDO ARQUIVO:
#open('FOLHA.txt', 'w')

# TRANSFORMANDO O ARQUIVO EM UM OBJETO, E ESCREVENDO NELE:
# arquivo = open('FOLHA.txt', 'w')
# arquivo.write('Primeira Linha \n')
# Quebra de linha : \n

# ATUALIZANDO DADOS JÁ INSERIDOS:
# arquivo = open('FOLHA.txt', 'a')
# arquivo.write('Nova linha!')

# # MANIPULANDO O ARQUIVO ATRAVÉS DE MÉTODO:
# def escrever_arquivo(texto):
#     arquivo = open('FOLHA.txt', 'w')
#     arquivo.write(texto)
#     arquivo.close()
#
# def atualizar_arquivo(texto):
#     arquivo = open('FOLHA.txt', 'a')
#     arquivo.write(texto)
#     arquivo.close()
#
# def ler_arquivo(nome_arquivo):
#     arquivo = open(nome_arquivo, 'r')
#     texto = arquivo.read()
#     print(texto)
#
# if __name__=='__main__':
#     # escrever_arquivo('Primeiro Linha.\n')
#     # atualizar_arquivo('Segunda Linha. \n')
#     ler_arquivo('FOLHA.txt')



