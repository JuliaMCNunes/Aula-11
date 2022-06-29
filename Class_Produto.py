class Produto:
    def __init__(self, cod, descricao, fabricante, valor, quantidade=0):
        self.cod = cod
        self.descricao = descricao
        self.fabricante = fabricante
        self.valor = valor
        self.quantidade = quantidade
