burger = document.querySelector('.burger-menu')
navbar = document.querySelector('nav')
navlist = document.querySelector('nav ul')

burger.addEventListener('click', () => {
    navlist.classList.toggle('v-resp');
    navbar.classList.toggle('h-resp');
})

