
function fecha_disponible_save() {

    const fechas_dispon = document.getElementById("fecha_disponible_id");
  alert("fecha disponible")
    try {
      axios.post(
          "ingresar_fechas_disponibles",
          {
      
            fechas_dispon: fechas_dispon.value,
         
          },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((res) => {
          console.log(res.data);
         
        });
    } catch (error) {
      console.error(error);
    }
  }