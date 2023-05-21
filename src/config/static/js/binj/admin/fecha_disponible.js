//esta es la fecha o citas que introducira el amdin y se encntraran disponibles
//se usa la tabla frecha dispononible
function fecha_disponible_save() {
    const fecha_disponible = document.getElementById("fecha_disponible_");
    alert("fecha dispo");
  
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
          alert("cita disponoible");
        });
    } catch (error) {
      console.error(error);
    }
  }
  
  
//se coloca el codigo que muestre las fechas disponibles en un select
function mostrarfechadispo() {
  const selectfecha = document.getElementById("fecha");
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

        opcions.text = datos[index].fecha_disp;
        selectfecha.appendChild(opcions);
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