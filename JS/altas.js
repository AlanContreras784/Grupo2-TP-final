//const URL = "http://127.0.0.1:5000/"
const URL = "https://grupo2com23532.pythonanywhere.com/"

// Capturamos el evento de envío del formulario
document.getElementById('formulario').addEventListener('submit', function (event) {
    event.preventDefault(); // Evitamos que se envie el form
    var formData = new FormData();
    formData.append('codigo', document.getElementById('codigo').value);
    formData.append('nombre', document.getElementById('nombre').value);
    formData.append('apellido', document.getElementById('apellido').value);
    formData.append('dni', document.getElementById('dni').value);
    formData.append('deuda', document.getElementById('deuda').value);
    formData.append('tipo_impuesto', document.getElementById('tipo_impuesto').value);
    // Realizamos la solicitud POST al servidor
    fetch(URL + 'clientes', {
        method: 'POST',
        body: formData // Aquí enviamos formData en lugar de JSON
    })

    //Después de realizar la solicitud POST, se utiliza el método then() para manejar la respuesta del servidor.
    .then(function (response) {
        if (response.ok) {
                return response.json();
        } else {
            // Si hubo un error, lanzar explícitamente una excepción
            // para ser "catcheada" más adelante
            throw new Error('Error al agregar el cliente.');
        }
    })

        // Respuesta OK
    .then(function () {
        // En caso de éxito
        alert('Cliente agregado correctamente.');
    })
    .catch(function (error) {
        // En caso de error
        alert('Error al agregar el cliente.');
        console.error('Error:', error);
    })
    .finally(function () {
        // Limpiar el formulario en ambos casos (éxito o error)
        document.getElementById('codigo').value = "";
        document.getElementById('nombre').value = "";
        document.getElementById('apellido').value = "";
        document.getElementById('dni').value = "";
        document.getElementById('deuda').value = "";
        document.getElementById('tipo_impuesto').value = "";
    });
})        