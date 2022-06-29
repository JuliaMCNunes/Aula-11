from Class_Estoque import * 
from Class_Gerenciar_Estoque import * 

class Menu:
    def __init__(self):
        catalogo = Estoque()
        catalogo1 = Gerenciador()
        catalogo1.gerenciar = catalogo
        
        while True:
            selecao = input('Informe a opção desejada:' 
                            '\n1 - Cadastrar produto' 
                            '\n2 - Procurar produto'
                            '\n3 - Alterar informações do produto'
                            '\n4 - Efetuar abastecimento de produtos no estoque'
                            '\n5 - Efetuar retirada de produtos no estoque'
                            '\n6 - Ver movimentação de estoque'
                            '\n7 - Ver as entradas de produtos no estoque'
                            '\n8 - Ver as saidas de produtos no estoque'
                            '\n0 - Sair\n')
            
            if selecao == '1':
                catalogo.cadastrar_produtos()
            elif selecao == '2':
                catalogo.mostrar_itens()
            elif selecao == '3':
                catalogo.mudar_descricao()
            elif selecao == '4':
                catalogo1.entrada()
            elif selecao == '5':
                catalogo1.saida()
            elif selecao == '6':
                catalogo1.imprimir_t()
            elif selecao == '7':
                catalogo1.imprimir_e()
            elif selecao == '8':
                catalogo1.imprimir_s()
            elif selecao == '0':
                break
            else:
                print('\nOpção inválida!\n')
