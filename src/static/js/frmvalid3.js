const jobname = document.querySelector('#id_contactname');
const jobemail = document.querySelector('#id_contactemail');
const resume = document.querySelector('#id_resume');
const appform = document.querySelector('#id_appform');

const formhr = document.querySelector('#jobapp')

const checkUsernamehr = () => {
    let valid = false;

    const min = 3,
        max = 25;
    const username = jobname.value.trim();

    if (!isRequiredhr(username)) {
        showErrorhr(jobname, 'Please enter your name.');
    } else if (!isBetweenhr(username.length, min, max)) {
        showErrorhr(jobname, `Your name must be between ${min} and ${max} characters.`)
    } else {
        showSuccesshr(jobname);
        valid = true;
    }
    return valid;
};


const checkEmailhr = () => {
    let valid = false;
    const email = jobemail.value.trim();
    if (!isRequiredhr(email)) {
        showErrorhr(jobemail, 'Email cannot be blank.');
    } else if (!isEmailValid(email)) {
        showErrorhr(jobemail, 'Email is not valid.')
    } else {
        showSuccesshr(jobemail);
        valid = true;
    }
    return valid;
};

const checkResume = () => {
    let valid = false;
    resumechk = resume.files[0];
    if (!resumechk) {
        showErrorhr(resume, 'Please upload your resume.');
    } else if (resumechk.type !== 'application/pdf') {
        showErrorhr(resume, 'Please upload your resume in PDF format.');
    } else {
        showSuccesshr(resume);
        valid = true;
    }
    return valid;
};

const checkAppForm = () => {
    let valid = false;
    appformchk = appform.files[0];
    if (!appformchk) {
        showErrorhr(appform, 'Please upload your application form.');
    } else if (appformchk.type !== 'application/pdf') {
        showErrorhr(appform, 'Please upload your application form in PDF format.');
    } else {
        showSuccesshr(appform);
        valid = true;
    }
    return valid;
};

const isRequiredhr = value => value === '' ? false : true;
const isBetweenhr = (length, min, max) => length < min || length > max ? false : true;

const showErrorhr = (input, message) => {
    // get the form-field element
    const formFieldhr = input.parentElement;
    // add the error class
    formFieldhr.classList.remove('success');
    formFieldhr.classList.add('error');

    // show the error message
    const error = formFieldhr.querySelector('small');
    error.textContent = message;
};

const showSuccesshr = (input) => {
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

    let isUsernameValid = checkUsernamehr(),
        isEmailValid = checkEmailhr(),
        isJobResumeValid = checkResume(),
        isAppFormValid = checkAppForm();

    let isFormValid = isUsernameValid &&
        isEmailValid &&
        isJobResumeValid && isAppFormValid

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
        case 'appform':
            checkAppForm();
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