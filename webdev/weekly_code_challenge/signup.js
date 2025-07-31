const signupButton = document.getElementById('signupButton');
const loginButton = document.getElementById('loginButton');
const signupForm =document.getElementById('signup');
const loginForm = document.getElementById('login');

signupButton.addEventListener('click',function{
  loginForm.style.display='none';
  signupForm.style.display='block';
})
loginButton.addEventListener('click',function{
  loginForm.style.display='block';
  signupForm.style.display='none'
})


