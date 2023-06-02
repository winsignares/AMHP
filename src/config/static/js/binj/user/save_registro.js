function registrarme() {
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
      .post('guardaregistro', {
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
            title: '¡Registro Exitoso!',
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
