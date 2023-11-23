const contactname = document.querySelector('#id_contactname');
const emailEl = document.querySelector('#id_contactemail');
const jobtype = document.querySelector('#id_jobtype');
const jobpos = document.querySelector('#id_job');
const resume = document.querySelector('#id_resume');

const formhr = document.querySelector('#jobapp')

const checkUsername = () => {
    let valid = false;

    const min = 3,
        max = 25;
    const username = contactname.value.trim();

    if (!isRequired(username)) {
        showError(contactname, 'Please enter your name.');
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

const checkJobType = () => {
    let valid = false;
    const jobtype = jobtype.value.trim();
    if (jobtype == 'disable') {
        showError(jobtype, 'Please choose an option.');
    } else {
        showSuccess(jobtype);
        valid = true;
    }
    return valid;
};

const checkJobPos = () => {
    let valid = false;
    const jobpos = jobpos.value.trim();
    if (jobpos == 'disable') {
        showError(jobpos, 'Please choose an option.');
    } else {
        showSuccess(jobpos);
        valid = true;
    }
    return valid;
};

const checkResume = () => {
    let valid = false;
    resume = resume.files[0];
    if (!isRequired(resume)) {
        showError(resume, 'Please upload your resume.');
    } else if ((resume.type) != 'application/pdf') {
        showError(resume, 'Please upload your resume in PDF format.')
    } else {
        showSuccess(resume);
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
        isJobTypeValid = checkJobType(),
        isJobPosValid = checkJobPos(),
        isJobResumeValid = checkResume();

    let isFormValid = isUsernameValid &&
        isEmailValid &&
        isJobTypeValid &&
        isJobPosValid &&
        isJobResumeValid

    if (isFormValid) {
        document.getElementById("jobapp").submit();
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

formhr.addEventListener('input', debounce(function (e) {
    switch (e.target.id) {
        case 'username':
            checkUsername();
            break;
        case 'email':
            checkEmail();
            break;
        case 'jobtype':
            checkJobType();
            break;
        case 'jobpos':
            checkJobPos();
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