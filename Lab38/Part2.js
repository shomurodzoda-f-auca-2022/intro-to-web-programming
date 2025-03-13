let user = {
    name: "John",
    age: 12
};
console.log("User Details: " + user);

//separate cases
console.log();

try {
    throw new Error("Something went wrong");
} catch (error) {
    console.error(error);
}

//separate cases
console.log();

const users = [
    {id: 1, name: "John", age: 12},
    {id: 2, name: "Alice", age: 22},
    {id: 3, name: "Michael", age: 32},
]
console.table(users);