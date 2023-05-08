// Obtener el botón "Nueva cita"
const botonNuevaCita = document.querySelector("#boton-nueva-cita");
const botonNuevaCita2 = document.querySelector("#boton-nueva-cita-disponible");


// Obtener el modal
const modal = document.querySelector(".modal1");
const modal2 = document.querySelector(".modal2");


// Obtener el botón de cierre del modal
const botonCerrar = document.querySelector(".close");
const botonCerrar2 = document.querySelector(".close2");

// Cuando se hace clic en el botón "Nueva cita", mostrar el modal
botonNuevaCita.addEventListener("click", () => {
  modal.style.display = "block";
});
botonNuevaCita2.addEventListener("click", () => {
    modal2.style.display = "block";
  });
// Cuando se hace clic en el botón de cierre del modal, ocultar el modal
botonCerrar.addEventListener("click", () => {
  modal.style.display = "none";
});
botonCerrar2.addEventListener("click", () => {
    modal2.style.display = "none";
  });
// Cuando el usuario hace clic fuera del modal, cerrar el modal
window.addEventListener("click", (evento) => {
  if (evento.target == modal) {
    modal.style.display = "none";
  }
});
window.addEventListener("click", (evento) => {
    if (evento.target == modal2) {
      modal2.style.display = "none";
    }
  });
  

