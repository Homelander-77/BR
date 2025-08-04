import { check } from "./cookieCheck.js";

window.addEventListener('load', function() {
    check().then(ans => {
	if (!ans) {
	    const { loadLoginForm } = await import('./loginLoader.js');
	    await loadLoginForm();
	} else {
	    const hello = document.getElementById('hello');
	    hello.style = 'block';
	}
    });
});

