let globalVar = "I am global!";

function display() {
    console.log(globalVar);
}

display();
console.log(globalVar);

// separate cases
console.log();

function localExample() {
    let localVar = "I am local!";
    console.log(localVar);
}
localExample();