class Elevador:

    def __init__(self, andarAtual, totalAndares, capacidadePessoas, pessoasPresentes):
        self.__andarAtual = andarAtual
        self.__totalAndares = totalAndares
        self.__capacidadePessoas = capacidadePessoas
        self.__pessoasPresentes = pessoasPresentes

    def inicializar(self):
        print('Inicializando elevador: ')
        print(f'Capacidade de pessoas: {self.__capacidadePessoas}     Total de andares: {self.__totalAndares}')

    def entrar(self):
        if self.__pessoasPresentes < self.__capacidadePessoas:
            self.__pessoasPresentes += 1
        else:
            print(f'O elevador atingiu sua capacidade total, não é mais possível entrar.')

    def sair(self):
        if self.__pessoasPresentes == 0:
            print('Não tem ninguém no elevador.')
        else:
            self.__pessoasPresentes -= 1
    
    def subir(self):
        if self.__andarAtual <= self.__totalAndares:
            self.__andarAtual += 1
        else:
            print('Você já está no último andar')

    def descer(self):
        if self.__andarAtual == 0:
            print('Você está no térreo, impossível descer;')
        else:
            self.__andarAtual -= 1