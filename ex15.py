# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

def main():
    celsius = int(input('Digite os graus em Celsius: '))
    fahrenheit = ((9 * celsius) / 5) + 32

    print(f'A temperatura convertida para Fahrenheit é: {fahrenheit}.')

if __name__ == '__main__':
    main()
