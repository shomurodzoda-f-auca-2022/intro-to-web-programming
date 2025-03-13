try {
    let json = '{"name": "John", "age": 20}'
    let user = JSON.parse(json);
    console.log(user.name);
} catch (error) {
    console.error("Error Parsing JSON: " + error.message);
} finally {
    console.log("Parsing attempted is finished");
}