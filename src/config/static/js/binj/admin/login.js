
function ingrso(){
    
    const usuario = document.getElementById('usuario');
    const contrasena = document.getElementById('contrasena');
    axios.post('login', {
        usuario: usuario.value,
        contraseña: contrasena.value
    })
        .then(function (response) {
            console.log(response)
                window.location.href = '/fronted/indexcita2';
          
              
        })
        .catch(function (error) {
            console.log(error);
           
        });
}




