import random
def main():
    numeroAle = random.randint(1, 170)

    numero = 0
    i = 0

    while numeroAle != numero:
        numero = int ( input("Digite um número: "))

        if numero > numeroAle:
            print("Seu número é maior")
        elif numero < numeroAle:
            print("O seu número é menor")
        print("\n")
        i += 1
    
    print("Você acertou com ", i)
     
    return 0
main() 