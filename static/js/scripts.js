const itemsContainer = document.querySelector('.overlay')

function windowOnClick (event) {
    if (event.target === itemsContainer){
        closeNav();
    }
}

function openNav() {
    document.getElementById("myNav").style.height = "100%";
}
  
function closeNav() {
    document.getElementById("myNav").style.height = "0%";
}


window.addEventListener('click', windowOnClick);