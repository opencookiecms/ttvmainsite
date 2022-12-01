

const contactname = document.querySelector('#id_contactname');
const emailEl = document.querySelector('#id_contactemail');
const companyName = document.querySelector('#id_companyname');
const subjectEmail = document.querySelector('#id_enquirysubject');
const messageEmail = document.querySelector('#id_enquirycontent');
const form = document.querySelector('#signup')




const checkUsername = () => {

    let valid = false;

    const min = 3,
        max = 25;

    const username = contactname.value.trim();

    if (!isRequired(username)) {
        showError(contactname, 'Please insert your name.');
    } else if (!isBetween(username.length, min, max)) {
        showError(contactname, `Your name must be between ${min} and ${max} characters.`)
    } else {
        showSuccess(contactname);
        valid = true;
    }
    return valid;
};


const checkEmail = () => {
    let valid = false;
    const email = emailEl.value.trim();
    if (!isRequired(email)) {
        showError(emailEl, 'Email cannot be blank.');
    } else if (!isEmailValid(email)) {
        showError(emailEl, 'Email is not valid.')
    } else {
        showSuccess(emailEl);
        valid = true;
    }
    return valid;
};


const checkCompany = () => {

    let valid = false;

    const min = 3,
        max = 50;

    const company = companyName.value.trim();

    if (!isRequired(company)) {
        showError(companyName, 'Company Name cannot be blank.');
    } else if (!isBetween(company.length, min, max)) {
        showError(companyName, `Company Name must be between ${min} and ${max} characters.`)
    } else {
        showSuccess(companyName);
        valid = true;
    }
    return valid;
};


const checkSubject = () => {

    let valid = false;

    const min = 3,
        max = 150;

    const subject = subjectEmail.value.trim();

    if (!isRequired(subject)) {
        showError(subjectEmail, 'Subject cannot be blank.');
    } else if (!isBetween(subject.length, min, max)) {
        showError(subjectEmail, `Subject must be between ${min} and ${max} characters.`)
    } else {
        showSuccess(subjectEmail);
        valid = true;
    }
    return valid;
};


const checkMessage = () => {

    let valid = false;

    const min = 3,
        max = 450;

    const message = messageEmail.value.trim();

    if (!isRequired(message)) {
        showError(messageEmail, 'Your enquiry cannot be blank.');
    } else if (!isBetween(message.length, min, max)) {
        showError(messageEmail, `Your enquiry must be between ${min} and ${max} characters.`)
    } else {
        showSuccess(messageEmail);
        valid = true;
    }
    return valid;
};




const isEmailValid = (email) => {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
};

const isRequired = value => value === '' ? false : true;
const isBetween = (length, min, max) => length < min || length > max ? false : true;

const showError = (input, message) => {
    // get the form-field element
    const formField = input.parentElement;
    // add the error class
    formField.classList.remove('success');
    formField.classList.add('error');

    // show the error message
    const error = formField.querySelector('small');
    error.textContent = message;
};

const showSuccess = (input) => {
    // get the form-field element
    const formField = input.parentElement;

    // remove the error class
    formField.classList.remove('error');
    formField.classList.add('success');

    // hide the error message
    const error = formField.querySelector('small');
    error.textContent = '';
}

form.addEventListener('submit', function (e){
    e.preventDefault();

    let isUsernameValid = checkUsername(),
        isEmailValid = checkEmail(),
        isCompanyvalid = checkCompany(),
        isSubjectvalid = checkSubject(),
        isMessagevalid = checkMessage();

    let isFormValid = isUsernameValid &&
        isEmailValid &&
        isCompanyvalid &&
        isSubjectvalid &&
        isMessagevalid

    if (isFormValid) {
        document.getElementById("signup").submit();
        console.log("done");
    }
});

const debounce = (fn, delay = 500) => {
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

form.addEventListener('input', debounce(function (e) {
    switch (e.target.id) {
        case 'username':
            checkUsername();
            break;
        case 'email':
            checkEmail();
            break;
        case 'subject':
            checkSubject();
            break;
        case 'message':
            checkMessage();
            break;
    
    }
}));



var input = document.querySelector("#id_contacttel");
var iti = window.intlTelInput(input, {
  // separateDialCode:true,
  utilsScript: "https://cdn.jsdelivr.net/npm/intl-tel-input@17.0.3/build/js/utils.js",
});

// store the instance variable so we can access it in the console e.g. window.iti.getNumber()
window.iti = iti;