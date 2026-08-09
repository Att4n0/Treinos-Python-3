import os
import subprocess
from modelos.restaurante import Restaurante
'''Importa a classe Restaurante do arquivo restaurante.py, na pasta modelos.'''
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

def limpa_tela():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run(['clear'])

#Criando restaurantes:
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('El Sombrero', 'Mexicana')
restaurante_japones = Restaurante('Midorigoi','Japonesa')

bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
bebida_suco.aplicar_desconto()

prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

restaurante_mexicano.alternar_estado()

def main():
    '''Ao iniciar o programa, faz o seguinte:'''
    limpa_tela()
    restaurante_praca.exibir_cardapio
    

if __name__ == '__main__':
    '''Se este arquivo não é chamado por outro, e sim aberto como programa principal,
    Executa os comandos a seguir. '''
    main()