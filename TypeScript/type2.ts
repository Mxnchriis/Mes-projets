class Pays {
    constructor(
        public readonly nom: string,
        public readonly superficie: number,
        public readonly capitale: string
    ) {}
    
    presentation(): void {
        console.log(`${this.nom} a une superficie de ${this.superficie} km² et sa capitale est ${this.capitale}.`);
    }
}

class Continent {
    constructor(
        public readonly nom: string,
        private pays: Pays[]
    ) {}

    getNbPays(): number {
        return this.pays.length;
    }

    affichePays(): void {
        this.pays.forEach(pays => pays.presentation());
    }

    ajouterPays(nouveauPays: Pays): void {
        this.pays.push(nouveauPays);
    }    
}

const france = new Pays("France", 67000, "Paris");
const espagne = new Pays("Espagne", 505990, "Madrid");



const europe = new Continent("Europe", [france, espagne]);
const italie = new Pays("Italie", 301340, "Rome");
europe.ajouterPays(italie);
console.log(`Nombre de pays dans ${europe.nom} : ${europe.getNbPays()}`);
europe.affichePays();
