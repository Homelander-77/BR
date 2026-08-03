import { check } from "./checkAuth.js";
import { apiFetch } from "./api.js";

window.addEventListener('DOMContentLoaded', async function() {
    const ans = await check();
    if (!ans) {
	await loadCSS('./login.css');
	const { loadLoginForm } = await import('./loginLoader.js');
	await loadLoginForm();
    } else {
	document.querySelectorAll('link[href*="login.css"]').forEach(link => link.remove());
	await loadCSS('./index.css');
	document.getElementById('login').innerHTML = '';
	document.getElementById('main').classList.remove('hidden');
	renderFilms();
    }

});

async function loadCSS(href) {
  return new Promise((resolve, reject) => {
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = href + '?v=' + Date.now();
    link.onload = () => {
      resolve(link);
    };
    link.onerror = (e) => {
      reject(e);
    };
    document.head.appendChild(link);
  });
}
async function renderFilms() {
    try {
	const res = await apiFetch('/rec', { method: 'POST' });
	const json = await res.json();
	
	
	const container = document.getElementById('films-container');
	container.innerHTML = '';
	json.forEach(film => {
	    const card = document.createElement('div');
	    card.className = 'film-card';
	    card.innerHTML = `
            <img class="film-poster" src="${film.f_path}" alt="${film.f_name}">
            <div class="film-info">
                <div class="film-title">${film.f_name}</div>
                <div class="film-desc">${film.f_view}</div>
                <div class="film-meta">
                    <span>${film.f_graduation}</span>
                    <span>⭐ ${film.f_r}</span>
                </div>
            </div>
        `;
	    container.appendChild(card);
	});
    } catch(err) {
	console.error('Error loading films:', err);
    }
}

