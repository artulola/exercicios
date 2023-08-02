salmes = float(input("Digite o valor do seu salário mensal: "))
reaj = float(input("Digite a porcentagem de reajuste salarial: "))

novosalario = (salmes * (reaj/100)) + salmes

print("Novo salário: ", novosalario)