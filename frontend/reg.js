import { check } from "./cookieCheck.js";

window.addEventListener('load', function() {
    check().then(ans => {
	if (ans) {
	    window.location.href = '/';
	}
    });
});


document.getElementById('registrationForm').addEventListener('submit', function(e) {
    e.preventDefault();
    reg();
});

const passwordInput = document.getElementById('password');
passwordInput.addEventListener('input', checkPassword);

const lengthIcon = document.getElementById('lengthIcon');
const caseIcon = document.getElementById('caseIcon');
const simIcon = document.getElementById('simIcon');
const commonIcon = document.getElementById('commonIcon');

const commonPoint = document.getElementById('common');

function getData(){
    const passwordInput =  document.getElementById('password').value;
    const firstNameInput = document.getElementById('firstName').value;
    const lastNameInput = document.getElementById('lastName').value;
    const emailInput = document.getElementById('email').value;

    const password = (typeof passwordInput === 'string') ? passwordInput : '';
    const firstName = (typeof firstNameInput === 'string') ? firstNameInput : '';
    const lastName = (typeof lastNameInput === 'string') ? lastNameInput : '';
    const email = (typeof emailInput === 'string') ? emailInput : '';

    return [password, firstName, lastName, email];
}

function levenshtein(a, b) {
    const matrix = Array(a.length + 1).fill(null).map(() =>
	Array(b.length + 1).fill(null)
    );
  for (let i = 0; i <= a.length; i++) matrix[i][0] = i;
  for (let j = 0; j <= b.length; j++) matrix[0][j] = j;
  for (let i = 1; i <= a.length; i++) {
    for (let j = 1; j <= b.length; j++) {
      const cost = a[i - 1] === b[j - 1] ? 0 : 1;
      matrix[i][j] = Math.min(
        matrix[i - 1][j] + 1,
        matrix[i][j - 1] + 1,
        matrix[i - 1][j - 1] + cost
      );
    };
  };
    return matrix[a.length][b.length];
}

function similarity(password, firstName, lastName, email) {    
    let personalData = [firstName, lastName, email];
    let coefs = personalData.map((data) => {
	let pwd = (typeof password === 'string') ? password : ''; // additionaly check
	let datum = (typeof data === 'string') ? data : ''; // additionaly check
	const distance = levenshtein(pwd.toLowerCase(), datum.toLowerCase());
	const maxLen = Math.max(pwd.length, datum.length);
	return 1 - distance / maxLen;
    });
    return Math.max(...coefs);
}

function len(password) {
    return password.length >= 8 && password.length < 96;
}

function specialSymbolsDigestsLetters(password) { 
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[.@$!%*#?&\/])[A-Za-z\d@$!%*#?&.\/]{8,}$/;
    return regex.test(password);
} 

function coincidence(password, firstName, lastName, email){
    if (password.length > 0 && firstName.length > 0 && lastName.length > 0 && email.length > 0){
	const sim = similarity(password, firstName, lastName, email);
	if (sim < 0.35){
	    return true;
	} else {
	    return false;
	}
    } else {
	return false;
    }
}

function checkPassword(){
    const [password, firstName, lastName, email] = getData();
    
    if (len(password)) {
	lengthIcon.textContent = '✓';
        lengthIcon.className = 'valid';
    } else {
	lengthIcon.textContent = '✗';
        lengthIcon.className = 'invalid';
    }
    
    if (specialSymbolsDigestsLetters(password)) {
	caseIcon.textContent = '✓';
        caseIcon.className = 'valid';
    } else {
	caseIcon.textContent = '✗';
        caseIcon.className = 'invalid';
    }
    
    if (coincidence(password, firstName, lastName, email)){
	simIcon.textContent = '✓';
        simIcon.className = 'valid';
    } else {
	simIcon.textContent = '✗';
        simIcon.className = 'invalid';
    }
}

function edit_common() {
    commonIcon.style = 'none';    
}

function showNotification(message) {
  const notif = document.getElementById('notification');
  notif.textContent = message;
  notif.classList.add('show');

  setTimeout(() => {
    notif.classList.remove('show');
  }, 5000);
}


function reg() {    
    const [password, firstName, lastName, email] = getData();
    if (len(password) && specialSymbolsDigestsLetters(password) && coincidence(password, firstName, lastName, email)){
        fetch('/api/reg', {
	method: 'POST',
	headers: {
	    'Content-Type': 'application/json'
	},
	body: JSON.stringify({firstname: firstName,
			      lastname: lastName,
			      login: email, 
			      password: password})
    })
	    .then(res => {
		if (res.status === 400) {
		    edit_common();
		    alert("Bad Request: Please check your input and try again.");
		} else if (res.status === 200) {
		    window.location.href = '/';
		} else {
		    alert("Unexpected server response.");
                    throw new Error('Unexpected status: ' + res.status);
		}
	    })
	    .catch(error => {
		console.error('Fetch error:', error);
		alert("Network error or bad response");
	    });
    } else {
	
    }
}
