// Task 1
function createCounter() {
    let count = 0;
    return function () {
        count++;
        return count;
    }
}
const counter1 = createCounter();
console.log(counter1());
console.log(counter1());

// Task 2
// separate cases
console.log();

const counter2 = createCounter();
console.log(counter2());
console.log(counter2());