const input = document.getElementById("difficulty");

function increment() {
    if (input.value < input.max) {
        input.value = parseInt(input.value) + 1;
    }
}

function decrement() {
    if (input.value > input.min) {
        input.value = parseInt(input.value) - 1;
    }
}