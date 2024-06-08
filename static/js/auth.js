document.addEventListener("DOMContentLoaded", function() {
    const showRegister = document.getElementById('show-register');
    const showLogin = document.getElementById('show-login');
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');

    // Set the initial visibility of the forms
    loginForm.style.display = 'block';
    registerForm.style.display = 'none';

    if (showRegister) {
        showRegister.addEventListener('click', function(event) {
            event.preventDefault();
            loginForm.style.display = 'none';
            registerForm.style.display = 'block';
        });
    }

    if (showLogin) {
        showLogin.addEventListener('click', function(event) {
            event.preventDefault();
            registerForm.style.display = 'none';
            loginForm.style.display = 'block';
        });
    }
});