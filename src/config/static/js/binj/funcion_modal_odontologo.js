var modal4 = document.getElementById("myModal_tabla_odontologo_1");

// Obtener el botón que abre el modal
var btn4 = document.getElementById("myBtn_4");

// Cuando el usuario haga clic en el botón, abrir el modal
btn4.onclick = function () {
    modal4.style.display = "block";
}


// Cuando el usuario haga clic fuera del modal, cerrarlo
window.onclick = function (event) {
  if (event.target == modal4) {
    modal4.style.display = "none";
  }
}
