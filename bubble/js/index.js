const bodyele = document.querySelector(".bodyele");
const bubble = document.getElementById("bubble");

function change(e){
  
  let x = Math.round(e.touches[0].pageX);
  let y = Math.round(e.touches[0].pageY);
  let endX = bodyele.offsetWidth;
  let endY = bodyele.offsetHeight;
  
  if ((x>=50 && y>=50)&&(x<=310 &&y <=788)){
    bubble.style.left = x + "px";
    bubble.style.top = y + "px";
    console.log(screen.colorDepth);
  }
  
}

function touched(h){
  let x = Math.round(h.touches[0].pageX);
  let y = Math.round(h.touches[0].pageY);
  
  bubble.style.left = x + "px";
  bubble.style.top = y + "px";
  console.log(h);
}

function touchcomp(j){
  console.log(j);
}

window.onload=function(){
  bodyele.addEventListener("touchmove",change);
  bodyele.addEventListener("touchstart",touched);
  bodyele.addEventListener("touchend",touchcomp);
  
}