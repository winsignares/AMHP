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
                window.location.href = '/otra_vista';  // Reemplaza '/otra_vista' con la URL de la vista deseada
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
