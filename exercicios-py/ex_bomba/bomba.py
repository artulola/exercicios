class BombaCombustivel:

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
         self.tipoCombustivel = tipoCombustivel
         self.valorLitro = valorLitro
         self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valorDesejadoReais):
         litrosAbastecidos = valorDesejadoReais/self.valorLitro
         if litrosAbastecidos <= self.quantidadeCombustivel:
              self.quantidadeCombustivel -= litrosAbastecidos
              print(f"Carro abastecido com {litrosAbastecidos} litros de combustível!")
         else:
              print("Quantidade de combustível na bomba insuficiente.")

    
    def abastecerPorLitro(self, valorDesejadoLitros):
         litrosAbastecidos = valorDesejadoLitros * self.valorLitro
         if litrosAbastecidos <= self.quantidadeCombustivel:
              self.quantidadeCombustivel -= litrosAbastecidos
              print(f"Carro abastecido com {litrosAbastecidos} litros de combustível")
         else:
              print("Quantidade de combustível na bomba insuficiente.")

    
    def alterarValor(self, novoValor):
         self.valorLitro = novoValor
         print(f"Valor Alterado! Novo valor: {self.valorLitro}")

    def alterarCombustivel(self, novoTipo):
         self.tipoCombustivel = novoTipo
         print(f"Tipo de combustível alterado! Novo tipo: {self.tipoCombustivel}")
    
    def alterarQuantidadeCombustivel(self, novaQuantidade):
         self.quantidadeCombustivel = novaQuantidade
         print(f"Quantidade de combustível alterada! Nova quantidade: {self.quantidadeCombustivel}")


bomba = BombaCombustivel('Gasolina comum', 5.47, quantidadeCombustivel= float(input('Digite a quantidade de combustível disponível na bomba: ')))

print('\n----CONFIGURAÇÃO BOMBA DE COMBUSTÍVEL----\n')
print(f'Tipos de combustível da bomba: {bomba.tipoCombustivel}\nPreço do litro: {bomba.valorLitro}\nQuantidade de combustível disponível: {bomba.quantidadeCombustivel}')

print('Selecione a opção desejada:')

opc = int(input("\n1 - Abastecer por valor;\n2 - Abastecer por litro;\n3 - Alterar o valor do combustível;\n4 - Alterar o tipo do combustível;\n5- Alterar a quantidade de combustível disponível na bomba.\n"))

if(opc == 1):
    bomba.abastecerPorValor(valorDesejadoReais = float(input("Digite o valor: ")))
elif(opc == 2):
    bomba.abastecerPorLitro(valorDesejadoLitros = float(input("Digite a quantidade de litros: ")))
elif(opc == 3):
    bomba.alterarValor(novoValor = float(input("Digite um novo valor para o litro: ")))
elif(opc == 4):
    bomba.alterarCombustivel(novoTipo = str(input("Digite o novo tipo de combustivel: ")))
elif(opc == 5):
    bomba.alterarQuantidadeCombustivel(novaQuantidade = float(input("Digite a nova quantidade de combustivel: ")))


