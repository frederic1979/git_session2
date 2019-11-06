function ligneAleatoire() {
    // On récupère la liste des rangées
    const listeDesRangees = document.getElementsByClassName('rangee');
    // On en prend une au hasard pour ajouter la nouvelle boite
    return listeDesRangees.item(Math.floor(listeDesRangees.length * Math.random()));
}

// On s'abonne au clic sur le bouton ajouter boite
document.getElementById('ajouter-boite').addEventListener('click', function (event) {
    // On crée une nouvelle div
    const nouvelleBoite = document.createElement('div');
    // On ajoute la classe 'boite' à la div créée
    nouvelleBoite.classList.add('boite');
    // On ajoute la classe 'derniere' à la div créée
    nouvelleBoite.classList.add('derniere')

    // On randomise la taille des boites
    const size = Math.random();
    if (size > 0.66) {
        nouvelleBoite.classList.add('grosse');
    } else if (size < 0.33) {
        nouvelleBoite.classList.add('petite');
    }

    // On s'assure qu'aucune boite n'a la classe 'dernière'
    document.querySelectorAll('.boite').forEach(element => element.classList.remove('derniere'));
    
    // On ajoute la nouvlle boite à une ligne aléatoire
    ligneAleatoire().appendChild(nouvelleBoite);
});

// On s'abonne au clic sur le bouton supprimer boite
document.getElementById('supprimer-boite').addEventListener('click', function (event) {
    // On récupère une ligne aléatoire
    const uneLigneAleatoire = ligneAleatoire();
    // On récupère les boites de la ligne
    const lesBoitesDeLaRangee = uneLigneAleatoire.getElementsByClassName('boite');

    // Si on a effectivement des boites, alors on supprime la dernière
    if (lesBoitesDeLaRangee.length > 0) {
        const boiteASuppr = lesBoitesDeLaRangee[lesBoitesDeLaRangee.length - 1];
        uneLigneAleatoire.removeChild(boiteASuppr);
    }
});

// On liste toutes les boites lors du chargement de la page
const lesBoites = document.querySelectorAll('.boite');

// On affiche toutes les boites
for (let boite of lesBoites) {
    boite.addEventListener('click', function (event) {
        let taille = '';
        if (boite.classList.contains('petite'))
            taille += 'petite';
        else if (boite.classList.contains('grosse'))
            taille += 'GROSSE';

        console.log(`Vous avez cliqué sur une ${taille} boite`);
    });
}
