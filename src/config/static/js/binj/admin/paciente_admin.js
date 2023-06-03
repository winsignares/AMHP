

//--------------------------------------------------------------
//esta funcion muestra los datos en una tabla inmediatamente que se habre la vista
function mostrar() {
  const divcate = document.getElementById('tabla');
  axios.get('mostrar_pacientes_admin', {
    responseType: 'json'
  })

    .then(function (response) {
      let datos = response.data
      var length = (Object.keys(datos).length) + 1;
      let mostrar = '';
      i = 0
      for (let index = 1; index < length; index++) {
        mostrar += ` <tr>   
                <td >${datos[index].id}</td>  
                <td >${datos[index].Rol}</td>  
                <td >${datos[index].fecha_de_regitro}</td>  
                <td>${datos[index].Name}</td>
                <td>${datos[index].cedula}</td>
                <td>${datos[index].telefono}</td>  
                <td>${datos[index].direccion}</td>  
                <td>${datos[index].Email}</td>  
                <td>${datos[index].fecha_nacimiento}</td>   
                <td><a onclick="abrir_modal_actualizar(${datos[index].id}) "class="btn btn-primary btn-edit">Actualizar</a></td>
                <td><a onclick="eliminar(${datos[index].id})" class="btn btn-danger btn-eliminar">Eliminar</a></td>
              </tr> `;
      }
      divcate.innerHTML = mostrar
    })
    .catch(function (error) {
      // Maneja los errores aquí
      console.log(error);
    });
}
window.addEventListener('load', function () {
  mostrar();
})



//----------este es el js-------------------------------
function abrir_modal_actualizar(id) {
  // Obtener el modal
  var modal = document.getElementById("myModal_tabla_paciente_admin_actualizar");
  const edwin = document.getElementById("id_nuevo")

  edwin.value = id

  // Abrir el modal
  modal.style.display = "block";
  //cierra el modal en cualquier parte de la pantalla
  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }

  //este es el id del boton
  const btnActualizar = document.getElementById('btn-actualizarpaciente');
  btnActualizar.onclick = function () {
    // Obtener los nuevos valores de los campos del formulario
    const name_new = document.getElementById('Fullname_nuevo');
    const cedula_new = document.getElementById('Cedula_nuevo');
    const telefono_new = document.getElementById('Telefono_nuevo');
    const direccion_new = document.getElementById('Direccion_nuevo');
    const Correo_new = document.getElementById('Correo_nuevo');
    const Fechadenacimento_new = document.getElementById('fecha_nuevo');

    axios.post('actualizar_paciente_admin', {
      id: edwin.value,
      Name: name_new.value,
      cedula: cedula_new.value, 
      telefono: telefono_new.value,
      direccion: direccion_new.value,
      Email: Correo_new.value,
      fecha_nacimiento: Fechadenacimento_new.value
    }, {
      headers: {
        'Content-Type': 'multipart/form-data'

      }
    }
    ).then((res) => {
      console.log(res.data)
      Swal.fire({
        position: 'top-center',
        icon: 'success',
        title: '¡Paciente Actualizado Exitosa mente!',
        showConfirmButton: false,
        timer: 2000,
      })

    })
      .catch((error) => {
        console.error(error)
      })

  }
}


//esta es la funcion de guardar paciente(registro) como admin utilizando la ruta de "admin_tabla_paciente.py"
function registrar_paciente() {
  const name = document.getElementById('Fullname');
  const Cedula = document.getElementById('Cedula');
  const Telefono = document.getElementById('Telefono');
  const Direccion = document.getElementById('Direccion');
  const Correo = document.getElementById('Correo');
  const Fechadenacimento = document.getElementById('fecha');

  // Validar si hay datos en todos los campos
  if (
    name.value === '' ||
    Cedula.value === '' ||
    Telefono.value === '' ||
    Direccion.value === '' ||
    Correo.value === '' ||
    Fechadenacimento.value === ''
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

  axios
    .post('guardarpaciente_admin', {
      Name: name.value,
      cedula: Cedula.value,
      telefono: Telefono.value,
      direccion: Direccion.value,
      Email: Correo.value,
      fecha_nacimiento: Fechadenacimento.value,
    }, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
    .then((res) => {
      console.log(res.data);
      if (res.data === 'Paciente already exists in the database') {
        // Mostrar la alerta de paciente existente
        Swal.fire({
          position: 'top-center',
          icon: 'warning',
          title: 'El paciente ya existe en la base de datos.',
          showConfirmButton: false,
          timer: 2000,
        });
      } else {
        // Mostrar la alerta de éxito
        Swal.fire({
          position: 'top-center',
          icon: 'success',
          title: '¡Paciente Registrado Exitosamente!',
          showConfirmButton: false,
          timer: 2000,
        });

        // Restablecer los valores de los campos
        name.value = '';
        Cedula.value = '';
        Telefono.value = '';
        Direccion.value = '';
        Correo.value = '';
        Fechadenacimento.value = '';
      }
    })
    .catch((error) => {
      console.error(error);
    });
}


//----------------------------------------------------------------
//buscador
function buscadorpaciente() {
  // Obtiene el valor del campo de búsqueda
  var datoabuscar = document.getElementById("buscadorpacienteadmin").value.toUpperCase();

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




//-------------------eliminar---------------------------------------------


function eliminar(id) {
  Swal.fire({
    title: '¿Desea eliminar el paciente?',
    text: 'Esta acción no se puede deshacer',
    imageUrl: '/static/img/eliminar_paciente.png', // Reemplaza 'ruta_de_la_imagen.jpg' con la ruta de la imagen que deseas mostrar
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
        title: 'paciente Eliminado(a) con éxito!',
        icon: 'success'
        
      });
      axios.post('eliminar_paciente_admin', {
        id: id
      })
        .then(function (response) {
          
          console.log(response);
          mostrar();
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
