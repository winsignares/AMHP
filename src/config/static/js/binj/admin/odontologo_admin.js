//esta funcion muestra los datos en una tabla inmediatamente que se habre la vista
function mostrar() {
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
                <td>${datos[index].nombre}</td>
                <td>${datos[index].direccion}</td>
                <td>${datos[index].telefono}</td>  
                <td>${datos[index].correo}</td> 
                <td>${datos[index].especialidad}</td> 
                <td><a onclick="acualizar_odontologo() "class="btn btn-primary btn-edit">Actualizar</a></td>
                <td><a onclick="eliminar() " class="btn btn-danger btn-eliminar">Eliminar</a></td>
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

//esta es la funcion de guardar paciente(registro) como admin utilizando la ruta de "admin_tabla_paciente.py"

function registrar_odontologo() {
    const Nombre = document.getElementById('Nombre');
    const direccion = document.getElementById('Direccion');
    const Telefono = document.getElementById('Telefono');
    const Correo = document.getElementById('Email');
    const Especialidad = document.getElementById('Especialidad');
    alert('Registrar odontologo')

    axios.post('guardarodontologos_admin', {
        nombre: Nombre.value,
        direccion: direccion.value,
        telefono: Telefono.value,
        correo: Correo.value,
        especialidad: Especialidad.value,


    }, {
        headers: {
            'Content-Type': 'multipart/form-data'

        }
    }
    ).then((res) => {
        console.log(res.data)
        alert("registro existoso")

    })
        .catch((error) => {
            console.error(error)
        })


}
//-----modal de odontologo-----
function acualizar_odontologo() {
    // ... resto del código
    
    // Obtener el modal
    var modal = document.getElementById("myModal_tabla_odontologo_1");
  
    // Abrir el modal
    modal.style.display = "block";
  }
  