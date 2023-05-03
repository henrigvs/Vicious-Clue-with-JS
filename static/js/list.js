document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.getElementsByClassName('btn-list');
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', function() {
            const clue = this.getAttribute('clue');
            Swal.fire({
                customClass: {
                    popup: 'popup'
                },
                title: 'clue',
                text: clue,
                confirmButtonClass: 'swal2-confirm button-cool',
                confirmButtonText: 'Cool',
                buttonsStyling: false,
            });
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.getElementsByClassName('btn-solution');
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', function() {
            const solution = this.getAttribute('solution');
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
        });
    }
});

document.querySelectorAll(".btn-difficulty").forEach(btn => {
    btn.addEventListener("click", event => {
        const action = event.target.dataset.action;
        const riddleId = event.target.value;

        fetch(`/edit/updateDifficulty/${riddleId}`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({action: action})
        }).then(response => {
            if (response.ok) {
                response.json().then(data => {
                    const difficultyValue = document.getElementById(`difficulty-${riddleId}`);
                    difficultyValue.innerText = data.newDifficulty;
                })
            } else {
                console.error("Failed to update difficulty");
            }
        });
    });
});

document.querySelectorAll(".btn-delete").forEach(btn => {
    btn.addEventListener("click", event => {
        const riddleId = event.target.value;
        let remainingRiddle = parseInt(event.target.dataset.remainingRiddle);

        console.log("Dataset remaining-riddle:", event.target.dataset.remainingRiddle); // Update this line
        console.log("Remaining riddles before deletion (parsed):", remainingRiddle);

        fetch(`/edit/deleteRiddle/${riddleId}`, {
            method: "POST"
        }).then(response => {
            if (response.ok) {
                event.target.closest("tr").remove();
                remainingRiddle--;
                if (remainingRiddle < 1) {
                    window.location.href = emptyListURL;
                }
                else if(remainingRiddle % 5 === 0){
                    let page = remainingRiddle/5;
                    window.location.href = `/list/${page}`;
                }
            } else {
                console.error("Failed to delete riddle");
            }
        });
    });
});


