
//este es para abrir el modal de registro admin
var modal_regsitro = document.getElementById("myModal_regritoadmin");


// Obtener el botón que abre el modal
var btn_regsitro = document.getElementById("myBtn_modal_registro_adin");


// Cuando el usuario haga clic en el botón, abrir el modal
btn_regsitro.onclick = function () {
  modal_regsitro.style.display = "block";
}

// Cuando el usuario haga clic fuera del modal, cerrarlo
window.onclick = function (event) {
  if (event.target == modal_regsitro) {
    modal_regsitro.style.display = "none";
  }
}