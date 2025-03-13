console.log("Before timeout");
setTimeout(() => { console.log("Executed after 3 seconds"); }, 3000);
console.log("After timeout");

//separate cases
console.log();

let count = 0;
let interval = setInterval(() => {
    count++;
    console.log("Interval execution:", count);

    if (count === 3) {
        clearInterval(interval);
    }
}, 1000);