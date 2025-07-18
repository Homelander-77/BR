passwordInput.addEventListener('input', checkPassword)
document.getElementById('registrationForm').addEventListener('submit', reg);

const lengthIcon = document.getElementById('lengthIcon');
const caseIcon = document.getElementById('caseIcon');
const simIcon = document.getElementById('simIcon');
const commonIcon = document.getElementById('commonIcon');

const commonPoint = document.getElementById('common');

const firstNameInput = document.getElementById('firstName');
const lastNameInput = document.getElementById('lastName');
const emailInput = document.getElementById('email');


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
    }
  }
  return matrix[a.length][b.length];
}

function similarity(password, firstName, lastName, email) {
    const personalData = [firstName, lastName, email]
    let coefs = []; 
    for (let i=0; i < 3, i++) {
	const distance = levenshtein(password.toLowerCase(), personalData[i].toLowerCase());
	const maxLen = Math.max(a.length, b.length);
	coefs.push(1 - distance / maxLen);    
  }
  
  return Math.max(coefs);
}

function edit_conditions(password){
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[.@$!%*#?&/])[A-Za-z\d@$!%*#?&./]{8,}$/
    const arr = []

    if (password.length >= 8) {
	lengthIcon.textContent = '✓';
        lengthIcon.className = 'valid';
    } else {
	lengthIcon.textContent = '✗';
        lengthIcon.className = 'invalid';
    }
    
    if (regex.text(password)) {
	caseIcon.textContent = '✓';
        caseIcon.className = 'valid';
    } else {
	caseIcon.textContent = '✗';
        caseIcon.className = 'invalid';
    }
    
    if (if similarity < 0.65) {
	simIcon.textContent = '✓';
        simIcon.className = 'valid';
    } else {
	simIcon.textContent = '✗';
        simIcon.className = 'invalid';
    }

}

function edit_common(json) {
    
    
}

function checkPassword() {
    const password = this.value;

    edit_conditions(password);


function reg() {
        fetch('/api/reg', {
	method: 'POST',
	headers: {
	    'Content-Type': 'application/json'
	},
	body: JSON.stringify({firstname: firstNameInput.value,
			      lastname: lastNameInput.value,
			      login: emailInput.value, 
			      password: passwordInput.value})
    })
    .then(res => {
	res = res.json();
	if res.status == {
	    // redirect
	} else {
	    // red error
	}

    })

}
