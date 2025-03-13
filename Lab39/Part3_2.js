function fetchUserData() {
    return new Promise( ( resolve, reject ) => {
        setTimeout( () => {
            let success = true;
            if (success) {
                resolve({name: "Alice", age: 25});
            } else {
                reject("Failed to fetch user data");
            }
        }, 2000)
    });
}

fetchUserData()
    .then((userData) => console.log(userData))
    .catch((err) => console.log(err))
    .finally(() => console.log("Request successful!"));