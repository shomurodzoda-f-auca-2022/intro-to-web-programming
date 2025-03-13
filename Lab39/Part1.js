console.log("Start");
for (let i = 0; i< 3; i++){
    console.log("Loop iteration:", i);
}
console.log("End");

//separate cases
console.log();

console.log("Start");
setTimeout( () => {
    console.log("Delayed Message");
}, 2000);
console.log("End");