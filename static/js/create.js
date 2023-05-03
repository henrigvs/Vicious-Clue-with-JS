

$(document).ready(function() {
    let counter = 1;

    $("#addClueButton").click(function () {
        if (counter < 3) {
            const $newClue = $(".clue-wrapper").first().clone();
            $newClue.find("input").val('');
            const newClueNumber = counter + 1;
            $newClue.attr("clue-number", newClueNumber)
            $newClue.find("label").text(`Clue n° ${newClueNumber}`);
            $(".clue-container").append($newClue);
            counter++;
        }
    });
    $("#removeClueButton").click(function (){
        if(counter > 1){
            $(".clue-wrapper").last().remove();
            counter--;
        }
    })
});

function submitRiddle(){
    const clues = [];
    $('.clue-wrapper').each(
        function (){
            const RiddleElements = $(this).find('.new-value').val();
            clues.push({description: RiddleElements});
        }
    );

    $('#clues').val(JSON.stringify(clues));

    $('#createRiddleForm').submit();
}

document.getElementById("decreaseDifficulty").addEventListener("click", function () {
    let difficultyInput = document.getElementById("difficultyInput");
    let difficulty = parseInt(difficultyInput.value, 10);
    if (difficulty > 1) {
        difficulty -= 1;
        difficultyInput.value = difficulty;
    }
});

document.getElementById("increaseDifficulty").addEventListener("click", function () {
    let difficultyInput = document.getElementById("difficultyInput");
    let difficulty = parseInt(difficultyInput.value, 10);
    if (difficulty < 5) {
        difficulty += 1;
        difficultyInput.value = difficulty;
    }
});

