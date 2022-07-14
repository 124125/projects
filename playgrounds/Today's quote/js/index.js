function copytext(){
  copyText = document.querySelector(".quotetext");
  hwriter = document.getElementById("quotew");
  var temp = document.createElement("textarea");
  document.body.appendChild(temp);
  temp.value = copyText.innerText+ " -" + hwriter.innerText;
  temp.select();
  document.execCommand("copy");
  document.body.removeChild(temp);
}