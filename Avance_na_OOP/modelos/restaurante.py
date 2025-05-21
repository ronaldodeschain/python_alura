from modelos.avaliacao import Avaliacao

class Restaurante:
    """representa um restaurante e suas caracteristicas"""

    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instancia de restaurante

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria(str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        """ Retorna uma representação em string do restaurante"""
        return f'{self._nome} | {self._categoria}'
    
    #para definir um método da classe
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes"""
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliacao'.ljust(25)}| {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} |{str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    
    @property
    def ativo(self):
        """ Retorna o estado do restaurante """
        return 'verdadeiro' if self._ativo else 'falso'
    
    def alternar_estado(self):
        """ Alterna o estado de atividade do restaurante """
        self._ativo = not self._ativo
    

    def receber_avaliacao(self,cliente,nota):
        """
        Registra uma avaliação para o restaurante.

        Parametros:
        - Cliente(str): o nome do cliente da avaliação
        - nota(float): A nota atribuida ao restaurante(Entre 1 e 5)
        """        
        if 0 < nota <=5:
            avaliacao = Avaliacao(cliente,nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a media das avaliações"""
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao 
                             in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas,1)
        return media

    def adicionar_bebida_no_menu(self,bebida):
        self._cardapio.append(bebida)

    def adicionar_prato_no_menu(self,prato):
        self._cardapio.append(prato)