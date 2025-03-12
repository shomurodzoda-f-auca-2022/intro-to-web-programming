let numbers = [1, 2, 3];
numbers.push(4);
let last = numbers.pop();
console.log(last);

// separate cases
console.log();

let fruits = ["banana", "apple", "kiwi", "melon"];
let someFruits = fruits.slice(1, 3);
console.log(someFruits);

// separate cases
console.log();

let doubled = numbers.map(x => x * 2);
console.log(doubled);

// separate cases
console.log();

let evens = numbers.filter(x => x % 2 === 0);
console.log(evens);