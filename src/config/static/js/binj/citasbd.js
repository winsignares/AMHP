function addprocita() {
    const nombress = document.getElementById('nombre').value;
    const edad = document.getElementById('edad').value;
   // const genero = document.getElementById('genero').value;
   // const fecha = document.getElementById('consultaDate').value;
   // const consulta = document.getElementById('consulta').value;
   // const tarje_tade_credito = document.getElementById('tarjeta').value;
    const numero_de_tarjeta = document.getElementById('cardNumber').value;

   alert('a')
    axios.post('guardarcita', {
        
        nombre: nombress,
        edad: edad,
       // genero: genero,
       // consultaDate: fecha,
       // consulta: consulta,       
       // tarjeta: tarje_tade_credito,     
        cardNumber: numero_de_tarjeta       

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
