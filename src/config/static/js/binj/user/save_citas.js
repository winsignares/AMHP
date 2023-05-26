function save_cit() {
  const nombres = document.getElementById("nombres");
  const edades = document.getElementById("edades");
  const generos = document.getElementById("nombre_odonto");
  const fecha = document.getElementById("fecha");
  const consultas = document.getElementById("consultas");
  const tarjetas = document.getElementById("tarjetas");
  const cardNumber = document.getElementById("cardNumber");
  const estado_cita = document.getElementById("estado_cita");
  const problemas = document.getElementById("problemas");
  alert("si sirve ome ");

  try {
    axios
      .post(
        "guardarcitas",
        {
          Nombre_completo: nombres.value,
          Edad: edades.value,
          genero: generos.value,
          fecha: fecha.value,
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
        alert("sita agendada cono user");
      });
  } catch (error) {
    console.error(error);
  }

}

//function que mustra odontologo en un select
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
