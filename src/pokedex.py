"""
Módulo de definição da classe Pokedex.
"""
from typing import Dict, Set
from src.pokemon import Pokemon


class Pokedex:
    """
    Classe que representa a Pokédex - registro de pokémons capturados.
    
    Attributes:
        registro_total (Dict[int, Pokemon]): Dicionário com todos os pokémons registrados.
        status_captura (Set[int]): Conjunto com IDs dos pokémons já capturados.
    """
    
    def __init__(self):
        """Inicializa uma nova Pokédex vazia."""
        self.registro_total: Dict[int, Pokemon] = {}
        self.status_captura: Set[int] = set()
    
    def registrar_captura(self, id_pokemon: int) -> None:
        """
        Marca um pokémon como capturado na Pokédex.
        
        Args:
            id_pokemon (int): ID do pokémon capturado.
        """
        if id_pokemon in self.registro_total:
            self.status_captura.add(id_pokemon)
        else:
            raise ValueError(f"Pokémon com ID {id_pokemon} não foi registrado ainda.")
    
    def exibir_status(self) -> Dict[int, str]:
        """
        Retorna o status de captura de todos os pokémons registrados.
        
        Returns:
            Dict[int, str]: Mapa com ID do pokémon e seu status de captura.
        """
        status_map = {}
        for id_pokemon, pokemon in self.registro_total.items():
            capturado = "Capturado" if id_pokemon in self.status_captura else "Não capturado"
            status_map[id_pokemon] = f"{pokemon.nome} ({pokemon.tipo}): {capturado}"
        return status_map
    
    def adicionar_pokemon_registro(self, pokemon: Pokemon) -> None:
        """
        Adiciona um pokémon ao registro total da Pokédex.
        
        Args:
            pokemon (Pokemon): Pokémon a ser adicionado.
        """
        self.registro_total[pokemon.id] = pokemon
    
    def obter_pokemon(self, id_pokemon: int) -> Pokemon:
        """
        Obtém as informações de um pokémon pelo ID.
        
        Args:
            id_pokemon (int): ID do pokémon desejado.
            
        Returns:
            Pokemon: O pokémon solicitado.
        """
        if id_pokemon not in self.registro_total:
            raise ValueError(f"Pokémon com ID {id_pokemon} não existe na Pokédex.")
        return self.registro_total[id_pokemon]
    
    def quantidade_capturados(self) -> int:
        """
        Retorna a quantidade de pokémons capturados.
        
        Returns:
            int: Total de pokémons capturados.
        """
        return len(self.status_captura)
    
    def quantidade_total(self) -> int:
        """
        Retorna a quantidade total de pokémons conhecidos.
        
        Returns:
            int: Total de pokémons no registro.
        """
        return len(self.registro_total)
    
    def __repr__(self) -> str:
        """Representação em string da Pokédex."""
        return (f"Pokedex(Total: {self.quantidade_total()}, "
                f"Capturados: {self.quantidade_capturados()})")
