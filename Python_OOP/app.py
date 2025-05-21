from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca','Gourmet')
restaurante_praca.receber_avaliacao('Erasmo',10)
restaurante_praca.receber_avaliacao('Lais',8)
restaurante_praca.receber_avaliacao('Hebe',3)


def main():
   Restaurante.listar_restaurantes()


if __name__ =='__main__':
    main()