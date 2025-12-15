# Sistema de Pokémon - PCBox com Pokédex

Um sistema escalável e orientado a objetos para gerenciar pokémons, captura e armazenamento baseado no diagrama UML fornecido.

## 📁 Estrutura do Projeto

```
POO-Topico-Pokemon/
├── src/
│   ├── __init__.py          # Importações do pacote
│   ├── pokemon.py           # Classe Pokemon
│   ├── pokedex.py           # Classe Pokedex
│   ├── pcbox.py             # Classes PCBox e Boxes
│   └── treinador.py         # Classe Treinador
├── data/                    # Pasta para dados (futuro uso)
├── main.py                  # Script principal
├── LICENSE                  # Licença do projeto
└── README.md               # Este arquivo
```

## 🎯 Classes Implementadas

### Pokemon
Representa um pokémon individual.

**Atributos:**
- `id` (int): Identificador único
- `nome` (str): Nome do pokémon
- `tipo` (str): Tipo (Fogo, Água, Planta, etc)

**Métodos principais:**
- `gerar_pokemon_aleatorio()`: Gera um pokémon aleatório para testes

### Pokedex
Gerencia o registro e captura de pokémons.

**Atributos:**
- `registro_total` (Dict): Todos os pokémons conhecidos
- `status_captura` (Set): IDs dos pokémons capturados

**Métodos principais:**
- `adicionar_pokemon_registro(pokemon)`: Adiciona pokémon ao registro
- `registrar_captura(id_pokemon)`: Marca como capturado
- `exibir_status()`: Mostra status de todos os pokémons
- `quantidade_capturados()`: Total de capturados
- `quantidade_total()`: Total conhecidos

### PCBox
Sistema de armazenamento com múltiplas caixas.

**Componentes:**
- **Boxes**: Caixa individual (máx. 30 pokémons)
- **PCBox**: Gerenciador com 18 caixas

**Métodos principais:**
- `armazenar_pokemon(pokemon)`: Adiciona pokémon na primeira caixa disponível
- `listar_pokemons()`: Retorna todos os pokémons armazenados
- `remover_pokemon(indice)`: Remove pokémon pelo índice
- `obter_espaco_total_disponivel()`: Espaço total em todas as caixas

### Treinador
Representa o jogador que captura pokémons.

**Atributos:**
- `nome` (str): Nome do treinador
- `pokedex` (Pokedex): Pokédex pessoal
- `pcbox` (PCBox): Armazenamento pessoal

**Métodos principais:**
- `consultar_pokedex(pokedex)`: Visualiza pokémons conhecidos
- `consultar_pcbox(pcbox)`: Visualiza pokémons armazenados

## 🚀 Como Usar

### Executar o Exemplo

```bash
python main.py
```

### Adicionar Pokémons

Edit a função `criar_pokedex_exemplo()` em `main.py`:

```python
def criar_pokedex_exemplo() -> Pokedex:
    pokedex = Pokedex()
    
    pokemons = [
        Pokemon(1, "Bulbasaur", "Planta"),
        Pokemon(4, "Charmander", "Fogo"),
        # ADICIONE MAIS AQUI!
        Pokemon(YOUR_ID, "SeuPokémon", "SeuTipo"),
    ]
    
    for pokemon in pokemons:
        pokedex.adicionar_pokemon_registro(pokemon)
    
    return pokedex
```

### Criar um Script Customizado

```python
from src import Pokemon, Pokedex, PCBox, Treinador

# Criar componentes
pokedex = Pokedex()
pcbox = PCBox()
treinador = Treinador("Seu Nome")

# Adicionar pokémons à pokédex
pokemon1 = Pokemon(1, "Meu Pokémon", "Fogo")
pokedex.adicionar_pokemon_registro(pokemon1)

# Simular captura
pcbox.armazenar_pokemon(pokemon1)
pokedex.registrar_captura(pokemon1.id)

# Consultar informações
treinador.consultar_pokedex(pokedex)
treinador.consultar_pcbox(pcbox)
```

## 🔄 Fluxo de Captura

1. **Encontrar Pokémon**: Sistema descobre um pokémon selvagem
2. **Capturar**: Pokémon é adicionado ao PCBox
3. **Registrar**: ID do pokémon é registrado na Pokédex
4. **Consultar**: Treinador pode visualizar status via Pokédex e PCBox

## 📊 Características Escaláveis

✅ **Fácil Adição de Pokémons**: Apenas adicione objetos Pokemon à lista
✅ **Múltiplos Treinadores**: Cada um tem sua própria Pokedex e PCBox
✅ **Sistema de Caixas**: 18 caixas com 30 espaços cada (540 total)
✅ **Rastreamento Eficiente**: Usa Dict e Set para busca O(1)
✅ **Extensível**: Adicione novos tipos, métodos especiais, etc.

## 💡 Ideias de Expansão

- [ ] Tipos de ataque e fraquezas
- [ ] Sistema de combate entre pokémons
- [ ] Evolução de pokémons
- [ ] Trades entre treinadores
- [ ] Salvar/carregar dados em arquivo JSON
- [ ] Interface gráfica (Tkinter/PyQt)
- [ ] API REST para multiplayer

## 📝 Licença

Veja o arquivo LICENSE para mais detalhes.

---

**Desenvolvido com ❤️ usando Python 3.8+**
