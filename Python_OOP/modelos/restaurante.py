class Restaurante:
    def __init__(self,nome, categoria):
        self.nome = nome
        self.categoria = categoria
        ativo = False

di_colonia = Restaurante('Di Colonia','Gourmet')
print(di_colonia.nome)
print(di_colonia.categoria)
print(vars(di_colonia))
