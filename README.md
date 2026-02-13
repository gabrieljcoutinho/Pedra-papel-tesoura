# Jogo de Pedra, Papel e Tesoura (Jokenpô) em Python

Este projeto é uma implementação do clássico jogo "Pedra, Papel e Tesoura" desenvolvido em Python. O jogador compete contra o computador em um loop contínuo até decidir encerrar a partida.

## Funcionalidades

* **Modo Infinito:** O jogo roda continuamente dentro de um loop `while`, permitindo múltiplas rodadas sem a necessidade de reiniciar o script.
* **IA Aleatória:** O computador faz suas escolhas de forma imprevisível utilizando a biblioteca `random`.
* **Tratamento de Entrada:** O código utiliza o método `.lower()` para garantir que o comando do jogador seja reconhecido independentemente de letras maiúsculas ou minúsculas.
* **Condição de Saída:** O jogador pode encerrar o jogo a qualquer momento digitando o comando "sair".

## Mecânicas de Jogo

As regras de vitória implementadas seguem a lógica tradicional:
* **Pedra** vence Tesoura.
* **Papel** vence Pedra.
* **Tesoura** vence Papel.
* Escolhas iguais resultam em **Empate**.

## Tecnologias Utilizadas

* **Python 3.x:** Linguagem base.
* **Módulo `random`:** Para gerar a escolha aleatória do computador.

## Como Executar

1. Tenha o Python instalado em seu sistema.
2. Salve o código em um arquivo (ex: `jokenpo.py`).
3. Execute o script pelo terminal ou prompt de comando:
   ```bash
   python jokenpo.py
