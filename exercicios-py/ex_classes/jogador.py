class Jogador:

    def __init__(self, nome, posicao, nascimento, nacionalidade, altura, peso):
        self.nome = nome
        self.posicao = posicao
        self.nascimento = nascimento
        self.nacionalidade = nacionalidade
        self.altura = altura
        self.peso = peso

    def imprimirDados(self):
        print("INFORMAÇÕES JOGADOR")
        print(f'Nome: {self.nome}\nPosição: {self.posicao}\nAno de nascimento: {self.nascimento}\nNacionalidade: {self.nacionalidade}\nAltura: {self.altura}Peso: {self.peso}')

    def calcularIdade(self):
        idade = 2023 - self.nascimento
        print(f'O jogador possui aproximadamente {idade} anos')

    def tempoParaAposentar(self):
        idade = 2023 - self.nascimento
        if idade <= 40:
            if self.posicao == 'def':
                print(f'Faltam, aproximadamente, {40 - idade} anos para o jogador aposentar.')
            elif self.posicao == 'mei':
                print(f'Faltam, aproximadamente, {38 - idade} anos para o jogador aposentar.')
            elif self.posicao == 'ata':
                print(f'Faltam, aproximadamente, {35 - idade} anos para o jogador aposentar.')
        else:
            print('O jogador vai aposentar, ou, provavelmente já está aposentado.')
            