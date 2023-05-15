

//--------------------------------------------------------------
//esta funcion muestra los datos en una tabla inmediatamente que se habre la vista
function mostrar() {
  const divcate = document.getElementById('tabla');
  axios.get('mostrar_pacientes_admin', {
    responseType: 'json'
  })

    .then(function (response) {
      let datos = response.data
      var length = (Object.keys(datos).length) + 1;
      let mostrar = '';
      i = 0
      for (let index = 1; index < length; index++) {
        mostrar += ` <tr>   
                <td >${datos[index].id}</td>  
                <td>${datos[index].Name}</td>
                <td>${datos[index].cedula}</td>
                <td>${datos[index].telefono}</td>  
                <td>${datos[index].direccion}</td>  
                <td>${datos[index].Email}</td>  
                <td>${datos[index].fecha_nacimiento}</td>   
                <td><a onclick="abrir_modal_actualizar(${datos[index].id}) "class="btn btn-primary btn-edit">Actualizar</a></td>
                <td><a onclick="eliminar(${datos[index].id})" class="btn btn-danger btn-eliminar">Eliminar</a></td>
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



//----------este es el js-------------------------------
function abrir_modal_actualizar(id) {
  // Obtener el modal
  var modal = document.getElementById("myModal_tabla_paciente_admin_actualizar");
  const edwin = document.getElementById("id_nuevo")

  edwin.value = id

  // Abrir el modal
  modal.style.display = "block";
  //cierra el modal en cualquier parte de la pantalla
  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }


  //este es el id del boton
  const btnActualizar = document.getElementById('btn-actualizarpaciente');
  btnActualizar.onclick = function () {
    // Obtener los nuevos valores de los campos del formulario
    const name_new = document.getElementById('Fullname_nuevo');
    const cedula_new = document.getElementById('Cedula_nuevo');
    const telefono_new = document.getElementById('Telefono_nuevo');
    const direccion_new = document.getElementById('Direccion_nuevo');
    const Correo_new = document.getElementById('Correo_nuevo');
    const Fechadenacimento_new = document.getElementById('fecha_nuevo');

    alert('Registrar')
    axios.post('actualizar_paciente_admin', {
      id: edwin.value,
      Name: name_new.value,
      cedula: cedula_new.value, 
      telefono: telefono_new.value,
      direccion: direccion_new.value,
      Email: Correo_new.value,
      fecha_nacimiento: Fechadenacimento_new.value
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
//-------------------eliminar---------------------------------------------
function eliminar(id) {
  axios.post('eliminar_paciente_admin', {
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

//----------------------------------------------------------------
//buscador
function buscadorpaciente() {
  // Obtiene el valor del campo de búsqueda
  var datoabuscar = document.getElementById("buscadorpacienteadmin").value.toUpperCase();

  // Obtiene la tabla y los registros de la misma
  var tabla = document.getElementById("tabla");
  var rows = tabla.getElementsByTagName("tr");

  // Itera sobre los registros y los oculta si no coinciden con la búsqueda
  for (var i = 0; i < rows.length; i++) {
    var cells = rows[i].getElementsByTagName("td");
    var match = false;
    for (var j = 0; j < cells.length; j++) {
      if (cells[j].innerHTML.toUpperCase().indexOf(datoabuscar) > -1) {
        match = true;
        break;
      }
    }
    if (match) {
      rows[i].style.display = "";
    } else {
      rows[i].style.display = "none";
    }
  }
}


// //-------modal paciente de actualizar-----
// function actualizar_paciente() {
//   // Obtener el modal
//   var modal = document.getElementById("myModal_tabla_paciente_admin_actualizar");
//   // Abrir el modal
//   modal.style.display = "block";
//   //se cierra el modal con solo pressionar afuera de el
// window.onclick = function (event) {
//     if (event.target == modal) {
//       modal.style.display = "none";
//     }
//   }
// }
