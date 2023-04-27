// Función para manejar el envío del formulario
document.getElementById('odontologiaForm').addEventListener('submit', function (event) {
    event.preventDefault();

    // Obtener los datos del formulario
    var nombre = document.getElementById('nombre').value;
    var edad = document.getElementById('edad').value;
    var genero = document.getElementById('genero').value;
    var consulta = document.getElementById('consulta').value;

    // Validar los campos del formulario
    if (nombre === '' || edad === '' || genero === '' || consulta === '') {
        // Mostrar mensaje de error
        document.getElementById('mensajeError').style.display = 'block';
        setTimeout(function () {
            document.getElementById('mensajeError').style.display = 'none';
        }, 3000); // Ocultar mensaje de error después de 3 segundos
    } else {
        // Enviar formulario (aquí puedes agregar tu lógica de envío del formulario)
        // Mostrar mensaje de éxito
        document.getElementById('mensajeExito').style.display = 'block';
        setTimeout(function () {
            document.getElementById('mensajeExito').style.display = 'none';
        }, 3000); // Ocultar mensaje de éxito después de 3 segundos

        // Restablecer el formulario
        document.getElementById('odontologiaForm').reset();
    }
});
// Obtén los elementos del campo de número de tarjeta y fecha de vencimiento
var expiryDateInput = document.getElementById('expiryDate');
var consultaDateInput = document.getElementById('consultaDate');


// Agrega un evento de cambio al campo de fecha de vencimiento
expiryDateInput.addEventListener('change', function(event) {
    // Oculta el valor del campo de fecha de vencimiento
    var expiryDateValue = event.target.value;
    var hiddenExpiryDateValue = '';
    for (var i = 0; i < expiryDateValue.length; i++) {
        hiddenExpiryDateValue += '*';
    }
    event.target.value = hiddenExpiryDateValue;
});

// Agrega un evento de cambio al campo de fecha de consulta
consultaDateInput.addEventListener('change', function(event) {
    // Oculta el valor del campo de fecha de consulta
    var consultaDateValue = event.target.value;
    var hiddenConsultaDateValue = '';
    for (var i = 0; i < consultaDateValue.length; i++) {
        hiddenConsultaDateValue += '*';
    }
    event.target.value = hiddenConsultaDateValue;
});
