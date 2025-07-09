passwordInput.addEventListener('input', checkPassword)
document.getElementById('registrationForm').addEventListener('submit', function(e) {
    
});

const lengthIcon = document.getElementById('lengthIcon');
const caseIcon = document.getElementById('caseIcon');
const commonIcon = document.getElementById('commonIcon');
const simIcon = document.getElementById('simIcon');

const firstNameInput = document.getElementById('firstName');
const lastNameInput = document.getElementById('lastName');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');

function edit_conditions(json) {
    if json.length{
	lengthIcon.textContent = '✓';
        lengthIcon.className = 'valid';
    } else {
        lengthIcon.textContent = '✗';
        lengthIcon.className = 'invalid';
    }
    if json.symbols{
	caseIcon.textContent = '✓';
        caseIcon.className = 'valid';
    } else {
	caseIcon.textContent = '✗';
        caseIcon.className = 'invalid';
    }
    if json.common {
	commonIcon.textContent = '✓';
        commonIcon.className = 'valid';
    } else {
	commonIcon.textContent = '✗';
        commonIcon.className = 'invalid';
    }
    if json.sim {
	simIcon.textContent = '✓';
        simIcon.className = 'valid';
    } else {
	simIcon.textContent = '✗';
        simIcon.className = 'invalid';
    }
    
}

function checkPassword() {
    const password = this.value;

    fetch('/api/analysis', {
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
	res = res.json()
	edit_conditions(res)
    });
};
