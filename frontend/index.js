import { check } from "./cookieCheck.js";

window.addEventListener('load', async function() {
    const ans = await check();
    if (!ans) {
	const { loadLoginForm } = await import('./loginLoader.js');
	await loadLoginForm();
    } else {
	document.getElementById('login').style.display = 'none';
	const hello = document.getElementById('main');
	hello.style.display = 'block';
    }
});

const films = [
    {
        title: "Blade Runner 2049",
        desc: "A young blade runner's discovery of a long-buried secret leads him to track down former blade runner Rick Deckard.",
        poster: "https://m.media-amazon.com/images/I/81p+xe8cbnL._AC_SY679_.jpg",
        year: 2017,
        rating: 8.0
    }
 ];

function renderFilms() {
    fetch('/api/recommendations', {
	method: 'POST',
	headers: {
	    'Content-Type': 'application/json'
	}
    })
    .then(res => res.json())
    .then(films => {
	for(let i = 0; i < films.length; i++){
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
	}
    })
	.catch(err => console.error('Error loading films:', err));;
}

document.addEventListener('DOMContentLoaded', renderFilms);
