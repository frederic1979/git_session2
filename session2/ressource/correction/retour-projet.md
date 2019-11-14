# Les retours globaux sur le projet Station Météo

## Modularisez votre code

Lorsque vous avez du code qui se répète, c'est que c'est le bon moment d'écrire une fonction.

Par exemple pour rajouter une mesure dans le DOM on peut faire :

```javascript
function loadMeasureInDom(parentElementName, measure, title) {
  // Transformation de la date en objet Date
  const measureDate = new Date(measure.measureDate);

  // Creation de la div qui contiendra ma mesure
  const packingElement = document.createElement('div');
  document.getElementById(parentElementName).appendChild(packingElement);

  // Creation du titre de la mesure
  const titleElement = document.createElement('h2');
  titleElement.textContent = title + measureDate.toLocaleDateString();
  packingElement.appendChild(titleElement);

  // Creation des éléments HTML qui contiendront les détails de ma mesure
  const ulMeasures = document.createElement('ul');
  const liTemperature = document.createElement('li');
  const liHumidity = document.createElement('li');
  const liPressure = document.createElement('li');

  // Remplissage des éléments li avec les détails de ma mesure
  liTemperature.textContent = 'Température : ' + measure.temperature + ' °C';
  liHumidity.textContent = 'Humidité : ' + measure.humidity + ' %hum';
  liPressure.textContent = 'Pression : ' + measure.pressure + ' hPa';

  // Ajout des éléments li au ul parent
  ulMeasures.appendChild(liTemperature);
  ulMeasures.appendChild(liHumidity);
  ulMeasures.appendChild(liPressure);

  // Ajout du ul contenant les détails au div parent
  packingElement.appendChild(ulMeasures);
}
```

_Pourquoi ?_ Parce que cela permet d'éviter de répéter plusieurs fois ce même code. Si vous avez besoin ensuite de changer l'affichage, ce sera facile d'avoir le **même comportement** pour toutes les mesures.

## Choisissez des noms de variables parlants

Choisissez des noms de variables qui ont du sens !

```javascript
// Mauvais exemple
const a = measureDate.substring(0, 3);

// Bon exemple
const measureDateYear = measureDate.substring(0, 3);
```

_Pourquoi ?_ Parce que ce sera beaucoup plus facile par la suite de comprendre votre code.

## Formattez votre code (utilisez l'IDE)

Dans VS Code ou dans IntelliJ, utilisez les **raccouris clavier** pour mettre en forme votre code facilement.

```javascript
// Mauvais exemple
let result = 1;
for (let counter = 0; counter < 10; counter = counter + 1) {
result = result * 2;
}

// Un autre mauvais exemple
let result = 1;
  for (let counter = 0; counter < 10; counter = counter + 1) {
    result = result * 2;
      }


// Bon exemple
let result = 1;
for (let counter = 0; counter < 10; counter = counter + 1) {
  result = result * 2;
}
```

_Pourquoi ?_ Parce que c'est beaucoup plus facile à lire !

## Rendez votre code résilient

Il est important de coder dès le début pensant à la **résilience** de votre code. Vous devez **éviter** au maximum de faire des **hypothèses** lorsque vous codez sur la taille des tableaux, la longueur des chaînes de caractères, ...

Vous devez dès le départ penser aux cas d'utilisation qui ne sont peut-être pas encore arrivés.

Par exemple, ne comptez pas sur un nombre précis d'éléments d'un tableau.

```javascript
// Exemple risqué
const oUl = document.getElementById("temperature");
const liOfUl = oUl.getElementsByTagName("li");
// Comment savoir ici que j'aurais forcément au moins 4 éléments ?
if (liOfUl.length > 0) {
  const liToDelete1 = liOfUl[liOfUl.length - 4];
  const liToDelete2 = liOfUl[liOfUl.length - 3];
  const liToDelete3 = liOfUl[liOfUl.length - 2];
  const liToDelete4 = liOfUl[liOfUl.length - 1];

  oUl.removeChild(liToDelete1);
  oUl.removeChild(liToDelete2);
  oUl.removeChild(liToDelete3);
  oUl.removeChild(liToDelete4);
}

// Exemple sans risque
const temperatureList = document.getElementById("temperature");
while (oUl.firstChild) {
  oUl.removeChild(elementToClean.firstChild);
}
```

## Utilisez les templates strings

```javascript
const prenom = 'Bernard';
const nom = 'Hugueney';

console.log(`Le plus fort en Java c'est ${prenom} ${nom}`);
```

_Pourquoi ?_ Parce que c'est plus facile à lire !

## Commentez le code

```javascript
// No comment
```

## Soyez consistent

- Choisissez si vous utilisez des `"` ou `'` pour délimiter les chaines de caractères (mais pas les deux)
- Mettez toujours des `;` à la fin des lignes
- Nommez tout en français ou tout en anglais (mais pas de frenghlish)
- Choisissez la même indentation partout (2 ou 4 espaces)
