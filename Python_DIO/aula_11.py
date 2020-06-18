# Except ( Exceção):

#filha = "Sophia"

try:
    print(filha)
except Exception as erro:
    print(f"Falta definir filha.{erro.__class__}")
else:
    print("Formato correto")
finally:
    print("Até logo!")


