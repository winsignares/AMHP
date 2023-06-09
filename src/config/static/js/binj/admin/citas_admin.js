//----------------------funcion mostrar tabla de citas
function mostrar_cita_admin_tabla() {
  const divcate = document.getElementById("tabla");

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
                <td>${datos[index].Rol}</td>  
                <td>${datos[index].Nombre_completos}</td>
                <td>${datos[index].Cedula}</td>
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
  mostrar_cita_admin_tabla();
});


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

        opcion.value = datos[index].id_paciente;
        opcion.text = datos[index].Nombre_paciente;


        opcion2.value = datos[index].id_paciente;
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
  const odontlogos = document.getElementById("odontlogos");
  const fecha = document.getElementById("fecha");
  const consultas = document.getElementById("consultas");
  const tarjetas = document.getElementById("tarjetas");
  const cardNumber = document.getElementById("cardNumber");
  const estado_cita = document.getElementById("estado_cita");
  const problemas = document.getElementById("problemas");
  const nombres = document.getElementById("nombre_prueba");


  // Validar si hay datos en todos los campos
  if (
    odontlogos.value === "" ||
    fecha.value === "" ||
    consultas.value === "" ||
    tarjetas.value === "" ||
    cardNumber.value === "" ||
    estado_cita.value === "" ||
    problemas.value === "" ||
    nombres.value === ""

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
        "guardarcitas_admin",
        {


          odontlogos: odontlogos.value,
          fecha: fecha.value,
          consulta: consultas.value,
          tarje_tade_credito: tarjetas.value,
          Num_tarjeta: cardNumber.value,
          cita_estado: estado_cita.value,
          problema: problemas.value,
          Nombre_completo: nombres.value,
        },
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      )
      .then((res) => {
        console.log(res.data);
        mostrar_cita_admin_tabla();
        mostrarnombrepaciente();
        if( res.data=== "se guardo la cita")
         Swal.fire({
          position: 'top-center',
          icon: 'success',
          title: '¡Cita guardada Exitosamente!',
          showConfirmButton: false,
          timer: 2000,
         });

        // Limpiar los valores de los campos después de guardar


        odontlogos.value = "";
        fecha.value = "";
        consultas.value = "";
        tarjetas.value = "";
        cardNumber.value = "";
        estado_cita.value = "";
        problemas.value = "";
        nombres.value = "";
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

        // esta es el select donde va a ingresar 
        opcion.value = datos[index].id_odontologo;
        opcion.text = datos[index].Nombre_odontologo;

        // este es el selctec donde quiere que actualize
        opcion2.value = datos[index].id_odontologo;
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
    const nombres_actualizar = document.getElementById("nombre_paciente_actualizar");
    const odontlogos = document.getElementById("nombre_odontologo_actualizar");
    const fecha = document.getElementById("fecha_actualizar");
    const consultas = document.getElementById("consultas_actualizar");
    const tarjetas = document.getElementById("tarjetas_actualizar");
    const cardNumber = document.getElementById("cardNumber_actualizar");
    const estado_cita = document.getElementById("estado_cita_actualizar");
    const problemas = document.getElementById("problemas_actualizar");


    axios.post('actualizar_citas_admin', {
      id: id_citas.value,
      Nombre_actualizar: nombres_actualizar.value,

      odontlogos_actualizar: odontlogos.value,
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
      if(res.data==="se actualizo cita")
      Swal.fire({
        position: 'top-center',
        icon: 'success',
        title: '¡Cita Actualizada Exitosa mente!',
        showConfirmButton: false,
        timer: 2000,
      })

    })
      .catch((error) => {
        console.error(error)

      })

  }

}

// eliminar citas como admin

function eliminarcitaadmin(id) {
  Swal.fire({
    title: '¿Desea eliminar la Cita?',
    text: 'Esta acción no se puede deshacer',
    imageUrl: '/static/img/odontologo_eliminar.png', // Reemplaza 'ruta_de_la_imagen.jpg' con la ruta de la imagen que deseas mostrar
    imageWidth: 200, // Ancho de la imagen en píxeles
    imageHeight: 200, // Alto de la imagen en píxeles
    imageAlt: 'Imagen de la cita', // Descripción de la imagen
    icon: 'info',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: 'red',
    confirmButtonText: 'Aceptar'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire({
        title: '!Cita Eliminada con éxito!',
        icon: 'success'
      });
      axios.post('eliminar_citas_admin', {
        id: id
      })
        .then(function (response) {
          console.log(response);
          mostrar_cita_admin_tabla();
        })
        .catch(function (error) {
          console.log(error);
        });
    } else {
      Swal.fire({
        title: '¡Cancelado!',
        icon: 'error'
      });
    }
  });
}