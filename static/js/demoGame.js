// Helper Functions
const getRiddlesArray = async () => {
    const response = await fetch("/riddles/getAllRiddles");
    return await response.json();
};

const pickANumber = (maxNumber) => {
    return Math.floor(Math.random() * (maxNumber + 1));
};

const checkAnswer = (userAnswer, correctAnswer) => {
    return userAnswer.trim().toLowerCase() === correctAnswer.trim().toLowerCase();
};

// Game Logic
let correctAnswers = 0;
let incorrectAnswers = -1;
let lastRiddleId = null;

const updateCounters = () => {
    const correctAnswerCounter = document.getElementById("correctAnswerCounter");
    const incorrectAnswerCounter = document.getElementById("incorrectAnswerCounter");

    correctAnswerCounter.innerText = `Consecutive correct answers: ${correctAnswers}`;
    incorrectAnswerCounter.innerText = `Consecutive incorrect answers or skipped riddles: ${incorrectAnswers}`;
};

const getRandomRiddle = async () => {
    const riddles = await getRiddlesArray();

    if (riddles.length === 0) {
        return null;
    } else if (riddles.length === 1) {
        return riddles[0];
    }

    let randomIndex;

    do {
        randomIndex = pickANumber(riddles.length - 1);
    } while (lastRiddleId === riddles[randomIndex]);

    lastRiddleId = riddles[randomIndex];
    return riddles[randomIndex];
};

const displayRiddle = async (riddle) => {
    const riddleDescription = document.getElementById("riddleDescription");
    riddleDescription.innerHTML = "";

    const riddleTitle = document.createElement("h2");
    riddleTitle.innerText = "Riddle";
    riddleDescription.appendChild(riddleTitle);

    const riddleText = document.createTextNode(riddle.description);
    riddleDescription.appendChild(riddleText);

    const clueButtons = document.getElementById("clueButtons");
    clueButtons.innerHTML = "";

    riddle.clues.forEach((clue, index) => {
        const clueButton = document.createElement("button");
        clueButton.innerText = `Show Clue ${index + 1}`;
        clueButton.className = "btn-clue-game";
        clueButton.onclick = () => {
            Swal.fire({
                customClass: {
                    popup: "popup",
                },
                title: "Clue",
                text: clue.clueDescription,
                confirmButtonClass: "swal2-confirm button-cool",
                confirmButtonText: "Cool",
                buttonsStyling: false,
            });
        };
        clueButtons.appendChild(clueButton);
    });
};

const getRandomRiddleButton = document.getElementById("getRandomRiddle");
getRandomRiddleButton.addEventListener("click", async () => {
    const riddle = await getRandomRiddle();

    if (riddle === null) {
        alert("The site is still under construction. Please check back later for riddles.");
        return;
    }

    incorrectAnswers++;
    updateCounters();

    await displayRiddle(riddle);

    const userAnswerField = document.getElementById("userAnswer");
    userAnswerField.className = "answer-input";
    userAnswerField.placeholder = "Your answer";
    const submitButton = document.getElementById("submitAnswer");
    submitButton.className = "btn";

    submitButton.onclick = () => {
        const userAnswer = userAnswerField.value;
        const isCorrect = checkAnswer(userAnswer, riddle.solution);
        const message = document.getElementById("message");

        if (isCorrect) {
            correctAnswers++;
            incorrectAnswers = 0;
        } else {
            correctAnswers = 0;
            incorrectAnswers++;
        }
        updateCounters();
        const correctAnswerCounter = document.getElementById("correctAnswerCounter");

        if (isCorrect) {
            message.innerText = "Well done!";
            // Hide the riddle container after a correct answer
            document.getElementById("riddleContainer").style.display = "none";

            if (correctAnswers === 3) {
                window.location.href = "/your_next_page_url";
            }
            correctAnswerCounter.innerText = `Consecutive correct answers: ${correctAnswers}`;
        } else {
            message.innerText = "Incorrect answer. Try again.";
            correctAnswerCounter.innerText = `Consecutive correct answers: ${correctAnswers}`;
        }
    };
    userAnswerField.value = "";
    document.getElementById("message").innerText = "";

    document.getElementById("riddleContainer").style.display = "block";
});

updateCounters();

