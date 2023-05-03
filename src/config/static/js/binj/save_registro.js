
function crearcuenta(event) {
    event.preventDefault();
    const name = document.getElementById('name');
    const username = document.getElementById('username');
    const email = document.getElementById('email');
    const password = document.getElementById('password');
   

    axios.post('guardaregistro', {
        Name: name.value,
        Username: username.value,
        Email: email.value,
        Password: password.value,
        

    }, {
        headers: {
        'Content-Type': 'multipart/form-data'

        }
    }
    ).then((res) => {
        console.log(res.data)
        alert("registro existoso")
        window.location.href = "/fronted/indexprincipal";
    })
    .catch((error) => {
        console.error(error)
    })

    
}