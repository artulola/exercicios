A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))
C = int(input("Digite o terceiro número: "))
D = int(input("Digite o quarto número: "))

print("Verificando números...")

if A % 2 == 0 and A % 3 == 0:
    print(A)
if B % 2 == 0 and B % 3 == 0:
    print(B)
if C % 2 == 0 and C % 3 == 0:
    print(C)
if D % 2 == 0 and D % 3 == 0:
    print(D)

if (A % 2 != 0 or A % 3 != 0) and (B % 2 != 0 or B % 3 != 0) and (C % 2 != 0 or C % 3 != 0) and (D % 2 != 0 or D % 3 != 0):
    print("Nenhum número se encaixa nas condições do programa!")