function startCounter() {
    let counter = 1;

    const interval = setInterval(() => {
        console.log(`Counter: ${counter}`);
        counter++;

        if (counter > 5) {
          clearInterval(interval);
        }
    }, 1000);
}
startCounter();