

function buscar_citas_user() {
  const divcate = document.getElementById('tabla');
  const codigo_cita_buscar = document.getElementById('buscarcitasuser_id');

  axios.post('der', {
    codigo_cita_buscar: codigo_cita_buscar.value,
    
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
        <td>${datos[index].codigo_cita}</td>
        <td>${datos[index].fechas_disponissss}</td>
      <td>${datos[index].Nombre_completos}</td>
      <td>${datos[index].nombre_odontologos}</td> 

      <td>${datos[index].consulta}</td>  
      <td>${datos[index].estado_citas}</td> 
      <td>${datos[index].problema}</td>
        
              </tr> `;
      }
      divcate.innerHTML = mostrar
    })
    .catch(function (error) {
      // Maneja los errores aquí
      console.log(error);
    });
}
// window.addEventListener('load', function () {
//   mostrar_pssaciente();
// })




