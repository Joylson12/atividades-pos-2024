import { useState, useEffect } from 'react';

function App() {
  const [allPokemons, setAllPokemons] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const pokemonsPerPage = 10;

  const loadPokemons = async () => {
    try {
      const response = await fetch('https://pokeapi.co/api/v2/pokemon?limit=100');
      const data = await response.json();
      setAllPokemons(data.results);
      setCurrentPage(1);
    } catch (error) {
      console.error('Erro ao buscar os Pokémon:', error);
      alert('Não foi possível carregar os Pokémon.');
    }
  };

  const getPaginatedPokemons = () => {
    const start = (currentPage - 1) * pokemonsPerPage;
    const end = start + pokemonsPerPage;
    return allPokemons.slice(start, end);
  };

  const changePage = (direction) => {
    setCurrentPage((prevPage) => prevPage + direction);
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4">Pokédex do Jowl</h1>
      <div className="d-grid gap-2 col-6 mx-auto">
        <button onClick={loadPokemons} className="btn btn-success btn-lg">
          Carregar Todos os Pokémons
        </button>
      </div>

      <div className="mt-4">
        {getPaginatedPokemons().map((pokemon) => (
          <div key={pokemon.name} className="pokemon-card p-3">
            <p className="pokemon-name"><strong>Nome:</strong> {pokemon.name}</p>
          </div>
        ))}
      </div>

      <div className="d-flex justify-content-center mt-4">
        <button
          onClick={() => changePage(-1)}
          className="btn btn-success"
          disabled={currentPage === 1}
        >
          Anterior
        </button>
        <button
          onClick={() => changePage(1)}
          className="btn btn-success"
          disabled={(currentPage * pokemonsPerPage) >= allPokemons.length}
        >
          Próximo
        </button>
      </div>
    </div>
  );
}

export default App;
