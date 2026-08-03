from modelos.restaurante import Restaurante
'''Importa a classe Restaurante do arquivo restaurante.py, na pasta modelos.'''
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


#Criando restaurantes:
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('El Sombrero', 'Mexicana')
restaurante_japones = Restaurante('Midorigoi','Japonesa')

bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')

restaurante_mexicano.alternar_estado()

def main():
    '''Ao iniciar o programa, faz o seguinte:'''
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    '''Se este arquivo não é chamado por outro, e sim aberto como programa principal,
    Executa os comandos a seguir. '''
    main()