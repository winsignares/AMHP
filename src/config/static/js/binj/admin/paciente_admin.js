//esta funcion muestra los datos en una tabla inmediatamente que se habre la vista
function mostrar() {
    const divcate = document.getElementById('tabla');
    axios.get('mostrar_pacientes_admin',{
        responseType: 'json'
    } )
      
      .then(function (response) {
            let datos = response.data
            var length = (Object.keys(datos).length) + 1;
            let mostrar = '';
            i= 0
            for (let index = 1; index < length; index++) {
                mostrar += ` <tr>   
                <td>${datos[index].id}</td>  
                <td>${datos[index].Name}</td>
                <td>${datos[index].cedula}</td>
                <td>${datos[index].telefono}</td>  
                <td>${datos[index].direccion}</td>  
                <td>${datos[index].Email}</td>  
                <td>${datos[index].fecha_nacimiento}</td>  
                <td><a onclick="mostrarModalActualizar() "class="btn btn-primary btn-edit">Actualizar</a></td>
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
window.addEventListener('load', function() {
    mostrar();
})
  
//esta es la funcion de guardar paciente(registro) como admin utilizando la ruta de "admin_tabla_paciente.py"

function registrar_paciente() {
    const name = document.getElementById('Fullname');
    const Cedula = document.getElementById('Cedula');
    const Telefono = document.getElementById('Telefono');
    const Direccion = document.getElementById('Direccion');
    const Correo = document.getElementById('Correo');
    const Fechadenacimento = document.getElementById('fecha');
    alert('Registrar')

    axios.post('guardarpaciente_admin', {
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
        
    })
    .catch((error) => {
        console.error(error)
    })

}
// Función para mostrar el modal de actualizar
function mostrarModalActualizar() {
    // Obtener el modal
    var modal = document.getElementById("modalActualizar");
    // Mostrar el modal
    modal.style.display = "block";
  }
  
  // Función para cerrar el modal de actualizar
  function cerrarModalActualizar() {
    // Obtener el modal
    var modal = document.getElementById("modalActualizar");
    // Ocultar el modal
    modal.style.display = "none";
  }
  
  // Agregar un evento al botón de cerrar del modal
  var cerrar = document.getElementsByClassName("close1")[0];
  cerrar.onclick = function() {
    cerrarModalActualizar();
  }
  
  // Agregar un evento al hacer clic fuera del modal
  window.onclick = function(event) {
    var modal = document.getElementById("modalActualizar");
    if (event.target == modal) {
      cerrarModalActualizar();
    }
  }
  