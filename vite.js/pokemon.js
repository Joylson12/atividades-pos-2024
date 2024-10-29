let allPokemons = [];
let currentPage = 1;
const pokemonsPerPage = 10;

export async function loadPokemons() {
    try {
        const url = 'https://pokeapi.co/api/v2/pokemon?limit=100';
        const response = await fetch(url);
        const data = await response.json();
        allPokemons = data.results;
        currentPage = 1;
        displayPokemons();
    } catch (error) {
        console.error('Erro ao buscar os Pokémon:', error);
        alert('Não foi possível carregar os Pokémon.');
    }
}

export async function createPokemonCard(pokemon) {
    const response = await fetch(pokemon.url);
    const pokemonData = await response.json();

    const pokemonContainer = document.getElementById('pokemon-container');
    const card = document.createElement('div');
    card.className = 'pokemon-card p-3';

    card.innerHTML = `
        <div class="pokemon-name">${pokemonData.name}</div>
        <p><strong>Altura:</strong> ${pokemonData.height} decímetros</p>
        <p><strong>Peso:</strong> ${pokemonData.weight} hectogramas</p>
        <p><strong>Tipos:</strong> ${pokemonData.types.map(type => type.type.name).join(', ')}</p>
        <p><strong>Habilidades:</strong> ${pokemonData.abilities.map(ability => ability.ability.name).join(', ')}</p>
    `;

    pokemonContainer.appendChild(card);
}

export function displayPokemons() {
    const pokemonContainer = document.getElementById('pokemon-container');
    pokemonContainer.innerHTML = '';

    const start = (currentPage - 1) * pokemonsPerPage;
    const end = start + pokemonsPerPage;

    const paginatedPokemons = allPokemons.slice(start, end);

    paginatedPokemons.forEach(createPokemonCard);

    document.getElementById('prev-btn').disabled = currentPage === 1;
    document.getElementById('next-btn').disabled = end >= allPokemons.length;
}

export function changePage(direction) {
    currentPage += direction;
    displayPokemons();
}
