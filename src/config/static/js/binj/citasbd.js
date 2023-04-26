function addprovedor() {
    const Nombre_proveedorr = document.getElementById('odontologiaForm').value;
    const correoprovider = document.getElementById('genero').value;
    const Direccionprovider = document.getElementById('consultaDate').value;
    const telefonoprovider = document.getElementById('consulta').value;

   alert('a')
   console.log(Nombre_proveedorr, correoprovider, Direccionprovider, telefonoprovider, responsableprovider)
    axios.post('guardarprovider', {
        
        Nombre_proveedor: Nombre_proveedorr,
        correo: correoprovider,
        Direccion: Direccionprovider,
        telefono: telefonoprovider,
        Descripcion: responsableprovider       

    }, {
        headers: {
        'Content-Type': 'multipart/form-data'

        }
    }).then((res) => {
        console.log(res.data)
    })
    .catch((error) => {
        console.error(error)
    })
}
