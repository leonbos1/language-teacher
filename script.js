window.onload = function () {
    setNewWord();
};

allWords = [
    { "dutch": "appel", "italian": "mela", "english": "apple" },
    { "dutch": "banaan", "italian": "banana", "english": "banana" },
    { "dutch": "citroen", "italian": "limone", "english": "lemon" },
    { "dutch": "druif", "italian": "uva", "english": "grape" }
]

function submit() {
    input = document.getElementById('input').value;

    if (input == "") {
        alert("Please enter a valid input");
        return;
    }

    var word = document.getElementById('word').innerHTML;
    var feedback = document.getElementById('feedback');

    var index = allWords.findIndex(x => x.dutch === word);

    if (allWords[index].italian === input) {
        feedback.innerHTML = "Correct!";
        feedback.style.color = "green";
        setNewWord();
    } else {
        feedback.innerHTML = "Incorrect!";
        feedback.style.color = "red";
    }
}

function setNewWord() {
    var word = document.getElementById('word');

    var index = Math.floor(Math.random() * allWords.length);

    word.innerHTML = allWords[index].dutch;
}
