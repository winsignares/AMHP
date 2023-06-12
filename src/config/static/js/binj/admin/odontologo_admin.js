//esta funcion muestra los datos en una tabla inmediatamente que se habre la vista
function mostrar_odontologo() {
    const divcate = document.getElementById('tabla');
    axios.get('mostrar_odontologos_admin', {
        responseType: 'json'
    })

        .then(function (response) {
            let datos = response.data
            var length = (Object.keys(datos).length) + 1;
            let mostrar = '';
            i = 0
            for (let index = 1; index < length; index++) {
                mostrar += ` <tr>   
                <td>${datos[index].id}</td>  
                <td>${datos[index].Rol}</td>  
                <td>${datos[index].nombre_admin}</td>  
                <td>${datos[index].fecha_de_regitro}</td>  
                <td>${datos[index].nombre}</td>
                <td>${datos[index].cedula}</td>
                <td>${datos[index].direccion}</td>
                <td>${datos[index].telefono}</td>  
                <td>${datos[index].correo}</td> 
                <td>${datos[index].especialidad}</td> 
                <td><a onclick="acualizar_odontologo(${datos[index].id}) "class="btn btn-primary btn-edit">Actualizar</a></td>
                <td><a onclick="eliminar_odontologo(${datos[index].id}) " class="btn btn-danger btn-eliminar">Eliminar</a></td>
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
  mostrar_odontologo();
})


// ----------------guardar odontologo----------------------
function registrar_odontologo() {
  const Nombre = document.getElementById('nombres');
  const cedula_odon = document.getElementById('cedula_odon');
  const direccion = document.getElementById('Direccion');
  const Telefono = document.getElementById('Telefono');
  const Correo = document.getElementById('Email');
  const Especialidad = document.getElementById('Especialidad');

  // Validar si hay datos en todos los campos
  if (
    Nombre.value === '' ||
    cedula_odon.value === '' ||
    direccion.value === '' ||
    Telefono.value === '' ||
    Correo.value === '' ||
    Especialidad.value === ''
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
    .post('guardarodontologos_admin', {
      nombre: Nombre.value,
      cedula_odon: cedula_odon.value,
      direccion: direccion.value,
      telefono: Telefono.value,
      correo: Correo.value,
      especialidad: Especialidad.value,
    }, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
    .then((res) => {
      console.log(res.data);
      mostrar_odontologo();
      if (res.data === 'El odontólogo ya existe en la base de datos') {
        // Mostrar la alerta de odontólogo existente
        Swal.fire({
          position: 'top-center',
          icon: 'warning',
          title: 'El odontólogo ya existe en la base de datos.',
          showConfirmButton: false,
          timer: 2000,
        });
      } else {
        // Mostrar la alerta de éxito
        Swal.fire({
          position: 'top-center',
          icon: 'success',
          title: '¡Odontólogo registrado exitosamente!',
          showConfirmButton: false,
          timer: 2000,
        });

        // Restablecer los valores de los campos
        Nombre.value = '';
        cedula_odon.value = '';
        direccion.value = '';
        Telefono.value = '';
        Correo.value = '';
        Especialidad.value = '';
      }
    })
    .catch((error) => {
      console.error(error);
    });

  }
//-----modal de odontologo-----
function acualizar_odontologo(id) {
    // ... resto del código

    // Obtener el modal
    var modal2 = document.getElementById("myModal_tabla_odontologo_2");
    const odontologo = document.getElementById("id_nuevo2")

    odontologo.value = id

    // Abrir el modal
    modal2.style.display = "block";
    //cierra el modal en cualquier parte de la pantalla
    window.onclick = function (event) {
        if (event.target == modal2) {
            modal2.style.display = "none";
        }
    }
    //este es el id del boton
    const btnActualizar2 = document.getElementById('btn-actualizarmedico');
    btnActualizar2.onclick = function () {
        // Obtener los nuevos valores de los campos del formulario
        const nombres_nuevo2 = document.getElementById('nombres_nuevo2');
        const Direccion_nuevo2 = document.getElementById('Direccion_nuevo2');
        const Telefono_nuevo2 = document.getElementById('Telefono_nuevo2');
        const Email_nuevo2 = document.getElementById('Email_nuevo2');
        const Especialidad_nuevo2 = document.getElementById('Especialidad_nuevo2');
      
    
        axios.post('actualizar_odontologos_admin', {
            id: odontologo.value,
            nombre: nombres_nuevo2.value,
            direccion: Direccion_nuevo2.value,
            telefono: Telefono_nuevo2.value,
            correo: Email_nuevo2.value,
            especialidad: Especialidad_nuevo2.value
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
                title: 'Odontologo Actualizado Exitosa mente!',
                showConfirmButton: false,
                timer: 2000,
              })

        })
            .catch((error) => {
                console.error(error)
            })

    }

}


//funcion que elimina Odontologo

function eliminar_odontologo(id) {
  Swal.fire({
    title: '¿Desea eliminar al Odontologo(a)?',
    text: 'Esta acción no se puede deshacer',
    imageUrl: '/static/img/odontologo_eliminar.png',
    imageWidth: 200,
    imageHeight: 200,
    imageAlt: 'Imagen de la cita',
    icon: 'info',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: 'red',
    confirmButtonText: 'Aceptar'
  }).then((result) => {
    if (result.isConfirmed) {
      axios.post('eliminar_odontologo_admin', {
        id: id
      })
        .then(function (response) {
          console.log(response);
          if (response.data.message === 'odontologo eliminado correctamente') {
            Swal.fire({
              title: '¡Odontologo(a) eliminado(a) con éxito!',
              icon: 'success'
            });
            mostrar_odontologo();
          } else if (response.data.message === 'No se puede eliminar el odontologo porque tiene citas asociadas') {
            Swal.fire({
              title: 'No se puede eliminar el odontologo',
              text: 'El odontologo tiene citas asociadas',
              icon: 'warning'
            });
          } else {
            Swal.fire({
              title: 'Error al eliminar el odontologo',
              icon: 'error'
            });
          }
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