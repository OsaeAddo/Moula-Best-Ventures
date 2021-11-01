const menuBtn = document.querySelector('.fa-bars')
const navMenu = document.querySelector('.nav-menu')

function toggleNav() {
    navMenu.classList.toggle('show-nav-menu');
}

function windowOnClick (event) {
    if (event.target === navMenu){
        toggleNav();
    }
}
menuBtn.addEventListener('click', toggleNav);
window.addEventListener('click', windowOnClick);