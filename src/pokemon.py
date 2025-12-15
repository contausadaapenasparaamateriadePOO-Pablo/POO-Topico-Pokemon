class Pokemon:
    
    def __init__(self, id: int, nome: str, tipos: list[str]):
        self.id = id
        self.nome = nome
        self.tipos = tipos
        self.tipo = tipos[0] if tipos else "Desconhecido"
    
    def __repr__(self) -> str:
        """Representação em string do Pokémon."""
        return f"Pokemon(id={self.id}, nome='{self.nome}', tipo='{self.tipo}')"
    
    def __eq__(self, other) -> bool:
        """Compara dois Pokémons pelo ID."""
        if isinstance(other, Pokemon):
            return self.id == other.id
        return False
    
    def __hash__(self) -> int:
        """Permite usar Pokémon em sets e dicts."""
        return hash(self.id)
    
    @staticmethod
    def gerar_pokemon_aleatorio() -> 'Pokemon':
        """
        Gera um Pokémon aleatório (método que pode ser customizado).
        
        Returns:
            Pokemon: Um novo Pokémon aleatório.
        """
        return Pokemon(id_aleatorio, nome, [tipo])


class PokemonFogo(Pokemon):
    def __init__(self, id: int, nome: str, tipos: list[str]):
        super().__init__(id, nome, tipos)
    
    def ataque_especial(self) -> str:
        return f"{self.nome} usa Chamas!"  # Ataque especial de fogo


class PokemonAgua(Pokemon):
    def __init__(self, id: int, nome: str, tipos: list[str]):
        super().__init__(id, nome, tipos)
    
    def ataque_especial(self) -> str:
        return f"{self.nome} usa Jato d'Água!"  # Ataque especial de água


class PokemonPlanta(Pokemon):
    def __init__(self, id: int, nome: str, tipos: list[str]):
        super().__init__(id, nome, tipos)
    
    def ataque_especial(self) -> str:
        return f"{self.nome} usa Folha Navalha!"  # Ataque especial de planta


class PokemonEletrico(Pokemon):
    def __init__(self, id: int, nome: str, tipos: list[str]):
        super().__init__(id, nome, tipos)
    
    def ataque_especial(self) -> str:
        return f"{self.nome} usa Choque do Trovão!"  # Ataque especial elétrico


class PokemonNormal(Pokemon):
    def __init__(self, id: int, nome: str, tipos: list[str]):
        super().__init__(id, nome, tipos)
    
    def ataque_especial(self) -> str:
        return f"{self.nome} usa Ataque Rápido!"  # Ataque especial normal
