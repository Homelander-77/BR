import { check } from "./checkAuth.js";
import { apiFetch } from "./api.js";

window.addEventListener('load', async function(){
    check().then(ans => {
	if (ans) {
	    window.location.href = '/';
	    return;
	} else {
	    deleteCookie();
	} 
    });
    await loginUser();
});

function deleteCookie() {
    document.cookie = "id=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}

export async function loginUser() {
    document.getElementById('button').addEventListener('click', async (e) => {
	const res = await apiFetch('/login', {
	    method: 'POST',
	    body: { login: document.getElementById('userLogin').value,
		    password: document.getElementById('password').value }
	});

	if(res.status === 404){
	    document.getElementById('error').style.display = 'block';
	    return;
	} 
	const json = await res.json();
	if (!json.success){
	    document.getElementById('error').style.display = 'block';
	} else {
	    window.location.href = '/';
	}	
    });
};
