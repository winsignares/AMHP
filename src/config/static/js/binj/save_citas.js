function addprocita() {
    const nombre = document.getElementById('nombre');
    const edad = document.getElementById('edad');
    const generos= document.getElementById('generos');
    const consultaDates = document.getElementById('consultaDates');
    const consultas = document.getElementById('consultas');
    const tarjetas= document.getElementById('tarjetas');
    const cardNumber = document.getElementById('cardNumber');
    const problemas = document.getElementById('problemas');

    console.log(nombre, edad, cardNumber);

    try {
        axios.post('guardarcita', {
            Nombre_completo: nombre.value,
            Edad: edad.value,
            genero: generos.value,
            fecha: consultaDates.value,
            consulta: consultas.value,
            tarje_tade_credito: tarjetas.value,
            Num_tarjeta: cardNumber.value,
            problema: problemas.value
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
