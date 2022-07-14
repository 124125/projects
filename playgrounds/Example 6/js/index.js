const header = document.querySelector('header');


function scrollnev(){
  header.classList.toggle('onscroll',window.scrollY > 0);
  console.log("sc");
}

window.addEventListener('scroll',scrollnev);