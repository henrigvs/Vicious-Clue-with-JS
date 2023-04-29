document.getElementById('sweetalert').addEventListener('click', function (){
    var clue = this.getAttribute('clue')
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
})