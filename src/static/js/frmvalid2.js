

const newsname = document.querySelector('#id_newname');
const newsmail = document.querySelector('#id_mailaddress');
const newscompany = document.querySelector('#id_company');

const formsa = document.querySelector('#modalform')

const checkUsernamemail = () => {

    let valid = false;

    const min = 3,
        max = 25;

    const username = newsname.value.trim();

    if (!isRequireds(username)) {
        showError3(newsname, 'Please insert your name.');
    } else if (!isBetweenq(username.length, min, max)) {
        showError3(newsname, `Your name must be between ${min} and ${max} characters.`)
    } else {
        showSuccess3(newsname);
        valid = true;
    }
    return valid;
};


const checkEmailbews = () => {
    let valid = false;
    const email = newsmail.value.trim();
    if (!isRequireds(email)) {
        showError3(newsmail, 'Email cannot be blank.');
    } else if (!isEmailValids(email)) {
        showError3(newsmail, 'Email is not valid.')
    } else {
        showSuccess3(newsmail);
        valid = true;
    }
    return valid;
};


const checkCompanynews = () => {

    let valid = false;

    const min = 3,
        max = 50;

    const company = newscompany.value.trim();

    if (!isRequireds(company)) {
        showError3(newscompany, 'Company Name cannot be blank.');
    } else if (!isBetweenq(company.length, min, max)) {
        showError3(newscompany, `Company Name must be between ${min} and ${max} characters.`)
    } else {
        showSuccess3(newscompany);
        valid = true;
    }
    return valid;
};



const isEmailValids = (email) => {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
};

const isRequireds = value => value === '' ? false : true;
const isBetweenq = (length, min, max) => length < min || length > max ? false : true;

const showError3 = (input, message) => {
    // get the form-field element
    const formField3 = input.parentElement;
    // add the error class
    formField3.classList.remove('success');
    formField3.classList.add('error');

    // show the error message
    const error = formField3.querySelector('small');
    error.textContent = message;
};

const showSuccess3 = (input) => {
    // get the form-field element
    const formField3 = input.parentElement;

    // remove the error class
    formField3.classList.remove('error');
    formField3.classList.add('success');

    // hide the error message
    const error = formField3.querySelector('small');
    error.textContent = '';
}


formsa.addEventListener('submit', function (e){
    e.preventDefault();

    let isUsernameValid = checkUsernamemail(),
        isEmailValids = checkEmailbews(),
        isCompanyvalid = checkCompanynews();
    

    let isFormValid = isUsernameValid &&
        isEmailValids &&
        isCompanyvalid

    if (isFormValid) {
        document.getElementById("modalform").submit();
        console.log("done");
    }
});

const debounce3w = (fn, delay = 500) => {
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

formsa.addEventListener('input', debounce3w(function (e) {
    switch (e.target.id) {
        case 'username':
            checkUsernamemail();
            break;
        case 'email':
            checkEmailbews();
            break;
        case 'company':
            checkCompanynews();
            break;
      
    
    }
}));

// store the instance variable so we can access it in the console e.g. window.iti.getNumber()
window.iti = iti;