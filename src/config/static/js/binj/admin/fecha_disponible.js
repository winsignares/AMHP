//esta es la fecha o citas que introducira el amdin y se encntraran disponibles
//se usa la tabla frecha dispononible
function fecha_disponible_save() {
    const fecha_disponible = document.getElementById("fecha_disponible_");
   
    if (
      fecha_disponible.value === "" 
  
  
    ) {
      // Mostrar la alerta de error
      Swal.fire({
        position: 'top-center',
        icon: 'error',
        title: 'Por favor, complete todos los campos.',
        showConfirmButton: false,
        timer: 2000,
      });
      return; // Salir de la función si no hay datos en todos los campos
    }
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
          if(res.data==="La fecha ya existe"){

          
          Swal.fire({
            position: 'top-center',
            icon: 'warning',
            title: 'El fecha ya existe',
            showConfirmButton: false,
            timer: 2000,
          });
        }else if(res.data==="Se ha guardado la fecha disponible exitosamente"){
         Swal.fire({
            position: 'top-center',
            icon: 'success',
            title: '¡Se a guardado la Fecha disponible!',
            showConfirmButton: false,
            timer: 2000,
          })
          fecha_disponible.value = "";

        }

          
        });
        
    } 
    
    catch (error) {
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

        // boton guardar
        opcions.value = datos[index].id_fechadisp;
        opcions.text = datos[index].fecha_disp;

        // boton actualizar
        opcions2.value = datos[index].id_fechadisp;
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