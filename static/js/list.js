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

