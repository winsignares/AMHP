// Obtener el botón "Nueva cita"
const botonNuevaCita = document.querySelector("#boton-nueva-cita");

// Obtener el modal
const modal = document.querySelector(".modal1");

// Obtener el botón de cierre del modal
const botonCerrar = document.querySelector(".close");

// Cuando se hace clic en el botón "Nueva cita", mostrar el modal
botonNuevaCita.addEventListener("click", () => {
  modal.style.display = "block";
});

// Cuando se hace clic en el botón de cierre del modal, ocultar el modal
botonCerrar.addEventListener("click", () => {
  modal.style.display = "none";
});

// Cuando el usuario hace clic fuera del modal, cerrar el modal
window.addEventListener("click", (evento) => {
  if (evento.target == modal) {
    modal.style.display = "none";
  }
});
