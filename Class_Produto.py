class Produto:
    def __init__(self, cod, descricao, objeto, valor, quantidade=0):
        self.cod = cod
        self.descricao = descricao
        self.fabricante = objeto.nome
        self.valor = valor
        self.quantidade = quantidade
