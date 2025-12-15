from src.pokemon import Pokemon
from src.pokedex import Pokedex
from src.pcbox import PCBox
from typing import Set


class Treinador:
    
    def __init__(self, nome: str):
        self.nome = nome
        self.pcbox = PCBox()
        self.capturados: Set[int] = set()
    
    def registrar_captura(self, id_pokemon: int) -> None:
        self.capturados.add(id_pokemon)
    
    def consultar_pokedex(self, pokedex: Pokedex) -> None:
        status = pokedex.exibir_status()
        print(f"\n=== Pokédex de {self.nome} ===")
        print(f"Total de Pokémons: {pokedex.quantidade_total()}")
        print(f"Capturados: {len(self.capturados)}")
        
        max_descoberto = max(self.capturados) if self.capturados else 0
        limite = max(10, max_descoberto)
        
        print(f"\nMostrando até ID {limite}:")
        for id_p in range(1, limite + 1):
            if id_p in status:
                info = status[id_p]
                nome = "???" if id_p not in self.capturados else info.split(":")[0]
                capturado = "Capturado" if id_p in self.capturados else "Não capturado"
                print(f"  {id_p} - {nome}: {capturado}")
            else:
                break
    
    def obter_informacoes(self) -> str:
        return (f"Treinador: {self.nome}\n"
                f"Capturados: {len(self.capturados)}\n"
                f"PCBox: {self.pcbox}")
    
    def demonstrar_ataque(self, pokemon: Pokemon) -> None:
        if hasattr(pokemon, 'ataque_especial'):
            print(pokemon.ataque_especial())
        else:
            print(f"{pokemon.nome} usa um ataque básico!")
    
    def __repr__(self) -> str:
        return f"Treinador(nome='{self.nome}')"
