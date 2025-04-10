document.addEventListener("DOMContentLoaded", () => {
    // Dark mode toggle
    const toggleDarkMode = document.getElementById("dark-mode-toggle");
    if (toggleDarkMode) {
        toggleDarkMode.addEventListener("click", () => {
            document.body.classList.toggle("dark-mode");
            // Save user preference
            localStorage.setItem("darkMode", document.body.classList.contains("dark-mode"));
        });
    }

    // Initialize dark mode from localStorage
    if (localStorage.getItem("darkMode") === "true") {
        document.body.classList.add("dark-mode");
    }

    // Form submission handling
    const addTaskForm = document.getElementById("add-task-form");
    if (addTaskForm) {
        addTaskForm.addEventListener("submit", (e) => {
            // Form validation
            const taskInput = document.getElementById("task-title");
            if (taskInput.value.trim() === "") {
                e.preventDefault();
                taskInput.classList.add("is-invalid");
                return;
            }
        });
    }

    // Dynamic task interactions
    document.addEventListener("click", (e) => {
        // Complete task button
        if (e.target.closest(".complete-btn")) {
            const taskItem = e.target.closest("li");
            taskItem.classList.toggle("completed-task");
        }

        // Delete task button
        if (e.target.closest(".delete-btn")) {
            const taskItem = e.target.closest("li");
            taskItem.classList.add("fade-out");
            setTimeout(() => taskItem.remove(), 300);
        }
    });

    // Animation initialization
    const animateElements = document.querySelectorAll(".fade-in");
    animateElements.forEach(element => {
        element.style.opacity = 0;
        setTimeout(() => {
            element.style.transition = "opacity 0.5s ease-out";
            element.style.opacity = 1;
        }, 50);
    });
});