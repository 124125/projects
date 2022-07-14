var sliderw = document.querySelector(".slider");
var afteri = document.querySelector(".after-image-wrapper");
var contain = document.querySelector(".container");

function slideImg(e){
  
  /*     left margin of container from left edge      */
  let left = contain.offsetLeft;
  
  /*     width of container    */
  let right = contain.offsetWidth;
  
  /*     position of finger in container from left side of container    */
  let positionX = parseInt(e.touches[0].pageX) - left;
  
  /*     checking if finger in container and changing slider and image */
  if (positionX>0 && positionX<right){
    /*    seting value to after image width    */
    afteri.style.width = positionX+"px";
    
    /*    setting value to slider */
    sliderw.style.left = positionX+ "px";
    
    if (positionX < 10){
      afteri.style.width = 0;
      sliderw.style.left = 0;
    }
    
    if(positionX > right - 10){
      afteri.style.width = right;
      sliderw.style.left = right;
      window.close();
    }
  }
  
}

/*    triger  touchmove function when we touch screen    */
window.onload=function(){
  contain.addEventListener("touchmove",slideImg);
}
