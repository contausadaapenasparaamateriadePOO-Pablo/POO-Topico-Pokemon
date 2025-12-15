"""
Módulo de definição da classe Treinador.
"""
from src.pokemon import Pokemon
from src.pokedex import Pokedex
from src.pcbox import PCBox


class Treinador:
    """
    Classe que representa um Treinador Pokémon.
    
    O treinador possui:
    - Um nome
    - Uma Pokédex para registrar e acompanhar pokémons capturados
    - Um PCBox para armazenar pokémons capturados
    
    Attributes:
        nome (str): Nome do treinador.
        pokedex (Pokedex): Pokédex do treinador.
        pcbox (PCBox): Caixa de armazenamento do treinador.
    """
    
    def __init__(self, nome: str):
        """
        Inicializa um novo treinador.
        
        Args:
            nome (str): Nome do treinador.
        """
        self.nome = nome
        self.pokedex = Pokedex()
        self.pcbox = PCBox()
    
    def capturar_novo_pokemon(self, pcbox: 'PCBox', pokedex: 'Pokedex') -> None:
        """
        Consulta o PCBox e Pokédex (referência compartilhada).
        Este método será chamado quando o treinador captura um novo pokémon.
        
        Args:
            pcbox (PCBox): Referência ao PCBox global.
            pokedex (Pokedex): Referência à Pokédex global.
        """
        pass  # Implementação específica de captura será feita no main
    
    def consultar_pokedex(self, pokedex: Pokedex) -> None:
        """
        Consulta a Pokédex para ver informações de pokémons.
        
        Args:
            pokedex (Pokedex): Pokédex a ser consultada.
        """
        status = pokedex.exibir_status()
        print(f"\n=== Pokédex de {self.nome} ===")
        print(f"Total de Pokémons: {pokedex.quantidade_total()}")
        print(f"Capturados: {pokedex.quantidade_capturados()}")
        print("\nStatus dos Pokémons:")
        for _, info in status.items():
            print(f"  - {info}")
    
    def consultar_pcbox(self, pcbox: 'PCBox') -> None:
        """
        Consulta o PCBox para ver pokémons armazenados.
        
        Args:
            pcbox (PCBox): PCBox a ser consultado.
        """
        pokemons = pcbox.listar_pokemons()
        print(f"\n=== PCBox de {self.nome} ===")
        print(f"Total de Pokémons Armazenados: {pcbox.obter_quantidade_total()}")
        print(f"Espaço Disponível: {pcbox.obter_espaco_total_disponivel()}")
        print("\nPokémons Armazenados:")
        if not pokemons:
            print("  - Nenhum pokémon armazenado")
        else:
            for idx, pokemon in enumerate(pokemons):
                print(f"  {idx + 1}. {pokemon}")
    
    def obter_informacoes(self) -> str:
        """
        Retorna informações do treinador.
        
        Returns:
            str: Informações formatadas do treinador.
        """
        return (f"Treinador: {self.nome}\n"
                f"Pokédex: {self.pokedex}\n"
                f"PCBox: {self.pcbox}")
    
    def __repr__(self) -> str:
        """Representação em string do treinador."""
        return f"Treinador(nome='{self.nome}')"
