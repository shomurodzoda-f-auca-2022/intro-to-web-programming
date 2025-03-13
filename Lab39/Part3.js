let myPromise = new Promise((resolve, reject) => {
    let success = true;

    setTimeout( () => {
        if (success) {
            resolve("Operation successful!");
        } else {
            reject("Operation failed!");
        }
    }, 2000)
});

myPromise
    .then((message) => console.log(message))
    .catch((err) => console.log(err))
    .finally(() => console.log("Promise completed"));