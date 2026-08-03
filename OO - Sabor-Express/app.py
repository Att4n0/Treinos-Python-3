from modelos.restaurante import Restaurante
'''Importa a classe Restaurante do arquivo restaurante.py, na pasta modelos.'''

#Criando restaurantes:
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Ninguém', 10)
restaurante_praca.receber_avaliacao('Ulisses', 8)
restaurante_praca.receber_avaliacao('Odisseu', 3)

restaurante_mexicano = Restaurante('El Sombrero', 'Mexicana')
restaurante_japones = Restaurante('Midorigoi','Japonesa')

restaurante_mexicano.alternar_estado()

def main():
    '''Ao iniciar o programa, faz o seguinte:'''
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    '''Se este arquivo não é chamado por outro, e sim aberto como programa principal,
    Executa os comandos a seguir. '''
    main()