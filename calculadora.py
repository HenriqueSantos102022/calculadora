def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

if __name__ == "__main__":
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    
    print("Resultado da soma:", soma(x, y))
    print("Resultado da subtração:", subtrai(x, y))