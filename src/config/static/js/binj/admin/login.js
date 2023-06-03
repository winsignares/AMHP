
function ingrso(){
    
    const usuario = document.getElementById('usuario');
    const contrasena = document.getElementById('contrasena');
    axios.post('login', {
        usuario: usuario.value,
        contraseña: contrasena.value
    })
        .then(function (response) {
            console.log(response)
        //alerta de inicio de seccion
            // Swal.fire({
            //     position: 'top-center',
            //     icon: 'success',
            //     title: '¡seccion exitosa!',
            //     showConfirmButton: false,
            //     timer: 2000
            // });
          
              window.location.href = '/fronted/indexcita2'
        })
        .catch(function (error) {
            console.log(error);
           
        });
}




