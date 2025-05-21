from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praca','Gourmet')
fogosa = Bebida('Fogosa',15.0,'shot')
quiche = Prato('Quiche',8.9,'melhor quiche da cidade')
restaurante_praca.adicionar_no_cardapio(fogosa)
restaurante_praca.adicionar_no_cardapio(quiche)

def main():
  restaurante_praca.exibir_cardapio

if __name__ =='__main__':
    main()