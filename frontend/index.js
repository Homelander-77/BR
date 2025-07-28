import { check } from "./cookieCheck.js";

window.addEventListener('load', function() {
    if (!check()) {
   	window.location.href = '/login';
    }
});

