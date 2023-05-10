var modal3 = document.getElementById("myModal_tabla_paciente_1");

// Obtener el botón que abre el modal
var btn3 = document.getElementById("myBtn_3");

// Cuando el usuario haga clic en el botón, abrir el modal
btn3.onclick = function () {
    modal3.style.display = "block";
}


// Cuando el usuario haga clic fuera del modal, cerrarlo
window.onclick = function (event) {
  if (event.target == modal3) {
    modal3.style.display = "none";
  }
}
