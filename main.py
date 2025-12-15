"""
Script principal com exemplo de uso do sistema de Pokémon.
Demonstra como utilizar o sistema de forma escalável.
"""
from src import Pokemon, Pokedex, PCBox, Treinador
import random


def criar_pokedex_exemplo() -> Pokedex:
    """
    Cria uma Pokédex de exemplo com alguns pokémons.
    VOCÊ PODE ADICIONAR MAIS POKÉMONS AQUI CONFORME NECESSÁRIO.
    
    Returns:
        Pokedex: Pokédex inicializada com pokémons.
    """
    pokedex = Pokedex()
    
    # Exemplo com alguns pokémons - ADICIONE MAIS AQUI!
    pokemons = [
        Pokemon(1, "Bulbasaur", "Planta"),
        Pokemon(4, "Charmander", "Fogo"),
        Pokemon(7, "Squirtle", "Água"),
        Pokemon(25, "Pikachu", "Elétrico"),
        Pokemon(39, "Jigglypuff", "Normal"),
        Pokemon(54, "Psyduck", "Água"),
        Pokemon(58, "Growlithe", "Fogo"),
        Pokemon(63, "Abra", "Psíquico"),
        Pokemon(66, "Machop", "Lutador"),
        Pokemon(69, "Bellsprout", "Planta"),
    ]
    
    # Registra cada pokémon na Pokédex
    for pokemon in pokemons:
        pokedex.adicionar_pokemon_registro(pokemon)
    
    return pokedex


def simular_captura(treinador: Treinador, pokedex: Pokedex, pcbox: PCBox) -> None:
    """
    Simula a captura de pokémons aleatórios.
    
    Args:
        treinador (Treinador): Treinador que vai capturar pokémons.
        pokedex (Pokedex): Pokédex para registrar capturas.
        pcbox (PCBox): PCBox para armazenar pokémons.
    """
    print(f"\n{'='*60}")
    print(f"Iniciando captura de pokémons para {treinador.nome}...")
    print(f"{'='*60}\n")
    
    pokemons_registro = list(pokedex.registro_total.values())
    
    # Simula captura de 5 pokémons aleatórios
    for i in range(5):
        pokemon = random.choice(pokemons_registro)
        
        # Armazena no PCBox
        if pcbox.armazenar_pokemon(pokemon):
            # Registra na Pokédex
            pokedex.registrar_captura(pokemon.id)
            print(f"✓ {treinador.nome} capturou {pokemon.nome}!")
        else:
            print(f"✗ PCBox cheio! Não foi possível capturar {pokemon.nome}")
    
    print()


def exibir_resumo(treinador: Treinador, pokedex: Pokedex, pcbox: PCBox) -> None:
    """
    Exibe um resumo das informações do treinador.
    
    Args:
        treinador (Treinador): Treinador a ser resumido.
        pokedex (Pokedex): Pokédex a ser consultada.
        pcbox (PCBox): PCBox a ser consultado.
    """
    print(f"\n{'='*60}")
    print(f"RESUMO DE {treinador.nome.upper()}")
    print(f"{'='*60}")
    
    treinador.consultar_pokedex(pokedex)
    treinador.consultar_pcbox(pcbox)
    
    print(f"\n{'='*60}\n")


def main():
    """Função principal que executa o sistema."""
    
    # Inicializa componentes principais
    pokedex_global = criar_pokedex_exemplo()
    pcbox_global = PCBox()
    
    # Cria treinadores
    treinador1 = Treinador("Ash")
    treinador2 = Treinador("Misty")
    
    print(f"\n{'='*60}")
    print("BEM-VINDO AO SISTEMA POKÉMON!")
    print(f"{'='*60}\n")
    
    # Simula capturas para cada treinador
    simular_captura(treinador1, pokedex_global, pcbox_global)
    simular_captura(treinador2, pokedex_global, pcbox_global)
    
    # Exibe resumos
    exibir_resumo(treinador1, pokedex_global, pcbox_global)
    exibir_resumo(treinador2, pokedex_global, pcbox_global)
    
    # Exemplo adicional: Mostrando a escalabilidade
    print(f"{'='*60}")
    print("DEMONSTRAÇÃO DE ESCALABILIDADE")
    print(f"{'='*60}\n")
    
    print(f"Total de pokémons conhecidos: {pokedex_global.quantidade_total()}")
    print(f"Total de pokémons capturados: {pokedex_global.quantidade_capturados()}")
    print(f"Total armazenado no PCBox: {pcbox_global.obter_quantidade_total()}")
    print(f"Espaço disponível no PCBox: {pcbox_global.obter_espaco_total_disponivel()}\n")
    
    print("Para adicionar mais pokémons:")
    print("  1. Edite a função criar_pokedex_exemplo() em main.py")
    print("  2. Adicione novos objetos Pokemon à lista de pokémons")
    print("  3. O sistema se ajustará automaticamente!\n")


if __name__ == "__main__":
    main()
