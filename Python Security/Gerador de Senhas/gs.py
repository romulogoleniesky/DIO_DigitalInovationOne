import random, string

tamanho = 16
char = string.ascii_letters + string.digits + '!@#$%&*()'
rnd = random.SystemRandom()
print("".join(rnd.choice(char)for i in range (tamanho)))
