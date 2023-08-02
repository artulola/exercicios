A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

if (A == 0 or B == 0 or C == 0):
    print("Equação incompleta!")

delta = B**2 - 4*A*C
x1 = (-(B) + delta**0.5)/2*A
x2 = (-(B) - delta**0.5)/2*A

if (delta < 0):
    print("Não existe solução real!")

elif(delta > 0):
    print("Existem duas soluções reais e diferentes, sendo elas: ")
    print("x' = ", x1)
    print("x'' = ", x2)

elif(delta == 0):
    print("Há apenas uma solução real, sendo ela: ")
    if (type(x1) == float):
        print("Resultado:", x1)
    else:
        print("Resultado:", x2)
