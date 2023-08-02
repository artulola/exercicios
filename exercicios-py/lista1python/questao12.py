vendidos = int(input("Digite o número de carros vendidos pelo vendedor: "))
valorvendas = float(input("Digite o valor total das vendas do vendedor: "))
salfixo = float(input("Digite o salário fixo do vendedor: "))
valvendidos = float(input("Digite o valor que ele ganha por carros vendidos: "))

salfinal = salfixo + (valvendidos * vendidos) + (valorvendas * 0.05)

print("O salário final do vendedor é: ", salfinal)
