"""
Módulo de definição da classe PCBox.
"""
from typing import List, Optional
from src.pokemon import Pokemon


class Boxes:
    """
    Classe que gerencia os boxes (caixas) de armazenamento de pokémons.
    
    Attributes:
        id (int): Identificador da caixa.
        capacidade (int): Capacidade máxima de pokémons na caixa.
        pokemons (List[Pokemon]): Lista de pokémons armazenados.
    """
    
    def __init__(self, id: int, capacidade: int = 30):
        """
        Inicializa uma nova caixa.
        
        Args:
            id (int): Identificador da caixa.
            capacidade (int): Capacidade máxima de pokémons. Padrão: 30.
        """
        self.id = id
        self.capacidade = capacidade
        self.pokemons: List[Pokemon] = []
    
    def adicionar_pokemon(self, pokemon: Pokemon) -> bool:
        """
        Adiciona um pokémon à caixa se houver espaço.
        
        Args:
            pokemon (Pokemon): Pokémon a ser adicionado.
            
        Returns:
            bool: True se adicionado com sucesso, False se caixa cheia.
        """
        if len(self.pokemons) < self.capacidade:
            self.pokemons.append(pokemon)
            return True
        return False
    
    def remover_pokemon(self, indice: int) -> Optional[Pokemon]:
        """
        Remove um pokémon da caixa pelo índice.
        
        Args:
            indice (int): Índice do pokémon na lista.
            
        Returns:
            Optional[Pokemon]: O pokémon removido ou None se índice inválido.
        """
        if 0 <= indice < len(self.pokemons):
            return self.pokemons.pop(indice)
        return None
    
    def listar_pokemons(self) -> List[Pokemon]:
        """
        Retorna a lista de pokémons armazenados.
        
        Returns:
            List[Pokemon]: Lista de pokémons na caixa.
        """
        return self.pokemons.copy()
    
    def obter_espaco_disponivel(self) -> int:
        """
        Retorna o espaço disponível na caixa.
        
        Returns:
            int: Quantidade de pokémons que ainda cabem.
        """
        return self.capacidade - len(self.pokemons)
    
    def esta_cheia(self) -> bool:
        """Verifica se a caixa está cheia."""
        return len(self.pokemons) >= self.capacidade
    
    def __repr__(self) -> str:
        """Representação em string da caixa."""
        return (f"Box(id={self.id}, "
                f"Pokémons: {len(self.pokemons)}/{self.capacidade})")


class PCBox:
    """
    Classe que gerencia múltiplas caixas de armazenamento.
    
    Attributes:
        boxes (Boxes): Coleção de caixas.
        armazenamento (List[Pokemon]): Lista de todos os pokémons armazenados.
    """
    
    def __init__(self):
        """Inicializa o PCBox com 18 caixas padrão."""
        self.boxes: List[Boxes] = [Boxes(id=i+1) for i in range(18)]
        self.armazenamento: List[Pokemon] = []
    
    def armazenar_pokemon(self, pokemon: Pokemon) -> bool:
        """
        Armazena um pokémon procurando a primeira caixa com espaço.
        
        Args:
            pokemon (Pokemon): Pokémon a ser armazenado.
            
        Returns:
            bool: True se armazenado com sucesso, False se sem espaço.
        """
        for box in self.boxes:
            if not box.esta_cheia():
                if box.adicionar_pokemon(pokemon):
                    self.armazenamento.append(pokemon)
                    return True
        return False
    
    def listar_pokemons(self) -> List[Pokemon]:
        """
        Retorna a lista de todos os pokémons armazenados.
        
        Returns:
            List[Pokemon]: Lista de todos os pokémons.
        """
        return self.armazenamento.copy()
    
    def remover_pokemon(self, id_unico: int) -> Optional[Pokemon]:
        """
        Remove um pokémon do armazenamento pelo índice.
        
        Args:
            id_unico (int): Índice único do pokémon.
            
        Returns:
            Optional[Pokemon]: O pokémon removido ou None.
        """
        if 0 <= id_unico < len(self.armazenamento):
            pokemon = self.armazenamento.pop(id_unico)
            # Remove também da caixa
            for box in self.boxes:
                if pokemon in box.pokemons:
                    box.pokemons.remove(pokemon)
                    break
            return pokemon
        return None
    
    def obter_quantidade_total(self) -> int:
        """Retorna a quantidade total de pokémons armazenados."""
        return len(self.armazenamento)
    
    def obter_espaco_total_disponivel(self) -> int:
        """Retorna o espaço total disponível em todas as caixas."""
        return sum(box.obter_espaco_disponivel() for box in self.boxes)
    
    def listar_boxes(self) -> List[Boxes]:
        """Retorna a lista de todas as caixas."""
        return self.boxes.copy()
    
    def __repr__(self) -> str:
        """Representação em string do PCBox."""
        return (f"PCBox(Total de Pokémons: {self.obter_quantidade_total()}, "
                f"Espaço Disponível: {self.obter_espaco_total_disponivel()})")
