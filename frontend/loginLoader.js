export async function loadLoginForm() {
    const container = document.getElementById('login');
    container.innerHTML = `
    <div id="login-page">
      <div class="login-box" id="loginForm">
        <h1>Login</h1>
        <div class="error" id="error">Wrong login or password!</div>
        <form>
          <input type="text" id="userLogin" placeholder="Username" required>
          <input type="password" id="password" placeholder="Password" required>
          <button type="button" id="button">Login</button>
        </form>
      </div>
    </div>
  `;    
    const { loginUser } = await import('./login.js');
    await loginUser();
}
