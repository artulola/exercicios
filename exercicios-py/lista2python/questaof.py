a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a <= b and a <= c:
    menor = a
    if b <= c:
        meio = b
        maior = c
    else:
        meio = c
        maior = b
elif b <= a and b <= c:
    menor = b
    if a <= c:
        meio = a
        maior = c
    else:
        meio = c
        maior = a
elif c <= b and c <= a:
    menor = c
    if a <= b:
        meio = a
        maior = b
    else:
        meio = b
        maior = a 

print("Ordem crescente: ", menor, meio, maior)