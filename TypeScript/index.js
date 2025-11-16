// Fonction générique pour obtenir le statut de capitale
var getStatutCapitale = function (estCapitale, pays) {
    return estCapitale
        ? "est la capitale de ".concat(pays)
        : "n'est pas la capitale de ".concat(pays);
};
// Fonction générique pour afficher les informations d'une ville
var afficherInfosVille = function (ville) {
    var statutCapitale = getStatutCapitale(ville.estCapitale, ville.pays);
    console.log("".concat(ville.nom, " a une population de ").concat(ville.population, " et ").concat(statutCapitale));
};
// Exemple d'utilisation
var paris = {
    nom: 'Paris',
    population: 2000000,
    estCapitale: true,
    pays: 'la France'
};
var lyon = {
    nom: 'Lyon',
    population: 500000,
    estCapitale: false,
    pays: 'la France'
};
afficherInfosVille(paris);
afficherInfosVille(lyon);
