A = int(input("Digite o primeiro valor (A): "))
B = int(input("Digite o segundo valor (B): "))

if (A > B):
    sub = A - B

elif (B > A):
    sub = B - A

else:
    sub = 0

print("Resultado:",sub)