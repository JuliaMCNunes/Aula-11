from Class_Estoque import *

class Gerenciador:
    def __init__(self):
        self.movimentacao = []
        self.entrada_p = []
        self.saida_p = []
        self.gerenciar = Estoque()
        
    def entrada(self):
        cont = 0
        abast = input('\nInforme o código do produto: ')
        for i in range(len(self.gerenciar.lista_produtos)):
            if self.gerenciar.lista_produtos[i].cod == abast:
                en = int(input('Informe a quantidade do produto: '))
                self.gerenciar.lista_produtos[i].quantidade += en
                self.movimentacao.append(f'Entrada de {en} unidades do produto ' + self.gerenciar.lista_produtos[i].cod)
                self.entrada_p.append(f'Entrada de {en} unidades do produto ' + self.gerenciar.lista_produtos[i].cod)
            else:
                cont += 1
                if cont == len(self.gerenciar.lista_produtos):
                    print('Código não encontrado!')
                    
    def saida(self):
        cont = 0
        retira = input('\nInforme o código do produto: ')
        for i in range(len(self.gerenciar.lista_produtos)):
            if self.gerenciar.lista_produtos[i].cod == retira:
                sa = int(input('Informe a quantidade do produto: '))
                if self.gerenciar.lista_produtos[i].quantidade > sa:
                    self.gerenciar.lista_produtos[i].quantidade -= sa
                    self.movimentacao.append(f'Saida de {sa} unidades do produto ' + self.gerenciar.lista_produtos[i].cod)
                    self.saida_p.append(f'Saida de {sa} unidades do produto ' + self.gerenciar.lista_produtos[i].cod)
                else:
                    print('O valor solicitado excede a quantidade no estoque.')
            else:
                cont += 1
                if cont == len(self.gerenciar.lista_produtos):
                    print('Código não encontrado!')

    def imprimir_t(self):
        for i in self.movimentacao:
            print('\n ', i)
            print('')

    def imprimir_e(self):
        for i in self.entrada_p:
            print('\n ', i)
            print('')
            
    def imprimir_s(self):
        for i in self.saida_p:
            print('\n ', i)
            print('')
