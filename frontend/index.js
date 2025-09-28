import { check } from "./cookieCheck.js";

window.addEventListener('load', async function() {
    const ans = await check();
    if (!ans) {
	const { loadLoginForm } = await import('./loginLoader.js');
	await loadLoginForm();
    } else {
	document.getElementById('login').style.display = 'none';
	const hello = document.getElementById('hello');
	hello.style.display = 'block';
    }
});

