let numbers = [1, 2, 3, 4, 5, 6, 7];

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] === 5) {
        continue; // we will not print the "5" per requirement of Lab
    }

    console.log(numbers[i]);
}