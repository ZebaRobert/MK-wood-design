document.addEventListener("DOMContentLoaded", function(){
    const showLogin = document.getElementById('show-login');
    const loginForm = document.getElementById('login-form');

    // Set the initial visibility of the forms
    loginForm.style.display = 'block';
    registerForm.style.display = 'none';


    if (showLogin){
        showLogin.addEventListener('click', function(event){
            event.preventDefault();
            registerForm.style.display = 'none';
            loginForm.style.display = 'block';
        })
    }
})