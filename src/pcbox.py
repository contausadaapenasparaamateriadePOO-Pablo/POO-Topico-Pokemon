from typing import List, Optional
from bisect import bisect_left
from src.pokemon import Pokemon


class Boxes:
    
    def __init__(self, id: int, capacidade: int = 30):
        self.id = id
        self.capacidade = capacidade
        self.pokemons: List[Pokemon] = []
    
    def adicionar_pokemon(self, pokemon: Pokemon) -> bool:
        if len(self.pokemons) < self.capacidade:
            # Inserir em ordem de ID
            ids = [p.id for p in self.pokemons]
            pos = bisect_left(ids, pokemon.id)
            self.pokemons.insert(pos, pokemon)
            return True
        return False
    
    def remover_pokemon(self, indice: int) -> Optional[Pokemon]:
        if 0 <= indice < len(self.pokemons):
            return self.pokemons.pop(indice)
        return None
    
    def listar_pokemons(self) -> List[Pokemon]:
        return self.pokemons.copy()
    
    def obter_espaco_disponivel(self) -> int:
        return self.capacidade - len(self.pokemons)
    
    def esta_cheia(self) -> bool:
        return len(self.pokemons) >= self.capacidade
    
    def __repr__(self) -> str:
        return (f"Box(id={self.id}, "
                f"Pokémons: {len(self.pokemons)}/{self.capacidade})")


class PCBox:
    
    def __init__(self):
        self.boxes: List[Boxes] = [Boxes(id=i+1) for i in range(16)]
        self.armazenamento: List[Pokemon] = []
    
    def armazenar_pokemon(self, pokemon: Pokemon) -> bool:
        for box in self.boxes:
            if not box.esta_cheia():
                if box.adicionar_pokemon(pokemon):
                    self.armazenamento.append(pokemon)
                    return True
        return False
    
    def listar_pokemons(self) -> List[Pokemon]:
        return self.armazenamento.copy()
    
    def remover_pokemon(self, id_unico: int) -> Optional[Pokemon]:
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
        return len(self.armazenamento)
    
    def obter_espaco_total_disponivel(self) -> int:
        return sum(box.obter_espaco_disponivel() for box in self.boxes)
    
    def listar_boxes(self) -> List[Boxes]:
        return self.boxes.copy()
    
    def mover_pokemon(self, pokemon: Pokemon, box_origem_id: int, box_destino_id: int) -> bool:
        if box_origem_id == box_destino_id:
            return False
        box_origem = self.boxes[box_origem_id - 1]
        box_destino = self.boxes[box_destino_id - 1]
        if pokemon in box_origem.pokemons and not box_destino.esta_cheia():
            box_origem.pokemons.remove(pokemon)
            box_destino.adicionar_pokemon(pokemon)
            return True
        return False
    
    def __repr__(self) -> str:
        return (f"PCBox(Total de Pokémons: {self.obter_quantidade_total()}, "
                f"Espaço Disponível: {self.obter_espaco_total_disponivel()})")
