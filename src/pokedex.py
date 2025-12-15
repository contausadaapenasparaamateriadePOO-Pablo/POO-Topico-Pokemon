from typing import Dict, Set
from src.pokemon import Pokemon


class Pokedex:
    
    def __init__(self):
        self.registro_total: Dict[int, Pokemon] = {}
        self.status_captura: Set[int] = set()
    
    def registrar_captura(self, id_pokemon: int) -> None:
        if id_pokemon in self.registro_total:
            self.status_captura.add(id_pokemon)
        else:
            raise ValueError(f"Pokémon com ID {id_pokemon} não foi registrado ainda.")
    
    def exibir_status(self) -> Dict[int, str]:
        status_map = {}
        for id_pokemon, pokemon in self.registro_total.items():
            capturado = "Capturado" if id_pokemon in self.status_captura else "Não capturado"
            status_map[id_pokemon] = f"{pokemon.nome} ({pokemon.tipo}): {capturado}"
        return status_map
    
    def adicionar_pokemon_registro(self, pokemon: Pokemon) -> None:
        self.registro_total[pokemon.id] = pokemon
    
    def obter_pokemon(self, id_pokemon: int) -> Pokemon:
        if id_pokemon not in self.registro_total:
            raise ValueError(f"Pokémon com ID {id_pokemon} não existe na Pokédex.")
        return self.registro_total[id_pokemon]
    
    def quantidade_capturados(self) -> int:
        return len(self.status_captura)
    
    def quantidade_total(self) -> int:
        return len(self.registro_total)
    
    def __repr__(self) -> str:
        return (f"Pokedex(Total: {self.quantidade_total()}, "
                f"Capturados: {self.quantidade_capturados()})")
