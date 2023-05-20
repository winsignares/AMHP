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
  