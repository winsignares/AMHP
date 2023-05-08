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
                <td><a onclick="actualizar() "class="btn btn-primary btn-edit">Actualizar</a></td>
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
    const name = document.getElementById('nombre');
    const Cedula = document.getElementById('Cedula');
    const Telefono = document.getElementById('Telefono');
    const Direccion = document.getElementById('Direccion');
    const Correo = document.getElementById('Correo');
    const Fechadenacimento = document.getElementById('fecha');
    alert('Registrar paci')

    axios.post('guardarpaciente_admin', {
        Names: name.value,
        cedulas: Cedula.value,
        telefonos: Telefono.value,
        direccions: Direccion.value,
        Emails: Correo.value,
        fecha_nacimientos: Fechadenacimento.value
        

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