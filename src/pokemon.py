"""
Módulo de definição da classe Pokemon.
"""


class Pokemon:
    """
    Classe que representa um Pokémon.
    
    Attributes:
        id (int): Identificador único do Pokémon na Pokédex.
        nome (str): Nome do Pokémon.
        tipo (str): Tipo do Pokémon (ex: Fogo, Água, Planta, etc).
    """
    
    def __init__(self, id: int, nome: str, tipo: str):
        """
        Inicializa um novo Pokémon.
        
        Args:
            id (int): Identificador único do Pokémon.
            nome (str): Nome do Pokémon.
            tipo (str): Tipo do Pokémon.
        """
        self.id = id
        self.nome = nome
        self.tipo = tipo
    
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
        import random
        tipos = ["Fogo", "Água", "Planta", "Elétrico", "Normal"]
        id_aleatorio = random.randint(1, 151)
        nome = f"Pokemon_{id_aleatorio}"
        tipo = random.choice(tipos)
        return Pokemon(id_aleatorio, nome, tipo)
