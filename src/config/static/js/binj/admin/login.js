//--------------------------------------------------------------
//esta funcion muestra los datos en una tabla inmediatamente que se habre la vista
function mostrar_admis() {
  const divcate = document.getElementById('tabla_mostrar_admins');
  axios.get('mostrar_admins', {
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
                <td >${datos[index].tipo_admin}</td>  
                <td >${datos[index].nombre}</td>  
                <td>${datos[index].apellido}</td>
                <td>${datos[index].correo}</td>
                <td>${datos[index].contraseña}</td>
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
  mostrar_admis();
})



function ingreso() {
  const usuario = document.getElementById('usuario');
  const contrasena = document.getElementById('contrasena');

  if (
    usuario.value === '' ||
    contrasena.value === ''

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
  axios.post('login', {
    usuario: usuario.value,
    contraseña: contrasena.value
  })
    .then(function (response) {
      console.log(response);

      if (response.data.status === "Correcto") {
        // Alerta de inicio de sesión exitoso
        Swal.fire({
          position: 'top-center',
          icon: 'success',
          title: '¡Inicio de sesión exitoso!',
          showConfirmButton: false,
          timer: 2000
        });

        // Redirigir a otra vista
        window.location.href = '/fronted/indexcita2';  // Reemplaza '/otra_vista' con la URL de la vista deseada
      } else if (response.data.status === "Error") {
        // Alerta de error con mensaje específico
        Swal.fire({
          position: 'top-center',
          icon: 'error',
          title: 'Error',
          text: response.data.message,
          showConfirmButton: false,
          timer: 2000
        });
      }
    })
    .catch(function (error) {
      console.log(error);
    });
}



//este codigo es para guardar un admin como admin , osea que el que grega otro admin es el mismo
function registro_admin() {
  const name_admin = document.getElementById('nombre_admin');
  const apellido_admin = document.getElementById('apellido_admin');
  const correo_admin = document.getElementById('correo_admin');
  const contra_admin = document.getElementById('conrasena_admin');

  // Validar si hay datos en todos los campos
  if (
    name_admin.value === '' ||
    apellido_admin.value === '' ||
    correo_admin.value === '' ||
    contra_admin.value === ''
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
    .post('guardar_admin', {
      name_admin: name_admin.value,
      apellido_admin: apellido_admin.value,
      correo_admin: correo_admin.value,
      contra_admin: contra_admin.value,
    }, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
    .then((res) => {
      console.log(res.data);
      if (res.data === 'El administrador ya existe en la base de datos') {
        // Mostrar la alerta de administrador existente
        Swal.fire({
          position: 'top-center',
          icon: 'warning',
          title: 'El administrador ya existe en la base de datos.',
          showConfirmButton: false,
          timer: 2000,
        });
      }else if (res.data === "No tienes permiso para realizar esta acción"){
        Swal.fire({
          position: 'top-center',
          icon: 'warning',
          title: 'solo eladmin princiapl puede registrar',
          showConfirmButton: false,
          timer: 2000,
        });
        
      } else {
        // Mostrar la alerta de éxito
        Swal.fire({
          position: 'top-center', 
          icon: 'success',
          title: '¡Administrador registrado exitosamente!',
          showConfirmButton: false,
          timer: 2000,
        });

        // Restablecer los valores de los campos
        name_admin.value = '';
        apellido_admin.value = '';
        correo_admin.value = '';
        contra_admin.value = '';
      }
    })
    .catch((error) => {
      console.error(error);
    });
}
 

// esto es para eliminar al paciente
function eliminar(id) {
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

      axios.post('elimina_admin', {
        id: id
      })
        .then(function (response) {
          mostrar_admis();
          console.log(response);
          if(response.data.message==='admin eliminado correctamente'){

          Swal.fire({
            title: '!admin Eliminado con éxito!',
            icon: 'success'
          });
          
        }
        else if(response.data.message==='No se puede eliminar al administrador principal'){
          Swal.fire({
            title: '!Lo lamento!',
            text: `no puede eliminar admin principal, aunque lo puede actualizar`,
            icon: 'warning'
          });

        } else if(response.data.message==='No se puede eliminar al admin porque tiene citas asociadas'){
          Swal.fire({
            title: '!admin tiene citas asosciadas éxito!',
            icon: 'warning'
          });

        } 
        else if(response.data.message==='No se puede eliminar al admin porque tiene fecha_dispo asociadas'){
          Swal.fire({
            title: '!admin tiene pacientes asosciadas éxito!',
            icon: 'warning'
          });
          
        } else if(response.data.message==='No se puede eliminar al admin porque tiene paciente asociadas'){
          Swal.fire({
            title: '!admin tiene pacientes asosciadas éxito!',
            icon: 'warning'
          });
          
        } else if(response.data.message==='No se puede eliminar al admin porque tiene odontologo asociadas'){
          Swal.fire({
            title: '!admin tiene odontologo asosciadas éxito!',
            icon: 'warning'
          });
          
        }  else {
          Swal.fire({
            title: '¡Cancelado!',
            icon: 'error'
          });
        }
      }
        )
        .catch(function (error) {
          console.log(error);
        });
    } 
 
  });
}





// --------------actualizar citas---------------------
function abrir_modal_actualizar(id) {
  // ... resto del código

  // Obtener el modal
  var modal = document.getElementById("myModal_regritoadmin_actualizar");
  const id_admin = document.getElementById("id_admin")

  id_admin.value = id

  // Abrir el modal
  modal.style.display = "block";
  //cierra el modal en cualquier parte de la pantalla
  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
  //este es el id del boton
  const btnActualizar_admin = document.getElementById('btn-registro_admin_actualizar');
  btnActualizar_admin.onclick = function () {
    // Obtener los nuevos valores de los campos del formulario
    
    const nombre_admin_nuevo = document.getElementById("nombre_admin_nuevo");
    const apellido_admin_nuevo = document.getElementById("apellido_admin_nuevo");
    const correo_admin = document.getElementById("correo_admin_nuevo");
    const conrasena_admin_nuevo = document.getElementById("conrasena_admin_nuevo");


    axios.post('actualizar_admin', {
      id: id_admin.value,
      nombre_admin_nuevo: nombre_admin_nuevo.value,
      apellido_admin_nuevo: apellido_admin_nuevo.value,
      correo_admin: correo_admin.value,
      conrasena_admin_nuevo: conrasena_admin_nuevo.value,
    }, {
      headers: { 
        'Content-Type': 'multipart/form-data'

      }
    }
    ).then((res) => {
      console.log(res.data)

      if(res.data==="se actualizo admin"){
      Swal.fire({
        position: 'top-center',
        icon: 'success',
        title: '¡Admin Actualizada Exitosa mente!',
        showConfirmButton: false,
        timer: 2000,
      });

      nombre_admin_nuevo.value = '';
      apellido_admin_nuevo.value = '';
      correo_admin.value = '';
      conrasena_admin_nuevo.value = '';


    }else if(res.data.message==="El nombre ya existe en otro administrador"){
      Swal.fire({
        title: '!el nombre del admin ya existe en otro admin!',
        icon: 'warning'
      });
      nombre_admin_nuevo.value = '';
    } 
    else if(res.data.message==="El apellido ya existe en otro administrador"){
      Swal.fire({
        title: '!el apellido del admin ya existe en otro admin!',
        icon: 'warning'
      });
      apellido_admin_nuevo.value = '';
      
    } else if(res.data.message==="El correo ya existe en otro administrador"){
      Swal.fire({
        title: '!el correo del admin ya existe en otro admin!',
        icon: 'warning'
      });
      correo_admin.value = '';
      
    } 
  }
    )
    .catch(function (error) {
      console.log(error);
    });
} 

}





