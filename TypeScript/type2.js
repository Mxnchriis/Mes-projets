var Pays = /** @class */ (function () {
    function Pays(nom, superficie, capitale) {
        this.nom = nom;
        this.superficie = superficie;
        this.capitale = capitale;
    }
    Pays.prototype.presentation = function () {
        console.log("".concat(this.nom, " a une superficie de ").concat(this.superficie, " km\u00B2 et sa capitale est ").concat(this.capitale, "."));
    };
    return Pays;
}());
var Continent = /** @class */ (function () {
    function Continent(nom, pays) {
        this.nom = nom;
        this.pays = pays;
    }
    Continent.prototype.getNbPays = function () {
        return this.pays.length;
    };
    Continent.prototype.affichePays = function () {
        this.pays.forEach(function (pays) { return pays.presentation(); });
    };
    Continent.prototype.ajouterPays = function (nouveauPays) {
        this.pays.push(nouveauPays);
    };
    return Continent;
}());
var france = new Pays("France", 67000, "Paris");
var espagne = new Pays("Espagne", 505990, "Madrid");
var europe = new Continent("Europe", [france, espagne]);
var italie = new Pays("Italie", 301340, "Rome");
// europe.ajouterPays(italie);
console.log("Nombre de pays dans ".concat(europe.nom, " : ").concat(europe.getNbPays()));
europe.affichePays();
