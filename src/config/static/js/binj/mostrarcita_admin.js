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
function actualizar() {
    // se hace que actualize solo la funcion
    $(document).on('click', '.btn-edit', function(e){
        e.preventDefault();
        console.log("si funciona")

    });
    $(document).on('click', '.btn-eliminar', function(e){
        e.preventDefault();
        console.log("si funciona")

    });
    $(document).ready(function() {
        $("#boton-buscar").click(function() {
          var value = $("#buscador").val().toLowerCase();
          $("#tabla tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
          });
        });
      });
      
      
}
