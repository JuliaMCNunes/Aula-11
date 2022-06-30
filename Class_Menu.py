from Class_Estoque import * 
from Class_Gerenciar_Estoque import * 

class Menu:
    def __init__(self):
        catalogo = Estoque()
        catalogo1 = Gerenciador()
        catalogo1.gerenciar = catalogo
        
        while True:
            exibir = print('--------------------------------------------------------'
                            '\nInforme a opção desejada:'
                            ''
                            '\n1 - Cadastrar fabricante'                            
                            ''                                                       
                            '\n2 - Cadastrar produto'                                
                            ''                                                       
                            '\n3 - Procurar produto'                                 
                            ''                                                       
                            '\n4 - Alterar informações do produto'                   
                            ''                                                       
                            '\n5 - Efetuar abastecimento de produtos no estoque'      
                            ''                                                       
                            '\n6 - Efetuar retirada de produtos no estoque'          
                            ''                                                       
                            '\n7 - Ver movimentação de estoque'                      
                            ''                                                       
                            '\n8 - Ver as entradas de produtos no estoque'           
                            ''                                                       
                            '\n9 - Ver as saidas de produtos no estoque'             
                            ''                                                       
                            '\n0 - Sair\n'                                           
                            '-------------------------------------------------------')
            selecao = input(': ')
            
            if selecao == '1':
                catalogo.cadastrar_fabricantes()
                
            elif selecao == '2':
                catalogo.cadastrar_produtos()
                
            elif selecao == '3':
                catalogo.mostrar_itens()
                
            elif selecao == '4':
                catalogo.mudar_descricao()
                
            elif selecao == '5':
                catalogo1.entrada()
                
            elif selecao == '6':
                catalogo1.saida()
                
            elif selecao == '7':
                catalogo1.imprimir_t()
                
            elif selecao == '8':
                catalogo1.imprimir_e()
                
            elif selecao == '9':
                catalogo1.imprimir_s()
                
            elif selecao == '0':
                break
            
            else:
                print('\nOpção inválida!\n')
