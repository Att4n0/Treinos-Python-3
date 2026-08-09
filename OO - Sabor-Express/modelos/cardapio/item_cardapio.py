from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        '''Método abstrato. Só serve pra forçar classes filhas desta a ter um método detalhando desconto.
        Se não tiverem, o programa quebra.'''
        pass