const jobname = document.querySelector('#id_contactname');
const jobemail = document.querySelector('#id_contactemail');
const resume = document.querySelector('#id_resume');

const formhr = document.querySelector('#jobapp')

const checkUsernamehr = () => {
    let valid = false;

    const min = 3,
        max = 25;
    const username = jobname.value.trim();

    if (!isRequired(username)) {
        showError(jobname, 'Please enter your name.');
    } else if (!isBetween(username.length, min, max)) {
        showError(jobname, `Your name must be between ${min} and ${max} characters.`)
    } else {
        showSuccess(jobname);
        valid = true;
    }
    return valid;
};


const checkEmailhr = () => {
    let valid = false;
    const email = jobemail.value.trim();
    if (!isRequired(email)) {
        showError(jobemail, 'Email cannot be blank.');
    } else if (!isEmailValid(email)) {
        showError(jobemail, 'Email is not valid.')
    } else {
        showSuccess(jobemail);
        valid = true;
    }
    return valid;
};

const checkResume = () => {
    let valid = false;
    resumechk = resume.files[0];
    if (!isRequired(resumechk)) {
        showError(resume, 'Please upload your resume.');
    } else if ((resumechk.type) != 'application/pdf') {
        showError(resume, 'Please upload your resume in PDF format.')
    } else {
        showSuccess(resume);
        valid = true;
    }
    return valid;
};

const isRequired = value => value === '' ? false : true;
const isBetween = (length, min, max) => length < min || length > max ? false : true;

const showError = (input, message) => {
    // get the form-field element
    const formFieldhr = input.parentElement;
    // add the error class
    formFieldhr.classList.remove('success');
    formFieldhr.classList.add('error');

    // show the error message
    const error = formFieldhr.querySelector('small');
    error.textContent = message;
};

const showSuccess = (input) => {
    // get the form-field element
    const formFieldhr = input.parentElement;

    // remove the error class
    formFieldhr.classList.remove('error');
    formFieldhr.classList.add('success');

    // hide the error message
    const error = formFieldhr.querySelector('small');
    error.textContent = '';
}

formhr.addEventListener('submit', function (e){
    e.preventDefault();

    let isUsernameValid = checkUsername(),
        isEmailValid = checkEmail(),
        isJobResumeValid = checkResume();

    let isFormValid = isUsernameValid &&
        isEmailValid &&
        isJobResumeValid

    if (isFormValid) {
        document.getElementById("jobapp").submit();
        console.log("done");
    }
});

const debouncehr = (fn, delay = 500) => {
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

formhr.addEventListener('input', debouncehr(function (e) {
    switch (e.target.id) {
        case 'username':
            checkUsernamehr();
            break;
        case 'email':
            checkEmailhr();
            break;
        case 'resume':
            checkResume();
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