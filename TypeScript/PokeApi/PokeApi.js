
async function ApiSearch(){
    try {
        let pokemon = document.getElementById("searchbar").value;
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon.toLowerCase()}`)

        console.log(pokemon);

        if (!response.ok){
            throw new Error(`${pokemon} isn't in the PokémonAPI databases, try something else`)
        }

        const data = await response.json();
        const pokemonSprite = data.sprites.front_default;
        const imgElement = document.getElementById("pokemonSprite")

        imgElement.src = pokemonSprite;
        imgElement.style.display = "block";

        // Masquer le message d'erreur si la recherche réussit
        const errorMessage = document.getElementById("errorMessage");
        errorMessage.style.display = "none";
        errorMessage.textContent = "";

        // Afficher les types du Pokémon
        const typesContainer = document.getElementById("pokemonTypes");
        typesContainer.innerHTML = ""; // Réinitialiser les types précédents
        
        data.types.forEach(typeData => {
            const typeDiv = document.createElement("div");
            const typeName = typeData.type.name;
            typeDiv.textContent = typeName.toUpperCase();
            typeDiv.className = `type-badge type-${typeName}`;
            typesContainer.appendChild(typeDiv);
        });
        
        typesContainer.style.display = "block";
    }
    catch (error) {
        console.error(error);
        // Masquer le sprite et les types en cas d'erreur
        document.getElementById("pokemonSprite").style.display = "none";
        document.getElementById("pokemonTypes").style.display = "none";
        
        // Afficher l'erreur dans le DOM
        const errorMessage = document.getElementById("errorMessage");
        errorMessage.textContent = error.message;
        errorMessage.style.display = "block";
        errorMessage.className = "error-message";
    }
}