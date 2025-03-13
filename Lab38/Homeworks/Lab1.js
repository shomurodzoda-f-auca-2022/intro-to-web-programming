function parseJSON (jsonStr) {
    try {
       const parsedObject = JSON.parse(jsonStr);
        console.log(parsedObject);
    } catch (error) {
        console.error("Invalid JSON format");
    }
}

parseJSON('{"name": "Alice", "age": 42}');
parseJSON('{name: "Alice", age: 42}');