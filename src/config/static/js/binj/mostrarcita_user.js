function mostrar() {
    const divcate = document.getElementById('tabla');
    axios.get('mostrar_citas',{
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
                <td>${datos[index].Username}</td>   
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
/*
function habilitar() {
    nom = document.getElementById("nombre").value;
    edadd = document.getElementById("edad").value;
    gene = document.getElementById("generos").value;
    fecha = document.getElementById("consultaDates").value;
    consul = document.getElementById("consultas").value;
    tarje = document.getElementById("tarjetas").value;
    num = document.getElementById("cardNumber").value;
    val = 0;
    if (nom == "") {
        val++;
    }
    if (edadd == "") {
        val++;
    }if (gene == "") {
        val++;
    }if (fecha == "") {
        val++;
    }if (consul== "") {
        val++;
    }if (tarje == "") {
        val++;
    }if (num == "") {
            val++;
    } if (val == 0) {
        document.getElementById("btn").disabled = false;
    } else {
        document.getElementById("btn").disabled = true;
    }
}
document.getElementById("nombre").addEventListener("keyup", habilitar);
document.getElementById("edad").addEventListener("keyup", habilitar);
document.getElementById("generos").addEventListener("keyup", habilitar);
document.getElementById("consultaDates").addEventListener("keyup", habilitar);
document.getElementById("consultas").addEventListener("keyup", habilitar);
document.getElementById("tarjetas").addEventListener("keyup", habilitar);
document.getElementById("cardNumber").addEventListener("keyup", habilitar);
document.getElementById("btn").addEventListener("click", () => {
    console.log("se llenaron los input");
});
*/