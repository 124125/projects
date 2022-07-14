const card = document.querySelector('.card');
const content = document.querySelector('.content');
console.log(card);

card.addEventListener('click',function(){
  console.log("hello");
  content.style = "animation: fade 1s ";
});