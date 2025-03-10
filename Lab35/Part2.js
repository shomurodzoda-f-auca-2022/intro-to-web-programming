let fruits = ["banana", "grape", "apple"];
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

// separate the cases
console.log();

let i = 0;
while (i < fruits.length) {
    console.log(fruits[i]);
    i++
}

// separate the cases
console.log();

fruits = ["banana", "grape", "apple", "potatoes", "pineapple"];
for (let i = 0; i < fruits.length; i++) {
    if (fruits[i] === "potatoes") {
        console.log("Oops, you pick vegetable!");
        break;
    }

    console.log(fruits[i]);
}

// separate the cases
console.log();

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
i = 0;
while (i < numbers.length) {
    if (numbers[i] % 5 === 0) {
        console.log(numbers[i] + " is divisible by 5.");
        i++;
        continue;
    }

    console.log(numbers[i]);
    i++;
}