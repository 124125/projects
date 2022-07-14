const btn = document.querySelector('.btn');
const menu = document.querySelector('.menubar');
const goback = document.getElementById('goback');

function go(e){
  menu.style = "left:0;opacity:1;";
}


function gobac(m){
  menu.style = "left:-100vw;opacity:0;";
}

goback.addEventListener("click",gobac);
btn.addEventListener("click",go);
