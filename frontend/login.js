window.addEventListener('load', function(){
    document.getElementById('button').addEventListener('click', login);
});
function login() {
    fetch('/api/login', {
	method: 'POST',
	headers: {
        'Content-Type': 'application/json'
	},
	body: JSON.stringify({login: document.getElementById('login').value, 
			     password: document.getElementById('password').value})
    })
	.then(res => {
	    console.log(res.status)
	    if(res.status === 404){
		return '404';
	    } 
	    return res.json();
	})
	.then((json) => {
	    console.log(json.success);
	    if (!json.success){
		document.getElementById('error').style.display = 'block';
	    } else {
		document.getElementById('form').style.display = 'none';
		document.getElementById('cont').style.display = 'block';
	    }
	})
};
