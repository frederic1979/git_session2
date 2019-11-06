
alert('Hello World');

function add() {
    const numberOne = prompt('Numéro 1 :');
    const numberTwo = prompt('Numéro 2 :');
    return Number(numberOne) + Number(numberTwo);
}

console.log(add());

function sortTable() {
    const numbers = []; 
    for (let index = 0; index < 5; index++) {
        numbers.push(prompt(`Numéro ${index + 1} :`));
    }
    numbers.sort();
    console.log(numbers);
}

sortTable();