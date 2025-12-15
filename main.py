from src import Pokemon, PokemonFogo, PokemonAgua, PokemonPlanta, PokemonEletrico, PokemonNormal, Pokedex, PCBox, \
    Treinador, Boxes
import random



def criar_pokemon(id: int, nome: str, tipos: list[str]) -> Pokemon:
    tipo_principal = tipos[0].lower()
    if "fire" in tipo_principal or "fogo" in tipo_principal:
        return PokemonFogo(id, nome, tipos)
    elif "water" in tipo_principal or "água" in tipo_principal:
        return PokemonAgua(id, nome, tipos)
    elif "grass" in tipo_principal or "planta" in tipo_principal:
        return PokemonPlanta(id, nome, tipos)
    elif "electric" in tipo_principal or "elétrico" in tipo_principal:
        return PokemonEletrico(id, nome, tipos)
    else:
        return PokemonNormal(id, nome, tipos)


def criar_pokedex_global() -> Pokedex:
    pokedex = Pokedex()
    pokemon_data = [
        {"id": 1, "nome": "Bulbasaur", "tipos": ["Grass", "Poison"]},
        {"id": 2, "nome": "Ivysaur", "tipos": ["Grass", "Poison"]},
        {"id": 3, "nome": "Venusaur", "tipos": ["Grass", "Poison"]},
        {"id": 4, "nome": "Charmander", "tipos": ["Fire"]},
        {"id": 5, "nome": "Charmeleon", "tipos": ["Fire"]},
        {"id": 6, "nome": "Charizard", "tipos": ["Fire", "Flying"]},
        {"id": 7, "nome": "Squirtle", "tipos": ["Water"]},
        {"id": 8, "nome": "Wartortle", "tipos": ["Water"]},
        {"id": 9, "nome": "Blastoise", "tipos": ["Water"]},
        {"id": 10, "nome": "Caterpie", "tipos": ["Bug"]},
        {"id": 11, "nome": "Metapod", "tipos": ["Bug"]},
        {"id": 12, "nome": "Butterfree", "tipos": ["Bug", "Flying"]},
        {"id": 13, "nome": "Weedle", "tipos": ["Bug", "Poison"]},
        {"id": 14, "nome": "Kakuna", "tipos": ["Bug", "Poison"]},
        {"id": 15, "nome": "Beedrill", "tipos": ["Bug", "Poison"]},
        {"id": 16, "nome": "Pidgey", "tipos": ["Normal", "Flying"]},
        {"id": 17, "nome": "Pidgeotto", "tipos": ["Normal", "Flying"]},
        {"id": 18, "nome": "Pidgeot", "tipos": ["Normal", "Flying"]},
        {"id": 19, "nome": "Rattata", "tipos": ["Normal"]},
        {"id": 20, "nome": "Raticate", "tipos": ["Normal"]},
        {"id": 21, "nome": "Spearow", "tipos": ["Normal", "Flying"]},
        {"id": 22, "nome": "Fearow", "tipos": ["Normal", "Flying"]},
        {"id": 23, "nome": "Ekans", "tipos": ["Poison"]},
        {"id": 24, "nome": "Arbok", "tipos": ["Poison"]},
        {"id": 25, "nome": "Pikachu", "tipos": ["Electric"]},
        {"id": 26, "nome": "Raichu", "tipos": ["Electric"]},
        {"id": 27, "nome": "Sandshrew", "tipos": ["Ground"]},
        {"id": 28, "nome": "Sandslash", "tipos": ["Ground"]},
        {"id": 29, "nome": "Nidoran♀", "tipos": ["Poison"]},
        {"id": 30, "nome": "Nidorina", "tipos": ["Poison"]},
        {"id": 31, "nome": "Nidoqueen", "tipos": ["Poison", "Ground"]},
        {"id": 32, "nome": "Nidoran♂", "tipos": ["Poison"]},
        {"id": 33, "nome": "Nidorino", "tipos": ["Poison"]},
        {"id": 34, "nome": "Nidoking", "tipos": ["Poison", "Ground"]},
        {"id": 35, "nome": "Clefairy", "tipos": ["Fairy"]},
        {"id": 36, "nome": "Clefable", "tipos": ["Fairy"]},
        {"id": 37, "nome": "Vulpix", "tipos": ["Fire"]},
        {"id": 38, "nome": "Ninetales", "tipos": ["Fire"]},
        {"id": 39, "nome": "Jigglypuff", "tipos": ["Normal", "Fairy"]},
        {"id": 40, "nome": "Wigglytuff", "tipos": ["Normal", "Fairy"]},
        {"id": 41, "nome": "Zubat", "tipos": ["Poison", "Flying"]},
        {"id": 42, "nome": "Golbat", "tipos": ["Poison", "Flying"]},
        {"id": 43, "nome": "Oddish", "tipos": ["Grass", "Poison"]},
        {"id": 44, "nome": "Gloom", "tipos": ["Grass", "Poison"]},
        {"id": 45, "nome": "Vileplume", "tipos": ["Grass", "Poison"]},
        {"id": 46, "nome": "Paras", "tipos": ["Bug", "Grass"]},
        {"id": 47, "nome": "Parasect", "tipos": ["Bug", "Grass"]},
        {"id": 48, "nome": "Venonat", "tipos": ["Bug", "Poison"]},
        {"id": 49, "nome": "Venomoth", "tipos": ["Bug", "Poison"]},
        {"id": 50, "nome": "Diglett", "tipos": ["Ground"]},
        {"id": 51, "nome": "Dugtrio", "tipos": ["Ground"]},
        {"id": 52, "nome": "Meowth", "tipos": ["Normal"]},
        {"id": 53, "nome": "Persian", "tipos": ["Normal"]},
        {"id": 54, "nome": "Psyduck", "tipos": ["Water"]},
        {"id": 55, "nome": "Golduck", "tipos": ["Water"]},
        {"id": 56, "nome": "Mankey", "tipos": ["Fighting"]},
        {"id": 57, "nome": "Primeape", "tipos": ["Fighting"]},
        {"id": 58, "nome": "Growlithe", "tipos": ["Fire"]},
        {"id": 59, "nome": "Arcanine", "tipos": ["Fire"]},
        {"id": 60, "nome": "Poliwag", "tipos": ["Water"]},
        {"id": 61, "nome": "Poliwhirl", "tipos": ["Water"]},
        {"id": 62, "nome": "Poliwrath", "tipos": ["Water", "Fighting"]},
        {"id": 63, "nome": "Abra", "tipos": ["Psychic"]},
        {"id": 64, "nome": "Kadabra", "tipos": ["Psychic"]},
        {"id": 65, "nome": "Alakazam", "tipos": ["Psychic"]},
        {"id": 66, "nome": "Machop", "tipos": ["Fighting"]},
        {"id": 67, "nome": "Machoke", "tipos": ["Fighting"]},
        {"id": 68, "nome": "Machamp", "tipos": ["Fighting"]},
        {"id": 69, "nome": "Bellsprout", "tipos": ["Grass", "Poison"]},
        {"id": 70, "nome": "Weepinbell", "tipos": ["Grass", "Poison"]},
        {"id": 71, "nome": "Victreebel", "tipos": ["Grass", "Poison"]},
        {"id": 72, "nome": "Tentacool", "tipos": ["Water", "Poison"]},
        {"id": 73, "nome": "Tentacruel", "tipos": ["Water", "Poison"]},
        {"id": 74, "nome": "Geodude", "tipos": ["Rock", "Ground"]},
        {"id": 75, "nome": "Graveler", "tipos": ["Rock", "Ground"]},
        {"id": 76, "nome": "Golem", "tipos": ["Rock", "Ground"]},
        {"id": 77, "nome": "Ponyta", "tipos": ["Fire"]},
        {"id": 78, "nome": "Rapidash", "tipos": ["Fire"]},
        {"id": 79, "nome": "Slowpoke", "tipos": ["Water", "Psychic"]},
        {"id": 80, "nome": "Slowbro", "tipos": ["Water", "Psychic"]},
        {"id": 81, "nome": "Magnemite", "tipos": ["Electric", "Steel"]},
        {"id": 82, "nome": "Magneton", "tipos": ["Electric", "Steel"]},
        {"id": 83, "nome": "Farfetch'd", "tipos": ["Normal", "Flying"]},
        {"id": 84, "nome": "Doduo", "tipos": ["Normal", "Flying"]},
        {"id": 85, "nome": "Dodrio", "tipos": ["Normal", "Flying"]},
        {"id": 86, "nome": "Seel", "tipos": ["Water"]},
        {"id": 87, "nome": "Dewgong", "tipos": ["Water", "Ice"]},
        {"id": 88, "nome": "Grimer", "tipos": ["Poison"]},
        {"id": 89, "nome": "Muk", "tipos": ["Poison"]},
        {"id": 90, "nome": "Shellder", "tipos": ["Water"]},
        {"id": 91, "nome": "Cloyster", "tipos": ["Water", "Ice"]},
        {"id": 92, "nome": "Gastly", "tipos": ["Ghost", "Poison"]},
        {"id": 93, "nome": "Haunter", "tipos": ["Ghost", "Poison"]},
        {"id": 94, "nome": "Gengar", "tipos": ["Ghost", "Poison"]},
        {"id": 95, "nome": "Onix", "tipos": ["Rock", "Ground"]},
        {"id": 96, "nome": "Drowzee", "tipos": ["Psychic"]},
        {"id": 97, "nome": "Hypno", "tipos": ["Psychic"]},
        {"id": 98, "nome": "Krabby", "tipos": ["Water"]},
        {"id": 99, "nome": "Kingler", "tipos": ["Water"]},
        {"id": 100, "nome": "Voltorb", "tipos": ["Electric"]},
        {"id": 101, "nome": "Electrode", "tipos": ["Electric"]},
        {"id": 102, "nome": "Exeggcute", "tipos": ["Grass", "Psychic"]},
        {"id": 103, "nome": "Exeggutor", "tipos": ["Grass", "Psychic"]},
        {"id": 104, "nome": "Cubone", "tipos": ["Ground"]},
        {"id": 105, "nome": "Marowak", "tipos": ["Ground"]},
        {"id": 106, "nome": "Hitmonlee", "tipos": ["Fighting"]},
        {"id": 107, "nome": "Hitmonchan", "tipos": ["Fighting"]},
        {"id": 108, "nome": "Lickitung", "tipos": ["Normal"]},
        {"id": 109, "nome": "Koffing", "tipos": ["Poison"]},
        {"id": 110, "nome": "Weezing", "tipos": ["Poison"]},
        {"id": 111, "nome": "Rhyhorn", "tipos": ["Ground", "Rock"]},
        {"id": 112, "nome": "Rhydon", "tipos": ["Ground", "Rock"]},
        {"id": 113, "nome": "Chansey", "tipos": ["Normal"]},
        {"id": 114, "nome": "Tangela", "tipos": ["Grass"]},
        {"id": 115, "nome": "Kangaskhan", "tipos": ["Normal"]},
        {"id": 116, "nome": "Horsea", "tipos": ["Water"]},
        {"id": 117, "nome": "Seadra", "tipos": ["Water"]},
        {"id": 118, "nome": "Goldeen", "tipos": ["Water"]},
        {"id": 119, "nome": "Seaking", "tipos": ["Water"]},
        {"id": 120, "nome": "Staryu", "tipos": ["Water"]},
        {"id": 121, "nome": "Starmie", "tipos": ["Water", "Psychic"]},
        {"id": 122, "nome": "Mr. Mime", "tipos": ["Psychic", "Fairy"]},
        {"id": 123, "nome": "Scyther", "tipos": ["Bug", "Flying"]},
        {"id": 124, "nome": "Jynx", "tipos": ["Ice", "Psychic"]},
        {"id": 125, "nome": "Electabuzz", "tipos": ["Electric"]},
        {"id": 126, "nome": "Magmar", "tipos": ["Fire"]},
        {"id": 127, "nome": "Pinsir", "tipos": ["Bug"]},
        {"id": 128, "nome": "Tauros", "tipos": ["Normal"]},
        {"id": 129, "nome": "Magikarp", "tipos": ["Water"]},
        {"id": 130, "nome": "Gyarados", "tipos": ["Water", "Flying"]},
        {"id": 131, "nome": "Lapras", "tipos": ["Water", "Ice"]},
        {"id": 132, "nome": "Ditto", "tipos": ["Normal"]},
        {"id": 133, "nome": "Eevee", "tipos": ["Normal"]},
        {"id": 134, "nome": "Vaporeon", "tipos": ["Water"]},
        {"id": 135, "nome": "Jolteon", "tipos": ["Electric"]},
        {"id": 136, "nome": "Flareon", "tipos": ["Fire"]},
        {"id": 137, "nome": "Porygon", "tipos": ["Normal"]},
        {"id": 138, "nome": "Omanyte", "tipos": ["Rock", "Water"]},
        {"id": 139, "nome": "Omastar", "tipos": ["Rock", "Water"]},
        {"id": 140, "nome": "Kabuto", "tipos": ["Rock", "Water"]},
        {"id": 141, "nome": "Kabutops", "tipos": ["Rock", "Water"]},
        {"id": 142, "nome": "Aerodactyl", "tipos": ["Rock", "Flying"]},
        {"id": 143, "nome": "Snorlax", "tipos": ["Normal"]},
        {"id": 144, "nome": "Articuno", "tipos": ["Ice", "Flying"]},
        {"id": 145, "nome": "Zapdos", "tipos": ["Electric", "Flying"]},
        {"id": 146, "nome": "Moltres", "tipos": ["Fire", "Flying"]},
        {"id": 147, "nome": "Dratini", "tipos": ["Dragon"]},
        {"id": 148, "nome": "Dragonair", "tipos": ["Dragon"]},
        {"id": 149, "nome": "Dragonite", "tipos": ["Dragon", "Flying"]},
        {"id": 150, "nome": "Mewtwo", "tipos": ["Psychic"]},
        {"id": 151, "nome": "Mew", "tipos": ["Psychic"]},
    ]
    for i, data in enumerate(sorted(pokemon_data, key=lambda x: x["id"]), start=1):
        pokemon = criar_pokemon(i, data["nome"], data["tipos"])
        pokedex.adicionar_pokemon_registro(pokemon)
    return pokedex


def menu_principal(treinadores: list, pokedex: Pokedex):
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Selecionar treinador")
        print("2. Criar novo treinador")
        print("3. Apagar treinador")
        print("4. Sair")
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            if not treinadores:
                print("Nenhum treinador cadastrado.")
                continue
            print("\nTreinadores disponíveis:")
            for i, t in enumerate(treinadores):
                print(f"{i+1}. {t.nome}")
            try:
                idx = int(input("Escolha o número do treinador: ")) - 1
                if 0 <= idx < len(treinadores):
                    menu_treinador(treinadores[idx], pokedex)
                else:
                    print("Número inválido.")
            except ValueError:
                print("Entrada inválida.")
        elif opcao == "2":
            nome = input("Digite o nome do novo treinador: ").strip()
            if nome:
                treinadores.append(Treinador(nome))
                print(f"Treinador {nome} criado.")
            else:
                print("Nome inválido.")
        elif opcao == "3":
            if not treinadores:
                print("Nenhum treinador para apagar.")
                continue
            print("\nTreinadores disponíveis:")
            for i, t in enumerate(treinadores):
                print(f"{i+1}. {t.nome}")
            try:
                idx = int(input("Escolha o número do treinador para apagar: ")) - 1
                if 0 <= idx < len(treinadores):
                    nome = treinadores[idx].nome
                    del treinadores[idx]
                    print(f"Treinador {nome} apagado.")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Entrada inválida.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")


def menu_treinador(treinador: Treinador, pokedex: Pokedex):
    while True:
        print(f"\n=== MENU DE {treinador.nome.upper()} ===")
        print("1. Capturar Pokémon")
        print("2. Gerenciar Boxes")
        print("3. Consultar Pokédex")
        print("4. Modificar nome")
        print("5. Demonstrar Ataque Especial")
        print("6. Voltar")
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            capturar(treinador, pokedex)
        elif opcao == "2":
            menu_boxes(treinador.pcbox)
        elif opcao == "3":
            treinador.consultar_pokedex(pokedex)
        elif opcao == "4":
            novo_nome = input("Digite o novo nome: ").strip()
            if novo_nome:
                treinador.nome = novo_nome
                print("Nome modificado.")
            else:
                print("Nome inválido.")
        elif opcao == "5":
            if treinador.pcbox.listar_pokemons():
                pokemon = random.choice(treinador.pcbox.listar_pokemons())
                treinador.demonstrar_ataque(pokemon)
            else:
                print("Nenhum Pokémon capturado para demonstrar ataque.")
        elif opcao == "6":
            break
        else:
            print("Opção inválida.")


def capturar(treinador: Treinador, pokedex: Pokedex):
    disponiveis = [p for p in pokedex.registro_total.values() if p.id not in treinador.capturados]
    if not disponiveis:
        print("Todos os pokémons já foram capturados!")
        return
    

    
    import random
    pokemon = random.choices(disponiveis)[0]
    
    if treinador.pcbox.armazenar_pokemon(pokemon):
        treinador.registrar_captura(pokemon.id)
        print(f"✓ Você encontrou e capturou {pokemon.nome} (ID: {pokemon.id})!")
    else:
        print("✗ Boxes cheios! Não foi possível capturar.")


def menu_boxes(pcbox: PCBox):
    while True:
        print("\n=== GERENCIAR BOXES ===")
        boxes = pcbox.listar_boxes()
        for box in boxes:
            print(f"Box {box.id}: {len(box.pokemons)}/30 pokémons")
        print("0. Voltar")
        try:
            box_id = int(input("Escolha o número da box (1-16) ou 0 para voltar: "))
            if box_id == 0:
                break
            if 1 <= box_id <= 16:
                menu_box(boxes[box_id-1], pcbox)
            else:
                print("Box inválida.")
        except ValueError:
            print("Entrada inválida.")


def menu_box(box: 'Boxes', pcbox: PCBox):
    while True:
        print(f"\n=== BOX {box.id} ===")
        print("1. Listar Pokémons")
        print("2. Mover Pokémon")
        print("3. Liberar Pokémon")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            pokemons = box.listar_pokemons()
            if not pokemons:
                print("Box vazia.")
            else:
                for i, p in enumerate(pokemons):
                    print(f"{i+1}. {p.nome} (ID: {p.id})")
        elif opcao == "2":
            mover(box, pcbox)
        elif opcao == "3":
            liberar(box, pcbox)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")


def mover(box_origem: 'Boxes', pcbox: PCBox):
    pokemons = box_origem.listar_pokemons()
    if not pokemons:
        print("Box vazia.")
        return
    print("Pokémons na box:")
    for i, p in enumerate(pokemons):
        print(f"{i+1}. {p.nome} (ID: {p.id})")
    try:
        idx = int(input("Escolha o número do Pokémon para mover: ")) - 1
        if 0 <= idx < len(pokemons):
            pokemon = pokemons[idx]
            boxes = pcbox.listar_boxes()
            print("Boxes disponíveis:")
            for b in boxes:
                if b.id != box_origem.id:
                    print(f"{b.id}. Box {b.id} ({len(b.pokemons)}/30)")
            dest_id = int(input("Escolha a box destino: "))
            if 1 <= dest_id <= 16 and dest_id != box_origem.id:
                if pcbox.mover_pokemon(pokemon, box_origem.id, dest_id):
                    print(f"✓ {pokemon.nome} movido para Box {dest_id}.")
                else:
                    print("Erro ao mover.")
            else:
                print("Box inválida.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")


def liberar(box: 'Boxes', pcbox: PCBox):
    pokemons = box.listar_pokemons()
    if not pokemons:
        print("Box vazia.")
        return
    print("Pokémons na box:")
    for i, p in enumerate(pokemons):
        print(f"{i+1}. {p.nome} (ID: {p.id})")
    try:
        idx = int(input("Escolha o número do Pokémon para liberar: ")) - 1
        if 0 <= idx < len(pokemons):
            pokemon = pokemons[idx]
            idx_global = pcbox.armazenamento.index(pokemon)
            pcbox.remover_pokemon(idx_global)
            print(f"✓ {pokemon.nome} liberado!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")


def main():
    pokedex = criar_pokedex_global()
    ash = Treinador("Ash")
    misty = Treinador("Misty")
    
    ash_pokemons = [
(1, "Bulbasaur", ["Grass", "Poison"]),
(4, "Charmander", ["Fire"]),
(5, "Charmeleon", ["Fire"]),
(6, "Charizard", ["Fire", "Flying"]),
(7, "Squirtle", ["Water"]),
(10, "Caterpie", ["Bug"]),
(11, "Metapod", ["Bug"]),
(12, "Butterfree", ["Bug", "Flying"]),
(16, "Pidgey", ["Normal", "Flying"]),
(17, "Pidgeotto", ["Normal", "Flying"]),
(18, "Pidgeot", ["Normal", "Flying"]),
(25, "Pikachu", ["Electric"]),
(98, "Krabby", ["Water"]),
(99, "Kingler", ["Water"]),
(106, "Hitmonlee", ["Fighting"]),
(107, "Hitmonchan", ["Fighting"]),
(110, "Weezing", ["Poison"]),
(115, "Kangaskhan", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(128, "Tauros", ["Normal"]),
(130, "Gyarados", ["Water", "Flying"]),
(131, "Lapras", ["Water", "Ice"]),
(143, "Snorlax", ["Normal"]),
(144, "Articuno", ["Ice", "Flying"]),
(145, "Zapdos", ["Electric", "Flying"]),
(146, "Moltres", ["Fire", "Flying"]),
(151, "Mew", ["Psychic"])
]
    
    for id_p, nome, tipos in ash_pokemons:
        pokemon = criar_pokemon(id_p, nome, tipos)
        ash.pcbox.armazenar_pokemon(pokemon)
        ash.registrar_captura(id_p)
    
    treinadores = [ash, misty]
    menu_principal(treinadores, pokedex)


if __name__ == "__main__":
    main()
