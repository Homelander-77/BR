export async function loadLoginForm() {
    const response = await fetch('./login.html');
    const html = await response.text();

    const loginDiv = document.getElementById('login');
    loginDiv.innerHTML = html;
    loginDiv.style.display = 'block';
    
    
    const { loginUser } = await import('./login.js');
    await loginUser();
}
