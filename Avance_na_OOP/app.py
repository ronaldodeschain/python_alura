from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praca','Gourmet')
fogosa = Bebida('Fogosa',15.0,'shot')
pudim = Sobremesa('Pudim docin',5.00,'Graaaande','Pudim mais que docin')
fogosa.aplicar_desconto()

quiche = Prato('Quiche',8.9,'melhor quiche da cidade')
restaurante_praca.adicionar_no_cardapio(fogosa)
restaurante_praca.adicionar_no_cardapio(quiche)
restaurante_praca.adicionar_no_cardapio(pudim)

def main():
  restaurante_praca.exibir_cardapio

if __name__ =='__main__':
    main()