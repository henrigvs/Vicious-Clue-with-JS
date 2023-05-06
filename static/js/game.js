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

const getUser = async (userId) => {
    const response = await fetch(`/users/${userId}`);
    return await response.json();
}

// Get score from back end to update counter on webpage
const getTotalScore = async (userId) => {
    const response = await fetch(`/users/${userId}`);
    const userData = await response.json();
    return parseInt(userData.score);
};

// Send score to backend
const sendUserScore = async (userId, consecutiveCorrectAnswer, incorrectAnswers, correctAnswers, clueRequested) => {
    const userScore = {
        correctAnswer: correctAnswers,
        incorrectAnswers: incorrectAnswers,
        clueRequested: clueRequested,
        consecutiveSeriesOfThree: consecutiveCorrectAnswer,
    };
    console.log(userScore);

    const response = await fetch(`/users/setScore/${userId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userScore),
    });

    if (response.ok) {
        console.log('User data has been sent successfully');
    } else {
        console.error('Failed to send user data');
    }
};

(async () => {
    const userScores = await getUser(userId);

    let consecutiveCorrectAnswers = parseInt(userScores.consecutiveSeriesOfThree);
    let incorrectAnswers = parseInt(userScores.incorrectAnswers) - 1; // -1 to handle for selection that increment by 1
    let correctAnswers = parseInt(userScores.correctAnswer);
    let clueRequested = parseInt(userScores.clueRequested);
    let totalScore = await getTotalScore(userId);
    let lastRiddleId = null;

    const updateCounters = async () => {
    await sendUserScore(userId, consecutiveCorrectAnswers, incorrectAnswers, correctAnswers, clueRequested);

    const correctConsecutiveAnswerCounter = document.getElementById("correctConsecutiveAnswerCounter");
    const incorrectAnswerCounter = document.getElementById("incorrectAnswerCounter");
    const correctAnswerCounter = document.getElementById("totalCorrectAnswerCounter");
    const clueRequestedCounter = document.getElementById("totalClueRequested");
    const totalScoreCounter = document.getElementById("totalScore");

    // Update totalScore
    totalScore = await getTotalScore(userId);

    correctConsecutiveAnswerCounter.innerText = `Consecutive correct answers: ${consecutiveCorrectAnswers}`;
    incorrectAnswerCounter.innerText = `Incorrect answers or skipped riddles: ${incorrectAnswers}`;
    correctAnswerCounter.innerText = `Total correct answers: ${correctAnswers}`;
    clueRequestedCounter.innerText = `Total clues requested: ${clueRequested}`;
    totalScoreCounter.innerText = `Score: ${totalScore}`;
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
        } while (lastRiddleId === riddles[randomIndex].riddleId);

        lastRiddleId = riddles[randomIndex].riddleId;
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
                clueRequested++;
                updateCounters();
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
                consecutiveCorrectAnswers++;
                correctAnswers++;
                incorrectAnswers = 0;
            } else {
                consecutiveCorrectAnswers = 0;
                incorrectAnswers++;
            }
            updateCounters();
            const correctConsecutiveAnswerCounter = document.getElementById("correctConsecutiveAnswerCounter");

            if (isCorrect) {
                message.innerText = "Well done!";
                message.style.marginTop = "20px";
                // Hide the riddle container after a correct answer
                document.getElementById("riddleContainer").style.display = "none";

                correctConsecutiveAnswerCounter.innerText = `Consecutive correct answers: ${consecutiveCorrectAnswers}`;
            } else {
                message.innerText = "Incorrect answer. Try again.";
                correctConsecutiveAnswerCounter.innerText = `Consecutive correct answers: ${consecutiveCorrectAnswers}`;
            }
        };
        userAnswerField.value = "";
        document.getElementById("message").innerText = "";

        document.getElementById("riddleContainer").style.display = "block";
        document.getElementById("counterContainer").style.display = "block";
    });

    updateCounters();
})();


