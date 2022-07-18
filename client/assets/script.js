let recaptchaToken = ''
let credentialsResponse = {}

function isCaptchaChecked() { // checks if the recaptcha is still valid
    return grecaptcha && grecaptcha.getResponse().length !== 0;
}


function recaptchaCallback(data) { // sets the token when the recaptcha is completed
    recaptchaToken = data
}


function handleCredentialResponse(data) {
    function jwtDecode(t) {
        let token = {};
        token.raw = t;
        token.header = JSON.parse(window.atob(t.split('.')[0]));
        token.payload = JSON.parse(window.atob(t.split('.')[1]));
        return (token)
    }

    const { credential } = data
    
    const { header, payload } = jwtDecode(credential)

    credentialsResponse = {
        name: payload.name,
        email: payload.email,
        credential,
    }
    // function handleCredentialResponse(response) {
    //     // decodeJwtResponse() is a custom function defined by you
    //     // to decode the credential response.
    //     const responsePayload = decodeJwtResponse(response.credential);
   
    //     console.log("ID: " + responsePayload.sub);
    //     console.log('Full Name: ' + responsePayload.name);
    //     console.log('Given Name: ' + responsePayload.given_name);
    //     console.log('Family Name: ' + responsePayload.family_name);
    //     console.log("Image URL: " + responsePayload.picture);
    //     console.log("Email: " + responsePayload.email);
    //  }
}

function getFormData() {
    return {
        productName: document.getElementById("productName").value,
        days: document.getElementById("days").value,
        satisfaction: document.getElementById("satisfaction").value,
        verdict: document.getElementById("verdict").value
    }
}

function getMissingFields() {
    const missingFields = []

    if (document.getElementById("productName").value === '') {
        missingFields.push("Product Name")
    }
    if (document.getElementById("days").value === '') {
        missingFields.push("Days of use")
    }
    if (document.getElementById("satisfaction").value === '') {
        missingFields.push("Product Satisfactory")
    }
    if (document.getElementById("verdict").valu === '') {
        missingFields.push("Final Verdict")
    }

    return missingFields
}

function submitForm() {
    const missingFields = getMissingFields()

    if (missingFields.length > 0) {
        alert("The following fields are missing: " + missingFields.join(' , '))
        return
    }

    if (!isCaptchaChecked()) {
        alert("Please verify you are a human with the Captcha test")
        return
    }

    if (Object.keys(credentialsResponse).length === 0) {
        alert("Please identify yourself with google sign in")
        return
    }

    console.log(getFormData())
}