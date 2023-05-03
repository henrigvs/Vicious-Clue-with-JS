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

function createInitialClueInputs(clues) {
    for (const clue of clues) {
        addClue(clue.clueDescription);
    }
}

function addClue(clueDescription = "") { // Add the optional parameter
    const clueContainer = document.getElementById("clueContainer");
    const clueNumber = clueContainer.childElementCount + 1;

    const clueWrapper = document.createElement("div");
    clueWrapper.classList.add("clue-wrapper");
    clueWrapper.setAttribute("clue-number", clueNumber);

    const label = document.createElement("label");
    label.setAttribute("for", "clue-" + clueNumber);
    label.innerText = "Clue";

    const input = document.createElement("input");
    input.type = "text";
    input.id = "clue-" + clueNumber;
    input.size = "30";
    input.classList.add("new-value");
    input.value = clueDescription; // Set the initial value to the given clueDescription

    clueWrapper.appendChild(label);
    clueWrapper.appendChild(input);
    clueContainer.appendChild(clueWrapper);
}

function removeClue() {
    const clueContainer = document.getElementById("clueContainer");
    if (clueContainer.childElementCount > 1) {
        clueContainer.removeChild(clueContainer.lastChild);
    }
}

function submitRiddle() {
    const clues = [];
    const clueContainer = document.getElementById("clueContainer");

    for (const clueWrapper of clueContainer.children) {
        const input = clueWrapper.querySelector("input");
        clues.push(input.value);
    }

    const hiddenClues = document.querySelector(".hidden-clues");
    hiddenClues.value = JSON.stringify(clues);
}

document.getElementById("addClueButton").addEventListener("click", () => addClue()); // Call addClue without arguments
document.getElementById("removeClueButton").addEventListener("click", removeClue);
