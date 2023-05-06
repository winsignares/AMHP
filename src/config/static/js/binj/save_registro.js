
function registrarme() {
    const name = document.getElementById('name');
    const Cedula = document.getElementById('Cedula');
    const Telefono = document.getElementById('Telefono');
    const Direccion = document.getElementById('Direccion');
    const Correo = document.getElementById('Correo');
    const Fechadenacimento = document.getElementById('fecha');
    alert('Registrar')

    axios.post('guardaregistro', {
        Name: name.value,
        cedula: Cedula.value,
        telefono: Telefono.value,
        direccion: Direccion.value,
        Email: Correo.value,
        fecha_nacimiento: Fechadenacimento.value
        

    }, {
        headers: {
        'Content-Type': 'multipart/form-data'

        }
    }
    ).then((res) => {
        console.log(res.data)
        alert("registro existoso")
        window.location.href = "/fronted/indexprincipal";
    })
    .catch((error) => {
        console.error(error)
    })

    
}