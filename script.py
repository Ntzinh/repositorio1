import random

def jogar_dado():
    input("Pressione Enter para jogar o dado...")
    resultado = random.randint(1, 6)
    print("Você jogou o dado e obteve:", resultado)

# Chamar a função para jogar o dado
jogar_dado()