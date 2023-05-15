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
    mostrar();
})
//funcion que elimina 
function eliminar_odontologo(id) {
    axios.post('eliminar_odontologo_admin', {
        id: id
    })
        .then(function (response) {
            // Manejar la respuesta de éxito aquí
            console.log(response);
            // Ejecutar la función mostrar() nuevamente para actualizar la tabla
            mostrar();
        })
        .catch(function (error) {
            // Manejar los errores aquí
            console.log(error);
        });
}
//-------------------eliminar---------------------------------------------
// function eliminar(id) {
//     axios.post('eliminar_paciente_admin', {
//         id: id
//     })
//     .then(function (response) {
//         // Manejar la respuesta de éxito aquí
//         console.log(response);
//         // Ejecutar la función mostrar() nuevamente para actualizar la tabla
//         mostrar();
//     })
//     .catch(function (error) {
//         // Manejar los errores aquí
//         console.log(error);
//     });
//   }
//esta es la funcion de guardar paciente(registro) como admin utilizando la ruta de "admin_tabla_paciente.py"

function registrar_odontologo() {
    const Nombre = document.getElementById('nombres');
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
        especialidad: Especialidad.value


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
        alert('Registrar odontologo')
    
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
            alert("se actualizio con exito")

        })
            .catch((error) => {
                console.error(error)
            })

    }

}
