export async function loadLoginForm() {
    const response = await fetch('./login.html');
    const html = response.text;

    document.getElementById('hello').innerHTML = html;
    
    const { login } = await import('./login.js');
    login();
}
