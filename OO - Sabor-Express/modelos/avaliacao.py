class Avaliacao:
    '''Classe que comporta as avaliações dos clientes para cada restaurante. '''
    def __init__(self, cliente, nota):
        '''Método construtor, inicia os atributos dos objetos
        
        Inputs:
        - cliente (str)
        - nota (int)
        
        '''
        self._cliente = cliente
        self._nota = nota
