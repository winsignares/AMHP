
function ingrso(){
    
    const user = document.getElementById('usuario');
    const contrasena = document.getElementById('contrasena');
    axios.post('login', {
        usuario: user.value,
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