function addprocita() {
    const nombre = document.getElementById('nombre').value;
    const edad = document.getElementById('edad').value;
    const cardNumber = document.getElementById('cardNumber').value;

    console.log(nombre, edad, cardNumber);

    try {
        axios.post('guardarcita', {
            Nombre_completo: nombre,
            Edad: edad,
            Num_tarjeta: cardNumber
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
