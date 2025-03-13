function fetchData() {
  return new Promise((resolve, reject) => {
    const isSuccess = Math.random() > 0.5;

    setTimeout(() => {
      if (isSuccess) {
        resolve("Data received");
      } else {
        reject("Error: Failed to fetch data");
      }
    }, 2000);
  });
}

fetchData()
  .then((result) => console.log(result))
  .catch((error) => console.error(error))
  .finally(() => console.log("Request completed"));
