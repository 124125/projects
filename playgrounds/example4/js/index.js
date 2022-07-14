const header = document.querySelector(".header");

window.addEventListener("scroll",change);

function change(e){
  console.log(header);
  header.classList.toggle("sticky",window.scrollY > 0);
}