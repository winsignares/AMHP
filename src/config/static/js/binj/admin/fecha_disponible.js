//esta es la fecha o citas que introducira el amdin y se encntraran disponibles
//se usa la tabla frecha dispononible
function fecha_disponible_save() {
    const fecha_disponible = document.getElementById("fecha_disponible_");
   
  
    try {
      axios
        .post(
          "ingresar_fechas_disponibles",
          {
            fechas_dispon: fecha_disponible.value,
          },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((res) => {
          console.log(res.data);
          Swal.fire({
            position: 'top-center',
            icon: 'success',
            title: '¡Se a guardado la Fecha disponible!',
            showConfirmButton: false,
            timer: 2000,
          })
        });
    } catch (error) {
      console.error(error);
    }
  }
  
  
//se coloca el codigo que muestre las fechas disponibles en un select
function mostrarfechadispo() {
  const selectfecha = document.getElementById("fecha");
  const selectfecha2 = document.getElementById("fecha_actualizar");
  axios
    .get("obtener_fechas_dispo", {
      responseType: "json",
    })

    .then(function (response) {
      let datos = response.data;
      var length = Object.keys(datos).length + 0;

      i = 0;
      for (let index = 0; index < length; index++) {
        const opcions = document.createElement("option");
        const opcions2 = document.createElement("option");

        opcions.text = datos[index].fecha_disp;
        opcions2.text = datos[index].fecha_disp;

        selectfecha.appendChild(opcions);
        selectfecha2.appendChild(opcions2);
      }
    })
    .catch(function (error) {
      // Maneja los errores aquí
      console.log(error);
    });
}
window.addEventListener("load", function () {
  mostrarfechadispo();
});