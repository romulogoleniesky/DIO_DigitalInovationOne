# AULA 11 - EXCEPTS - FAZENDO UMA EXCEÇÃO PERSONALIZADA:
# Lista de exceções do Python:
# link : https://docs.python.org/2/library/exceptions.html#exception-hierarchy

class Error(Exception): #classe de erro de exceção.
    pass #conteúdo qualquer!
class InputError(Error): # criado classe Erro de entrada que herda da clase erro.
    def ___init__(self, message):
        self.message = message
while True: #loop para avaliar a tentativa.
    try:
        x = int(input(" Entre com uma nota de 0 a 10 : "))
        print(x)
        if x > 10:
            raise InputError ('Nota não pode ser maior que 10.')
        # RAISE : forçar uma solução para a exceção.
        elif x < 0:
            raise InputError ('Nota não pode ser menor que zero!')
        break # Para a exceção:
    except ValueError:
        print("Valor inválido!")
    except InputError as ex:
        print(f'O erro foi: {ex} !')

