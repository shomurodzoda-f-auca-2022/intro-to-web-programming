// Task 1
let globalVar = "Hello from global";
function display1() {
    console.log(globalVar);
}
display1();

// Task 2
// separate cases
console.log();

function display2 () {
    let localVar = "Hello from global";
    console.log(localVar);
}
display2();

// Task 3
// separate cases
console.log();

function display3() {
    let localVar = "Hello from global";
    console.log(localVar);
}
display3();
// console.log(localVar); gives an error