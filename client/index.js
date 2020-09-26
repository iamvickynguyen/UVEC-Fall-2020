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

