document.addEventListener("DOMContentLoaded", function () {
    const ratingInputs = document.querySelectorAll(".star-rating input");
    ratingInputs.forEach((input) => {
        input.addEventListener("change", function () {
            console.log("Selected rating:", input.value);
        });
    });
});