const person = {
    name: "John",
    age: 25,
    occupation: "Farmer"
};
console.log(person.name);

// separate cases
console.log();

let keys = Object.keys(person);
let values = Object.values(person);

keys.forEach(key => {
    console.log(key + ": " + person[key]);
})