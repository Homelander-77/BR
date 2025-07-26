import { check } from "cookieCheck";

window.addEventListener('load', function() {
    if (!check) {
   	window.location.href = '/login';
    }
});

