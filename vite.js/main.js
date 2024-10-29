import { loadPokemons, changePage } from './pokemon.js';

document.getElementById('load-pokemons-btn').addEventListener('click', loadPokemons);
document.getElementById('prev-btn').addEventListener('click', () => changePage(-1));
document.getElementById('next-btn').addEventListener('click', () => changePage(1));
