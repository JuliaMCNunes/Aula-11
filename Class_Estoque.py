from Class_Produto import * 

class Estoque:
    def __init__(self):
        self.lista_produtos = []
        
    def cadastrar_produtos(self):
        print('')
        codi = input('Informe o código do produto: ')
        desc = input('Informe a descrição do produto: ')
        fabri = input('Informe o fabricante do produto: ')
        val = input('Informe o valor unitário deste produto: ')
        self.lista_produtos.append(Produto(cod=codi, descricao=desc, fabricante=fabri, valor=val))
        print('\nProduto cadastrado com sucesso!\n')
        
    def mostrar_itens(self):
        cont = 0
        procurar = input('\nInforme o código do produto que está procurando: ')
        for i in range(len(self.lista_produtos)):
            if self.lista_produtos[i].cod == procurar:
                print('\nCódigo:', self.lista_produtos[i].cod, '-', ' Descrição:', self.lista_produtos[i].descricao, '-',
                      ' Fabricante:', self.lista_produtos[i].fabricante, '-', ' Quantidade:', self.lista_produtos[i].quantidade, '-',
                      ' Valor Unitário:', self.lista_produtos[i].valor)
                print('')
            elif procurar == '':
                print('\nCódigo:', self.lista_produtos[i].cod, '-', ' Descrição:', self.lista_produtos[i].descricao, '-',
                      ' Fabricante:', self.lista_produtos[i].fabricante, '-', ' Quantidade:', self.lista_produtos[i].quantidade, '-',
                      ' Valor Unitário:', self.lista_produtos[i].valor)
                print('')
            else:
                cont += 1
                if cont == len(self.lista_produtos):
                    print('Código não encontrado!')
    
    def mudar_descricao(self):
        cont = 0
        select_cod = input('\nInforme o código do produto que deseja alterar: ')
        for i in range(len(self.lista_produtos)):
            if self.lista_produtos[i].cod == select_cod:
                self.lista_produtos[i].descricao = input('Informe a nova descricão do produto: ')
                print('')
            else:
                cont += 1
                if cont == len(self.lista_produtos):
                    print('\nEstes código não está cadastrado!\n')
