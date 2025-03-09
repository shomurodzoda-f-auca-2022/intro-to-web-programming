let score = 85;
if (score >= 90){
    console.log("Grade: A");
} else if (score <= 90){
    console.log("Grade: B");
} else {
    console.log("Grade: C or below");
}

// separate the cases
console.log();

let day = 3;
switch (day){
    case 1: {
        console.log("Today is Monday!");
        break;
    }
    case 2: {
        console.log("Today is Tuesday!");
        break;
    }
    case 3: {
        console.log("Today is Wednesday!");
        break;
    }
    case 4: {
        console.log("Today is Thursday!");
        break;
    }
    case 5: {
        console.log("Today is Friday!");
        break;
    }
    case 6: {
        console.log("Today is Saturday!");
        break;
    }
    case 7: {
        console.log("Today is Sunday!");
        break;
    }
    default: {
        console.log("Not a valid day!");
    }
}

// separate the cases
console.log();

let isLoggedIn = true;
let welcomeMessage = isLoggedIn ? "Welcome to Your App!" : "Please log in!";
console.log(welcomeMessage);