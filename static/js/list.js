// Return the array of riddles
const getRiddlesArray = async () => {
    const response = await fetch('/riddles/getAllRiddles');
    return await response.json();
};

// for debug
getRiddlesArray().then(riddles => {
    console.log(riddles);
});

// Split riddles into chunks
function chunkArray(array, chunkSize) {
    const chunks = [];
    for (let i = 0; i < array.length; i += chunkSize) {
        chunks.push(array.slice(i, i + chunkSize));
    }
    return chunks;
}

// Pagination generator
function createPagination(riddlesChunks) {
    const pagination = document.querySelector('.pagination');
    pagination.innerHTML = ""; // Clear the pagination div

    riddlesChunks.forEach((chunk, index) => {
        const pageNumber = index + 1;
        const pageLink = document.createElement('a');
        pageLink.href = '#';
        pageLink.textContent = pageNumber;
        pageLink.addEventListener('click', async (e) => {
            e.preventDefault();
            await displayRiddles(riddlesChunks[index]);
        });

        pagination.appendChild(pageLink);
    });
}

// Load all riddles and create the chunks
(async () => {
    const allRiddles = await getRiddlesArray();
    const riddlesChunks = chunkArray(allRiddles, riddlesPerPage);
    await displayRiddles(riddlesChunks[0]);

    createPagination(riddlesChunks);
})();


// Display riddles
async function displayRiddles(riddles) {
    const tbody = document.querySelector('.center-aligned tbody');
    tbody.innerHTML = "";

    for (const riddle of riddles) {
        let row = document.createElement('tr');
        row.setAttribute('data-category', riddle.category);

        // Column Owner ID if admin logged
        if (userRole === "admin") {
            let ownerIdCell = document.createElement('td');
            let ownerLink = document.createElement('a');
            ownerLink.setAttribute('class', 'ownerId');
            ownerLink.setAttribute('href', `/UserManagement/userDetails/${riddle.ownerId}`);
            ownerLink.textContent = riddle.ownerId;
            ownerIdCell.appendChild(ownerLink);
            row.appendChild(ownerIdCell);
        }

        // Column Riddles description
        let descriptionCell = document.createElement('td');
        descriptionCell.textContent = riddle.description;
        row.appendChild(descriptionCell);

        // Column Riddles solution
        let solutionCell = document.createElement('td');
        let solutionButton = document.createElement('button');
        solutionButton.setAttribute('id', 'sweetalert');
        solutionButton.setAttribute('class', 'btn-solution');
        solutionButton.setAttribute('solution', riddle.solution);
        solutionButton.textContent = 'show solution';
        solutionCell.appendChild(solutionButton);
        row.appendChild(solutionCell);

        // Column Riddles difficulty
        let difficultyCell = document.createElement('td');
        difficultyCell.setAttribute('class', 'col-difficulty');
        let decreaseButton = document.createElement('button');
        decreaseButton.setAttribute('class', 'btn-difficulty');
        decreaseButton.setAttribute('data-action', 'decrease');
        decreaseButton.setAttribute('value', riddle.riddleId);
        decreaseButton.textContent = '-';
        difficultyCell.appendChild(decreaseButton);

        let difficultySpan = document.createElement('span');
        difficultySpan.setAttribute('id', `difficulty-${riddle.riddleId}`);
        difficultySpan.textContent = riddle.difficulty;
        difficultyCell.appendChild(difficultySpan);

        let increaseButton = document.createElement('button');
        increaseButton.setAttribute('class', 'btn-difficulty');
        increaseButton.setAttribute('data-action', 'increase');
        increaseButton.setAttribute('value', riddle.riddleId);
        increaseButton.textContent = '+';
        difficultyCell.appendChild(increaseButton);
        row.appendChild(difficultyCell);

        // Column Riddles category
        let categoryCell = document.createElement('td');
        categoryCell.setAttribute('class', 'col-category');
        categoryCell.textContent = riddle.category;
        row.appendChild(categoryCell);

        // Column button edit
        let editCell = document.createElement('td');
        let editForm = document.createElement('form');
        editForm.setAttribute('action', `/edit/${riddle.riddleId}`);
        editForm.setAttribute('method', 'POST');
        let editButton = document.createElement('button');
        editButton.setAttribute('class', 'btn-modify');
        editButton.setAttribute('type', 'submit');
        editButton.textContent = 'Edit';
        editForm.appendChild(editButton);
        editCell.appendChild(editForm);
        row.appendChild(editCell);

        // Column button delete
        if (userRole === "admin") {
            let deleteCell = document.createElement('td');
            let deleteButton = document.createElement('button');
            deleteButton.setAttribute('class', 'btn-delete');
            deleteButton.setAttribute('data-remaining-riddle', riddle.remainingRiddle);
            deleteButton.setAttribute('value', riddle.riddleId);
            deleteButton.textContent = 'Delete';
            deleteCell.appendChild(deleteButton);
            row.appendChild(deleteCell);
        }

        tbody.appendChild(row);
    }
}

async function updateDifficulty(riddleId, action) {
    const response = await fetch(`/edit/updateDifficulty/${riddleId}`, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({action: action})
    });

    if (!response.ok) {
        throw new Error("Failed to update difficulty");
    }

    console.log("Difficulty updated");
    return response.json();
}

async function deleteRiddle(riddleId) {
    const response = await fetch(`/riddles/delete/${riddleId}`, {
        method: "DELETE"
    });

    if (!response.ok) {
        throw new Error("Failed to delete riddle");
    }
    console.log("Riddle deleted");
}

// events functions
function handleSolutionClick(event) {
    const solution = event.target.getAttribute('solution');
    Swal.fire({
        customClass: {
            popup: 'popup'
        },
        title: 'solution',
        text: solution,
        confirmButtonClass: 'swal2-confirm button-cool',
        confirmButtonText: 'Cool',
        buttonsStyling: false,
    });
    console.log("Solution button clicked");
}

async function handleDifficultyClick(event) {
    const action = event.target.dataset.action;
    const riddleId = event.target.value;

    try {
        const data = await updateDifficulty(riddleId, action);
        const difficultyValue = document.getElementById(`difficulty-${riddleId}`);
        difficultyValue.innerText = data.newDifficulty;
        console.log("Difficulty handler button clicked");
    } catch (error) {
        console.error(error);
    }
}

async function handleDeleteClick(event) {
    const riddleId = event.target.value;
    let remainingRiddle = parseInt(event.target.dataset.remainingRiddle);

    try {
        await deleteRiddle(riddleId);
        await filterRiddlesByCategory(document.getElementById("category-filter").value);
        event.target.closest("tr").remove();
        remainingRiddle--;

        if (remainingRiddle < 1) {
            window.location.href = emptyListURL;
        } else if (remainingRiddle % 5 === 0) {
            let page = remainingRiddle / 5;
            window.location.href = `/list/${page}`;
        }
    } catch (error) {
        console.error(error);
    }
}

// event delegation
document.addEventListener("click", (event) => {
    if (event.target.matches(".btn-solution")) {
        handleSolutionClick(event);
    } else if (event.target.matches(".btn-difficulty")) {
        handleDifficultyClick(event);
    } else if (event.target.matches(".btn-delete")) {
        handleDeleteClick(event).then(() => console.log("Button delete clicked"));
    }
});

// Filter the riddles by category and update the display and pagination
async function filterRiddlesByCategory(category) {
    const allRiddles = await getRiddlesArray();
    const filteredRiddles = category === 'all' ? allRiddles : allRiddles.filter(riddle => riddle.category === category);
    const riddlesChunks = chunkArray(filteredRiddles, riddlesPerPage);

    await displayRiddles(riddlesChunks[0]);
    createPagination(riddlesChunks);
}

document.getElementById("category-filter").addEventListener("change", async event => {
    const selectedCategory = event.target.value;
    await filterRiddlesByCategory(selectedCategory);
});


