import { check } from "./cookieCheck.js";

window.addEventListener('load', function(){
    let cookieValue = getCookie('id');
    if (cookieValue){
	check().then(ans => {
	    if (ans) {
		window.location.href = '/';
		return;
	    } else {
		deleteCookie();
	    } 
	});
    }
    document.getElementById('button').addEventListener('click', login);
});

function getCookie(name){
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return '';
}

function deleteCookie() {
    document.cookie = "id=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}

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
	    console.log(res.status);
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
		window.location.href = '/';
	    }
	});
};
