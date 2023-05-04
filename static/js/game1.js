// Return the array of riddles
const getRiddlesArray = async () => {
    const response = await fetch('/riddles/getAllRiddles');
    return await response.json();
};
getRiddlesArray().then(riddles => {
    console.log(riddles);
});

// Return the exact number of riddles
const getRiddleNumber = async () => {
    const riddles = await getRiddlesArray();
    return riddles.length;
}
getRiddleNumber().then(riddlesLength => {
    console.log(riddlesLength);
});

// Pick a random number between 0 and riddles.length - 1
const pickANumber = async () => {
    const maxNumber = await getRiddleNumber() - 1;
    return Math.floor(Math.random() * (maxNumber + 1));
}
pickANumber().then(nb => {
    console.log(nb);
});

/* ------- Function handling the game ------- */
let correctAnswers = 0;

// Get a random riddle
const getRandomRiddle = async () => {
    const riddles = await getRiddlesArray();
    const randomIndex = await pickANumber();
    return riddles[randomIndex];
};

// Display the random riddle
const displayRiddle = async (riddle) => {
    // Description
    const riddleDescription = document.getElementById("riddleDescription");
    riddleDescription.innerHTML = ""; // Clear the contents of the riddleDescription element

    const riddleTitle = document.createElement("h2");
    riddleTitle.innerText = "Riddle";
    riddleDescription.appendChild(riddleTitle);

    const riddleText = document.createTextNode(riddle.description);
    riddleDescription.appendChild(riddleText);


    // Clues
    const clueButtons = document.getElementById("clueButtons");
    clueButtons.innerHTML = "";

    riddle.clues.forEach((clue, index) => {
        const clueButton = document.createElement("button");
        clueButton.innerText = `Show Clue ${index + 1}`;
        clueButton.className = 'btn-clue-game';
        clueButton.onclick = () => {
            Swal.fire({
                customClass: {
                    popup: 'popup'
                },
                title: 'Clue',
                text: clue.clueDescription,
                confirmButtonClass: 'swal2-confirm button-cool',
                confirmButtonText: 'Cool',
                buttonsStyling: false,
            });
        };
        clueButtons.appendChild(clueButton);
    });
};

// Answer checker
const checkAnswer = (userAnswer, correctAnswer) => {
    return userAnswer.trim().toLowerCase() === correctAnswer.trim().toLowerCase();
};

// Button Get random riddle
const getRandomRiddleButton = document.getElementById("getRandomRiddle");
getRandomRiddleButton.addEventListener("click", async () => {
    const riddle = await getRandomRiddle();
    await displayRiddle(riddle);

    const userAnswerField = document.getElementById("userAnswer");
    userAnswerField.className = 'answer-input';
    userAnswerField.placeholder = 'Your answer';
    const submitButton = document.getElementById("submitAnswer");
    submitButton.className = 'btn';

    submitButton.onclick = () => {
        const userAnswer = userAnswerField.value;
        const isCorrect = checkAnswer(userAnswer, riddle.solution);
        const message = document.getElementById("message");
        const correctAnswerCounter = document.getElementById("correctAnswerCounter");

        if (isCorrect) {
            correctAnswers++;
            message.innerText = "Well done!";
            if (correctAnswers === 3) {
                window.location.href = "/your_next_page_url";
            }
            correctAnswerCounter.innerText = `Consecutive correct answers: ${correctAnswers}`;
        } else {
            correctAnswers = 0;
            message.innerText = "Incorrect answer. Try again.";
            correctAnswerCounter.innerText = `Consecutive correct answers: ${correctAnswers}`;
        }
    };
    document.getElementById("riddleContainer").style.display = "block";
});
