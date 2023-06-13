function save_citas_user() {
  const cedula_buscar = document.getElementById("cedula_buscar");
  const odontlogos = document.getElementById("nombre_odonto");
  const fechadipo_user = document.getElementById("fechadipo_user");
  const consultas = document.getElementById("consultas");
  const tarjetas = document.getElementById("tarjetas");
  const cardNumber = document.getElementById("cardNumber");
  const estado_cita = document.getElementById("estado_cita");
  const problemas = document.getElementById("problemas");

  if (
    cedula_buscar.value === "" ||
    odontlogos.value === "" ||
    fechadipo_user.value === "" ||
    consultas.value === "" ||
    tarjetas.value === "" ||
    cardNumber.value === "" ||
    estado_cita.value === "" ||
    problemas.value === ""
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
        "guardarcitas_user",
        {
          cedula_buscar: cedula_buscar.value,
          odontlogos: odontlogos.value,
          fecha: fechadipo_user.value,
          consulta: consultas.value,
          tarje_tade_credito: tarjetas.value,
          Num_tarjeta: cardNumber.value,
          estado_cita: estado_cita.value,
          problema: problemas.value,
        },
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      )
      .then((res) => {
        console.log(res.data);
        if (res.data.message === 'sisi') {
          // Mostrar la alerta de éxito con el código
          Swal.fire({
            position: 'top-center',
            icon: 'success',
            title: '¡Cita agendada con éxito!',
            html: `Código de cita: <strong>${res.data.codigo}</strong><br><br>Descripción: este codigo es para consultar su cita por si olvida algun dato.`,
            showConfirmButton: false,
            timer: 60000, // 1 minuto
          });
          // Restablecer los valores de los campos
          cedula_buscar.value = "";
          odontlogos.value = "";
          fechadipo_user.value = "";
          consultas.value = "";
          tarjetas.value = "";
          cardNumber.value = "";
          estado_cita.value = "";
          problemas.value = "";
        }  else if (res.data === 'Paciente already exists in the database') {
          // Mostrar la alerta de éxito
          Swal.fire({
            position: 'top-center',
            icon: 'warning',
            title: 'El paciente no existente',
            showConfirmButton: false,
            timer: 2000,
          });
        }
      });

  }
  // Mostrar la alerta de éxito


  catch (error) {
    console.error(error);



  }

}

//function que mustra odontologo en un select usando la ruta save_cita_user
function mostrarnombre_odontologo() {
  const select_name_odontologo = document.getElementById("nombre_odonto");
  axios
    .get("select_odontologo_mostrars", {
      responseType: "json",
    })

    .then(function (response) {
      let datos = response.data;
      var length = Object.keys(datos).length + 0;

      i = 0;
      for (let index = 0; index < length; index++) {
        const opcions = document.createElement("option");

        opcions.value = datos[index].id_odontologo;
        opcions.text = datos[index].name_odontologo;
        select_name_odontologo.appendChild(opcions);
      }
    })
    .catch(function (error) {
      // Maneja los errores aquí
      console.log(error);
    });
}
window.addEventListener("load", function () {
  mostrarnombre_odontologo();
});



//esta funcion hace que se muestre las fechas disponibles en el select usando la ruta save_cita_user
function mostrarfechadispo_user() {
  const selectfecha_dispo_user = document.getElementById("fechadipo_user");
  axios
    .get("obtener_fechas_dispo_como_user", {
      responseType: "json",
    })

    .then(function (response) {
      let datos = response.data;
      var length = Object.keys(datos).length + 0;
      i = 0;
      for (let index = 0; index < length; index++) {
        const opcions_fecha = document.createElement("option");

        opcions_fecha.value = datos[index].id_fechadisp;
        opcions_fecha.text = datos[index].fecha_disp_user;
        
        selectfecha_dispo_user.appendChild(opcions_fecha);
      }
    })
    .catch(function (error) {
      // Maneja los errores aquí
      console.log(error);
    });
}
window.addEventListener("load", function () {
  mostrarfechadispo_user();
});

// function habilitar() {
//     nom = document.getElementById("nombre").value;
//     edadd = document.getElementById("edad").value;
//     gene = document.getElementById("generos").value;
//     fecha = document.getElementById("consultaDates").value;
//     consul = document.getElementById("consultas").value;
//     tarje = document.getElementById("tarjetas").value;
//     num = document.getElementById("cardNumber").value;
//     val = 0;
//     if (nom == "") {
//         val++;
//     }
//     if (edadd == "") {
//         val++;
//     }if (gene == "") {
//         val++;
//     }if (fecha == "") {
//         val++;
//     }if (consul== "") {
//         val++;
//     }if (tarje == "") {
//         val++;
//     }if (num == "") {
//             val++;
//     } if (val == 0) {
//         document.getElementById("btn").disabled = false;
//     } else {
//         document.getElementById("btn").disabled = true;
//     }
// }
// document.getElementById("nombre").addEventListener("keyup", habilitar);
// document.getElementById("edad").addEventListener("keyup", habilitar);
// document.getElementById("generos").addEventListener("keyup", habilitar);
// document.getElementById("consultaDates").addEventListener("keyup", habilitar);
// document.getElementById("consultas").addEventListener("keyup", habilitar);
// document.getElementById("tarjetas").addEventListener("keyup", habilitar);
// document.getElementById("cardNumber").addEventListener("keyup", habilitar);
// document.getElementById("btn").addEventListener("click", () => {
//     console.log("se llenaron los input");
// });
