function admin(){
    var usuario, contrasena

    usuario = document.getElementById('usuario').value;
    contrasena = document.getElementById('contrasena').value;

    if (usuario == "admin" && contrasena == "1234"){ //condicional ternario (usar "==" o "equals") y usar "==" para iguales, "equals" para diferentes.
        window.location.href = 'fronted/indexprincipal'; //redirigimos al inicio. Para modificar el nombre del document
    }
    else{ //condicional if por condicional (usar "else if" o "elif") y usar "else" para sal
        alert("Usuario o contraseña incorrectos"); //alerta de texto. Para modificar el título del m

    }
}