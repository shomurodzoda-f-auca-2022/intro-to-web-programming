function divide (num1, num2) {
    if (num2 === 0) {
        throw new Error("Cannot divide by zero");
    }
    return num1 / num2;
}

let num1 = 12;
let num2 = 0;

try {
    console.log(divide(num1, num2));
} catch (error) {
    console.error(error);
}