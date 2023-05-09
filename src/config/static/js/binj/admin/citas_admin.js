
//-----------------------------modal--------------------------------------------

// Función para mostrar el modal de actualizar
function mostrarModalActualizar2() {
  // Obtener el modal
  var tablaadmin = document.getElementById("tablaadmin");
  // Mostrar el modal
  tablaadmin.style.display = "block";
}

// Función para cerrar el modal de actualizar
function cerrarModalActualizar2() {
  // Obtener el modal
  var tablaadmin = document.getElementById("tablaadminr");
  // Ocultar el modal
  tablaadmin.style.display = "none";
}

// Agregar un evento al botón de cerrar del modal
var cerrar = document.getElementsByClassName("close1")[0];
cerrar.onclick = function() {
  cerrarModalActualizar2();
}

// Agregar un evento al hacer clic fuera del modal
window.onclick = function(event) {
  var modal = document.getElementById("tablaadmin");
  if (event.target == modal) {
    cerrarModalActualizar2();
  }
}



//----------------------funcion mostrar tabla de citas 
function mostrar() {
    const divcate = document.getElementById('tabla');
    axios.get('mostrar_citas_admin',{
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
                <td>${datos[index].Nombre_completo}</td>
                <td>${datos[index].Edad}</td>
                <td>${datos[index].genero}</td>  
                <td>${datos[index].fecha}</td>  
                <td>${datos[index].consulta}</td>  
                <td><a onclick="mostrarModalActualizar2() "class="btn btn-primary btn-edit">Actualizar</a></td>
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


//-----------------------agendar citas-------------------------------------------------//
//esta es la funcion de guardar citas como admin utilizando la ruta de "citas.py"
function guardar_cita_admin() {
  const nombres = document.getElementById('nombre');
  const edades = document.getElementById('edad');
  const generos= document.getElementById('generos');
  const fecha = document.getElementById('fecha');
  const consultas = document.getElementById('consultas');
  const tarjetas= document.getElementById('tarjetas');
  const cardNumber = document.getElementById('cardNumber');
  const problemas = document.getElementById('problemas');
  alert('si sirve ome ')
  try {
      axios.post('guardarcitas', {
          Nombre_completo: nombres.value,
          Edad: edades.value,
          genero: generos.value,
          fecha: fecha.value,
          consulta: consultas.value,
          tarje_tade_credito: tarjetas.value,
          Num_tarjeta: cardNumber.value,
          problema: problemas.value,
          
      }, {
          headers: {
              'Content-Type': 'multipart/form-data'
          }
      }).then((res) => {
          console.log(res.data)
          
      })
  } catch (error) {
      console.error(error)
  }
}

function buscadordecitas() {
  // Obtiene el valor del campo de búsqueda
  var datoabuscar = document.getElementById("buscadorcitasadmin").value.toUpperCase();
  
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