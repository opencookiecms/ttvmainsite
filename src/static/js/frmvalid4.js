const reqname = document.querySelector('#id_contactname');
const reqemail = document.querySelector('#id_contactemail');
const reqcompany = document.querySelector('#id_companyname');

const reqform = document.querySelector('#reqapp')

const checkUsernameReq = () => {
    let valid = false;

    const min = 3,
        max = 25;
    const username = reqname.value.trim();

    if (!isRequiredReq(username)) {
        showErrorReq(reqname, 'Please enter your name.');
    } else if (!isBetweenReq(username.length, min, max)) {
        showErrorReq(reqname, `Your name must be between ${min} and ${max} characters.`)
    } else {
        showSuccessReq(reqname);
        valid = true;
    }
    return valid;
};

const checkEmailReq = () => {
    let valid = false;
    const email = reqemail.value.trim();
    if (!isRequiredReq(email)) {
        showErrorReq(reqemail, 'Email cannot be blank.');
    } else if (!isEmailValid(email)) {
        showErrorReq(reqemail, 'Email is not valid.')
    } else {
        showSuccessReq(reqemail);
        valid = true;
    }
    return valid;
};

const checkCompanyReq = () => {
    let valid = false;
    const company = reqcompany.value.trim();
    console.log ('Company Input:', company);
    if (!isRequiredReq(company)) {
        showErrorReq(reqcompany, 'Company cannot be blank.');
    } else if (!isCompanyValid(company)) {
        console.log('Validation Failed');
        showErrorReq(reqcompany, 'Company is not valid.')
    } else {
        showSuccessReq(reqcompany);
        valid = true;
    }
    return valid;
};

const isRequiredReq = value => value === '' ? false : true;
const isBetweenReq = (length, min, max) => length < min || length > max ? false : true;

const showErrorReq = (input, message) => {
    // get the form-field element
    const formFieldReq = input.parentElement;
    // add the error class
    formFieldReq.classList.remove('success');
    formFieldReq.classList.add('error');

    // show the error message
    const error = formFieldReq.querySelector('small');
    error.textContent = message;
};

const showSuccessReq = (input) => {
    // get the form-field element
    const formFieldReq = input.parentElement;

    // remove the error class
    formFieldReq.classList.remove('error');
    formFieldReq.classList.add('success');

    // hide the error message
    const error = formFieldReq.querySelector('small');
    error.textContent = '';
}

reqform.addEventListener('submit', function (e){
    e.preventDefault();

    let isUsernameValid = checkUsernameReq(),
        isEmailValid = checkEmailReq(),
        isCompanyValid = checkCompanyReq();

    let isFormValid = isUsernameValid &&
        isEmailValid &&
        isCompanyValid

    if (isFormValid) {
        document.getElementById("reqapp").submit();
        console.log("done");
    }
});

const debounceReq = (fn, delay = 500) => {
    let timeoutId;
    return (...args) => {
        // cancel the previous timer
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        // setup a new timer
        timeoutId = setTimeout(() => {
            fn.apply(null, args)
        }, delay);
    };
};

reqform.addEventListener('input', debounceReq(function (e) {
    switch (e.target.id) {
        case 'username':
            checkUsernameReq();
            break;
        case 'email':
            checkEmailReq();
            break;
    }
}));

var input = document.querySelector("#id_contacttel");
var iti = window.intlTelInput(input, {
  // separateDialCode:true,
  initialCountry: 'my',
  utilsScript: "https://cdn.jsdelivr.net/npm/intl-tel-input@17.0.3/build/js/utils.js",
});

// store the instance variable so we can access it in the console e.g. window.iti.getNumber()
window.iti = iti;
