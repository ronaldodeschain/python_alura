from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self,nome,preco,tamanho,descricao):
        self._nome = nome
        self._preco = preco
        self.tamanho = tamanho
        self.descricao = descricao

    def __str__(self):
        return self._nome


    def aplicar_desconto(self):
        ...