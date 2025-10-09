import { check } from "./cookieCheck.js";

window.addEventListener('load', async function() {
    const ans = await check();
    if (!ans) {
	const { loadLoginForm } = await import('./loginLoader.js');
	await loadLoginForm();
    } else {
	document.getElementById('login').classList.add('hidden');
	document.getElementById('main').classList.remove('hidden');
	renderFilms();
    }
});

function renderFilms() {
    fetch('/api/rec', {
	method: 'POST',
	headers: {
	    'Content-Type': 'application/json'
	}
    })
    .then(res => res.json())
    .then(films => {
	const container = document.getElementById('films-container');
	container.innerHTML = '';
	films.forEach(film => {
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
    })
	.catch(err => console.error('Error loading films:', err));;
}

