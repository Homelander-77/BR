import { check } from "./cookieCheck.js";

window.addEventListener('DOMContentLoaded', async function() {
    const ans = await check();
    if (!ans) {
	const { loadLoginForm } = await import('./loginLoader.js');
	await loadLoginForm();
    } else {
	await loadCSS("./index.css");
	document.getElementById('login').classList.add('hidden');
	document.getElementById('main').classList.remove('hidden');
	setTimeout(renderFilms, 50);
    }

});

async function loadCSS(href) {
  document.querySelectorAll('link[href*="login.css"]').forEach(link => link.remove());

  return new Promise((resolve, reject) => {
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = href + '?v=' + Date.now(); // для обхода кеша
    link.onload = () => {
      console.log("✅ CSS loaded:", href);
      resolve(link);
    };
    link.onerror = (e) => {
      console.error("❌ CSS load failed:", href, e);
      reject(e);
    };
    document.head.appendChild(link);
  });
}

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

