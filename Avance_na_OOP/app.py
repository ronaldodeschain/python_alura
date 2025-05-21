from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praca','Gourmet')
fogosa = Bebida('Fogosa',15.0,'shot')
quiche = Prato('Quiche',8.9,'melhor quiche da cidade')
restaurante_praca.adicionar_bebida_no_menu(fogosa)
restaurante_praca.adicionar_prato_no_menu(quiche)

def main():
   print(fogosa)
   print(quiche)

if __name__ =='__main__':
    main()