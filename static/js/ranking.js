// Fetch all users
const getAllUser = async () => {
    const response = await fetch(`/users/allUsers`);
    return await response.json();
};

// List
const displayRanking = async () => {
    const users = await getAllUser();
    const rankingTableBody = document.getElementById("rankingTableBody");

    users.sort((a, b) => b.score - a.score);

    users.forEach((user) => {
        const tr = document.createElement("tr");

        const tdFirstname = document.createElement("td");
        tdFirstname.style.paddingRight = "100px";
        tdFirstname.innerText = user.firstName;
        tr.appendChild(tdFirstname);

        const tdScore = document.createElement("td");
        tdScore.innerText = user.score;
        tr.appendChild(tdScore);

        rankingTableBody.appendChild(tr);
    });
};

// Call displayRanking to show the ranking when the page is loaded
displayRanking();
