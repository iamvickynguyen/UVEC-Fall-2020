// DATA
async function postEmail() {
    const email = document.querySelector('#input-email');
    const emailInput = email.value;

    $.ajax({
        type: "POST",
        url: 'http://127.0.0.1:5000/postEmail',
        data: JSON.stringify({ 'email': emailInput }),
        contentType: 'application/json;charset=UTF-8',
        success: function (response) {
            let responseData = JSON.parse(response);
            console.log(responseData.data);
            doSomething(responseData.data);
        },
        error: function (err) {
            // console.log(err);
            alert('Error! Wrong username or token');
        }
    });

    email.value = "";
}

// output is a list of key value [{firstName,lastName,gender,genderPreference,email,profession,lat,long,city,favoriteAnimal,favoriteMusicGenre,age,smoking,astrologicalSign,highestEducationLevel}]
function doSomething(output) {
    // do something with the output here...
}


// RESULT PAGE
const userContainer = document.querySelector(".user-container");
const next = document.querySelector(".btn-right");
const prev = document.querySelector(".btn-left");
const item = document.querySelector(".item-list");
const resultContainer = document.querySelector(".result");
const scoreContainer = document.querySelector(".score");

let idx = 0;
let results = [];


console.log(next);
console.log(prev);
const userInfo = {
    "name": "John Doe",
    "age": "28",
    "favoriteMusic": "rock",
    "favoriteAnimal": "dog",
    "city": "Victoria"
}

next.addEventListener("click", nextResult);
prev.addEventListener("click", prevResult);

function generateUser(user, userContainer) {
    const name = document.createElement("h3");
    name.classList.add("simple-card-title");
    name.innerText = user["name"]
    userContainer.children[0].appendChild(name);

    const age = document.createElement("p");
    age.classList.add("simple-card-desc");
    age.innerText = `Age: ${user["age"]}`
    userContainer.children[0].appendChild(age);

    const music = document.createElement("p");
    music.classList.add("simple-card-desc");
    music.innerText = `Favorite Music: ${user["favoriteMusic"]}`
    userContainer.children[0].appendChild(music);

    const animal = document.createElement("p");
    animal.classList.add("simple-card-desc");
    animal.innerText = `Favorite Animal: ${user["favoriteAnimal"]}`
    userContainer.children[0].appendChild(animal);

    const city = document.createElement("p");
    city.classList.add("simple-card-desc");
    city.innerText = `City: ${user["city"]}`;
    userContainer.children[0].appendChild(city);

    const line = document.createElement("div");
    line.classList.add("simple-card-line");

    userContainer.children[0].appendChild(line);

}

function nextResult(e) {
    idx++;
    generateUser(results[idx], resultContainer);
}

function prevResult(e) {
    idx--;
    generateUser(results[idx], resultContainer);
}
console.log(userContainer.children[0]);

item.innerText = `${idx}/${results.length}`;

const score = document.createElement("h3");
score.classList.add("simple-card-title")
// score.innerText = `${results[idx][score]}`;
scoreContainer.appendChild(score);
generateUser(userInfo, userContainer);

