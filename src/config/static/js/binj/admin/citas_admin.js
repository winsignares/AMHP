//----------------------funcion mostrar tabla de citas
function mostrar() {
  const divcate = document.getElementById("tabla");
  const selectnombre = document.getElementById("nombre_prueba");
  axios
    .get("mostrar_citas_admin", {
      responseType: "json",
    })

    .then(function (response) {
      let datos = response.data;
      var length = Object.keys(datos).length + 1;
      let mostrar = "";
      i = 0;
      for (let index = 1; index < length; index++) {
        mostrar += ` <tr>   
                <td>${datos[index].id}</td>  
                <td>${datos[index].Nombre_completos}</td>
                <td>${datos[index].Edad}</td>
                <td>${datos[index].genero}</td>  
                <td>${datos[index].fecha}</td>  
                <td>${datos[index].consulta}</td>  
                <td>${datos[index].tarje_credi}</td>  
                <td>${datos[index].Num_tarjeta}</td>  
                <td>${datos[index].estado_citas}</td>  
                <td>${datos[index].problema}</td>  
                <td><a onclick="actualizar_citas()"class="btn btn-primary btn-edit">Actualizar</a></td>
                <td><a onclick="eliminar() " class="btn btn-danger btn-eliminar">Eliminar</a></td>
              </tr> `;
     
      }
      divcate.innerHTML = mostrar;
    })
    .catch(function (error) {
      // Maneja los errores aquí
      console.log(error);
    });
}
window.addEventListener("load", function () {
  mostrar();
});
//---------------mostrar nombre de pacientes en un select---------------
function mostrarcategoriabooks() {
  const selectnombre = document.getElementById("nombre_prueba");
  axios.get("obtener_nombres_pacientes", {
      responseType: "json",
    })

    .then(function (response) {
      let datos = response.data;
      var length = Object.keys(datos).length + 0;
     
      i = 0;
      for (let index = 0; index < length; index++) {
       
        const opcion = document.createElement("option");
        
        opcion.text = datos[index].Nombre_paciente;
        selectnombre.appendChild(opcion);
      }
      
    })
    .catch(function (error) {
      // Maneja los errores aquí
      console.log(error);
    });
}
window.addEventListener("load", function () {
  mostrarcategoriabooks();
});

//-----------------------agendar citas-------------------------------------------------//
//esta es la funcion de guardar citas como admin utilizando la ruta de "citas.py"
function guardar_cita_admin() {
  const nombres = document.getElementById("nombre_prueba");
  const edades = document.getElementById("edades");
  const generos = document.getElementById("generos");
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
        "guardarcitas_admin",
        {
          Nombre_completo: nombres.value,
          Edad: edades.value,
          genero: generos.value,
          fecha: fecha.value,
          consulta: consultas.value,
          tarje_tade_credito: tarjetas.value,
          Num_tarjeta: cardNumber.value,
          cita_estado: estado_cita.value,
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
        alert("cita admin");
      });
  } catch (error) {
    console.error(error);
  }
}

function buscadordecitas() {
  // Obtiene el valor del campo de búsqueda
  var datoabuscar = document
    .getElementById("buscadorcitasadmin")
    .value.toUpperCase();

  // Obtiene la tabla y los registros de la misma
  var tabla = document.getElementById("tabla");
  var rows = tabla.getElementsByTagName("tr");

  // Itera sobre los registros y los oculta si no coinciden con la búsqueda
  for (var i = 0; i < rows.length; i++) {
    var cells = rows[i].getElementsByTagName("td");
    var match = false;
    for (var j = 0; j < cells.length; j++) {
      if (cells[j].innerHTML.toUpperCase().indexOf(datoabuscar) > -1) {
        match = true;
        break;
      }
    }
    if (match) {
      rows[i].style.display = "";
    } else {
      rows[i].style.display = "none";
    }
  }
}
//-----modal de citas-----
function actualizar_citas() {
  // ... resto del código

  // Obtener el modal
  var modal = document.getElementById("myModal_tabla_admin_1");

  // Abrir el modal
  modal.style.display = "block";
}



