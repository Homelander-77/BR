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
    const container = document.getElementById('films-container');
    container.innerHTML = '';
    films.forEach(film => {
        const card = document.createElement('div');
        card.className = 'film-card';
        card.innerHTML = `
            <img class="film-poster" src="${film.poster}" alt="${film.title}">
            <div class="film-info">
                <div class="film-title">${film.title}</div>
                <div class="film-desc">${film.desc}</div>
                <div class="film-meta">
                    <span>${film.year}</span>
                    <span>⭐ ${film.rating}</span>
                </div>
            </div>
        `;
        container.appendChild(card);
    });
}

document.addEventListener('DOMContentLoaded', renderFilms);
