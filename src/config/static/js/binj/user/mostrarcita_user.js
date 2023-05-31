//esta es el js que hace el filtro
function buscar_citas_user() { 
  const divcate = document.getElementById('tabla');
  const ids = document.getElementById('buscarcitasuser_id');
  alert("sisi")
  axios.post('buscarcita_user', {
    buscar: ids.value
      
  })
  .then(function (response) {
    let datos = response.data
    var length = (Object.keys(datos).length) + 1;
    let mostrar = '';
    i= 0
    for (let index = 1; index < length; index++) {
      mostrar += `<tr>
      <td>${datos[index].id}</td>
      <td>${datos[index].Nombre_completos}</td>
      <td>${datos[index].Edad}</td>
      <td>${datos[index].nombre_odontologos}</td>
      <td>${datos[index].fecha}</td>
      <td>${datos[index].consulta}</td>
      <td>${datos[index].estado_citas}</td>
      <td>${datos[index].problema}</td>
      <td><a onclick="actualizar()" class="btn btn-primary btn-edit">Actualizar</a></td>
      <td><a onclick="eliminar()" class="btn btn-danger btn-eliminar">Eliminar</a></td>
    </tr>`;
        
    }
    divcate.innerHTML = mostrar        
})
.catch(function (error) {
// Maneja los errores aquí
console.log(error);
});
}




