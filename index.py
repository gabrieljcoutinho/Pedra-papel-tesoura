import random

opcoes = ["pedra", "papel", "tesoura"]

while True:
    jogador = input("Escolha pedra, papel ou tesoura (ou 'sair'): ").lower()
    if jogador == "sair":
        break
    computador = random.choice(opcoes)  # Escolha aleatória
    print(f"Computador escolheu {computador}")

    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Você venceu!")
    else:
        print("Você perdeu!")
