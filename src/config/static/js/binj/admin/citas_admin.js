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
                <td>${datos[index].nombre_odontologos}</td>  
                <td>${datos[index].fecha}</td>  
                <td>${datos[index].consulta}</td>  
                <td>${datos[index].tarje_credi}</td>  
                <td>${datos[index].Num_tarjeta}</td>  
                <td>${datos[index].estado_citas}</td>  
                <td>${datos[index].problema}</td>  
                <td><a onclick="actualizar_citas_admin(${datos[index].id})"class="btn btn-primary btn-edit">Actualizar</a></td>
                <td><a onclick="eliminarcitaadmin(${datos[index].id}) " class="btn btn-danger btn-eliminar"">Eliminar</a></td>
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

// eliminar citas como admin
function eliminarcitaadmin(id) {
  axios.post('eliminar_citas_admin', {
      id: id
  })
      .then(function (response) {
          // Manejar la respuesta de éxito aquí
          console.log(response);
          // Ejecutar la función mostrar() nuevamente para actualizar la tabla
          mostrar();
      })
      .catch(function (error) {
          // Manejar los errores aquí
          console.log(error);
      });
}


//---------------mostrar nombre de pacientes en un select---------------
function mostrarnombrepaciente() {
  //este mustra en el select del modal de agendar citas
  const selectnombre = document.getElementById("nombre_prueba");
  // aqui mustra en el select del modal de actualizar
  const selectnombre2 = document.getElementById("nombre_paciente_actualizar");
  axios
    .get("obtener_nombres_pacientes", {
      responseType: "json",
    })

    .then(function (response) {
      let datos = response.data;
      var length = Object.keys(datos).length + 0;

      i = 0;
      for (let index = 0; index < length; index++) {
        const opcion = document.createElement("option");
        const opcion2 = document.createElement("option");

        opcion.text = datos[index].Nombre_paciente;
        opcion2.text = datos[index].Nombre_paciente;
        
        selectnombre.appendChild(opcion);
        selectnombre2.appendChild(opcion2);
      }
    })
    .catch(function (error) {
      // Maneja los errores aquí
      console.log(error);
    });
}
window.addEventListener("load", function () {
  mostrarnombrepaciente();
});

//-----------------------agendar citas-------------------------------------------------//
//esta es la funcion de guardar citas como admin utilizando la ruta de "citas.py"
function guardar_cita_admin() {
  const nombres = document.getElementById("nombre_prueba");
  const edades = document.getElementById("edades");
  const odontlogos = document.getElementById("odontlogos");
  const fecha = document.getElementById("fecha");
  const consultas = document.getElementById("consultas");
  const tarjetas = document.getElementById("tarjetas");
  const cardNumber = document.getElementById("cardNumber");
  const estado_cita = document.getElementById("estado_cita");
  const problemas = document.getElementById("problemas");
  alert("si sirve ome ");
  try {
    axios.post("guardarcitas_admin",
      {
        Nombre_completo: nombres.value,
        Edad: edades.value,
        odontlogos: odontlogos.value,
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
//--------------------buscador de citas --------------------------------------------
//esta funcion busca las citas en la tabla
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



//function que mustra odontologo en un select
function mostrarnombre_odontologo() {
  const selectodontologo = document.getElementById("odontlogos");
  const selectodontologo2 = document.getElementById("nombre_odontologo_actualizar");
  axios
    .get("obtener_nombres_odonlogo", {
      responseType: "json",
    })

    .then(function (response) {
      let datos = response.data;
      var length = Object.keys(datos).length + 0;

      i = 0;
      for (let index = 0; index < length; index++) {
        const opcion = document.createElement("option");
        const opcion2 = document.createElement("option");

        opcion.text = datos[index].Nombre_odontologo;
        opcion2.text = datos[index].Nombre_odontologo;
        selectodontologo.appendChild(opcion);
        selectodontologo2.appendChild(opcion2);

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


// --------------actualizar citas---------------------
function actualizar_citas_admin(id) {
  // ... resto del código

  // Obtener el modal
  var modal = document.getElementById("myModal_tabla_admin_actualizar");
  const id_citas = document.getElementById("id_citas_actualizar")

  id_citas.value = id

  // Abrir el modal
  modal.style.display = "block";
  //cierra el modal en cualquier parte de la pantalla
  window.onclick = function (event) {
      if (event.target == modal) {
          modal.style.display = "none";
      }
  }
  //este es el id del boton
  const btnActualizar_cita_amin = document.getElementById('btn-actualizarcita_admin');
  btnActualizar_cita_amin.onclick = function () {
      // Obtener los nuevos valores de los campos del formulario
      const nombres = document.getElementById("nombre_paciente_actualizar");
      const edades = document.getElementById("edad_actualizar");
      const odontlogos = document.getElementById("nombre_odontologo_actualizar");
      const fecha = document.getElementById("fecha_actualizar");
      const consultas = document.getElementById("consultas_actualizar");
      const tarjetas = document.getElementById("tarjetas_actualizar");
      const cardNumber = document.getElementById("cardNumber_actualizar");
      const estado_cita = document.getElementById("estado_cita_actualizar");
      const problemas = document.getElementById("problemas_actualizar");
      alert('actualizar_citas')
  
      axios.post('actualizar_citas_admin', {
        id:id_citas.value,
        Nombre_completo: nombres.value,
        Edad: edades.value,
        odontlogos: odontlogos.value,
        fecha: fecha.value,
        consulta: consultas.value,
        tarje_tade_credito: tarjetas.value,
        Num_tarjeta: cardNumber.value,
        cita_estado: estado_cita.value,
        problema: problemas.value,
      }, {
          headers: {
              'Content-Type': 'multipart/form-data'

          }
      }
      ).then((res) => {
          console.log(res.data)
          alert("se actualizio citas con exito")

      })
          .catch((error) => {
              console.error(error)
              alert("no se pudo actualizar")
          })

  }

}
