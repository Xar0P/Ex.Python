# Gerar um número de 1 a 100, e solicitar para que o usuário tente adivinhar o número.

import random

num_rand = random.randint(1,100)
num_user = int(input('Digite o número: '))

msg_acerto = 'Eita, você acertou o número, boaa!!'
msg_erro = f'Puts você errou, seu número escolhido foi {num_user} e o número correto é {num_rand}.'

print(msg_acerto if num_rand == num_user else msg_erro)