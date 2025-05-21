class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    #para definir um método da classe
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    #to get
    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'falso'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    


