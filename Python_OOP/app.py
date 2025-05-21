from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca','Gourmet')
restaurante_mexicano = Restaurante('el paco','mexicano')
restaurante_japones = Restaurante('Japartiu','japonesa')






def main():
   Restaurante.listar_restaurantes()


if __name__ =='__main__':
    main()