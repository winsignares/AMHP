function mostrar() {
    const divcate = document.getElementById('tabla');
    axios.get('mostrar_citas_user',{
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
                <td> <button onclick=" myFunction()">actualizar</button>
                <td> <button onclick=" myFunction()">eliminar</button>
                

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