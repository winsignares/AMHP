// Obtener el modal
var modal = document.getElementById("myModal_tabla_admin_1");
var modal2 = document.getElementById("myModal_tabla_admin_2");

// Obtener el botón que abre el modal
var btn = document.getElementById("myBtn_1");
var btn2 = document.getElementById("myBtn_2");

// Cuando el usuario haga clic en el botón, abrir el modal
btn.onclick = function () {
  modal.style.display = "block";
}
btn2.onclick = function () {
  modal2.style.display = "block";
}
// Cuando el usuario haga clic fuera del modal, cerrarlo
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  } else if (event.target == modal2) {
    modal2.style.display = "none";
  }
}




