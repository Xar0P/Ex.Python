# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade 
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 
# por Km rodado.

def main():
    quant_dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
    quant_km = float(input('Digite a quantidade de KMs percorridos: '))

    preco = (quant_dias * 60) + (quant_km * 0.15)

    print(f'O preço a pagar é: {preco}')

if __name__ == '__main__':
    main()