N1 = float(input("Digite a nota do primeiro bimestre: "))
N2 = float(input("Digite a nota do segundo bimestre: "))
N3 = float(input("Digite a nota do terceiro bimestre: "))
N4 = float(input("Digite a nota do quarto bimestre: "))

MD = (N1+N2+N3+N4)/4

if (MD >= 7):
    print("Aprovado!")
    print("Média final: ", MD)
else:
    NE = float(input("Digite a nota do exame: "))
    MD2 = (MD+NE)/2

    if(MD2 >= 5):
        print("Aprovado em exame!")
        print("Média final: ", MD2)
    else:
        print("Reprovado!")
        print("Média final: ", MD2)
   

