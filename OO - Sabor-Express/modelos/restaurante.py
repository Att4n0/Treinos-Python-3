from modelos.avaliacao import Avaliacao
'''Importa a classe Avaliacao do arquivo avaliacao. Essa classe vai interagir com a classe Restaurante'''
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    """Representa um restaurante e suas características."""
    restaurantes = []

    def __init__(self, nome, categoria):
        '''No momento da criação(instanciação) de um objeto da classe, o método inicializa os
        atributos e define o estado inicial da instância.
        
        Input:
        - Argumentos
        '''
    
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        '''Método especial que define a representação em texto legível 
        de um objeto, sendo acionado automaticamente pelas funções print() e str().
        Quando der um print que aciona o objeto, ao invés do retorno ser um código falando
        onde ele tá na memória e a classe, vai ser retornado o que tiver em retorno aqui em baixo.
        
        Input:
        - Argumento self

        Output:
        - Uma string

        '''
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        #Método criado
        '''Quando chamado, o método vai listar automaticamente todos os objetos na lista restaurantes
        
            Repare que na parte de restaurante ativo, chama-se .ativo, e não ._ativo.
            Assim, chama-se a propriedade ativo (abaixo), que retorna os emojis ao invés de False e True.
            O ^25 faz com que tenha um espaço de 25 caracteres para a string, e ela fique centralizada nesse espaço.

        Inputs
        -nome dos restaurantes (str)
        -categorias dos restaurantes (str)
        -média das avaliações (float)
        -emojis de ativo (str)

        Output:
        -print com as informações dos restaurantes
        
        '''
        print(f'{'Nome do restaurante':^25} | {'Categoria':^25} | {'Nota':^25} | {'Status':^25}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome:^25} | {restaurante._categoria:^25} | {restaurante.media_avaliacoes:^25} | {restaurante.ativo:^25}')

    @property
    def ativo(self):
        '''Propriedade "getter":
            se o restaurante estiver ativo, retorna como string o emoji ✅
            se or restaurante não estiver ativo, retorna o emoji ❌
        
            Útil para mostrar em listas. Ver função listar restaurantes
        '''
        return '✅' if self._ativo else '❌'

    def alternar_estado(self):
        '''Alterna o estado do restaurante de ativo para não ativo, ou vice-versa'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''Adiciona as avaliações de clientes, incluindo o nome do cliente e nota, a uma lista ligada ao objeto.
        As notas devem estar entre 0 e 5 (incluindo 5). ou não serão levadas em conta.

        Input:
        -cliente (str) (Importado)
        -nota (int) (Importado)

        Output:
        -Adiciona à lista individual do restaurante a avaliação.
        '''
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        '''Propriedade que calcula a média das notas para um restaurante.
           Se não há avaliações, a média é 0.
        
        Inputs:
        - nota (int) (Importado)
        - avaliação (list)

        Output:
        - média (float)

        '''
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_no_cardapio(self, item):
        '''Caso o item com o qual o método é chamado for instância de classe filha ou pai,
        adiciona à lista no cardápio.'''
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item,'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print (mensagem_prato)

            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)