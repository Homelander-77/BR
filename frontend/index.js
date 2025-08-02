import { check } from "./cookieCheck.js";

window.addEventListener('load', function() {
    check().then(ans => {
	if (!ans) {
	    window.location.href = '/login';
	}
    });
});

