//const URL = "http://127.0.0.1:5000/"
const URL = "https://grupo2com23532.pythonanywhere.com/"

// Realizamos la solicitud GET al servidor para obtener todos los productos
fetch(URL + 'clientes')
    .then(function (response) {
        if (response.ok) {
            return response.json();

        } else {
            // Si hubo un error, lanzar explícitamente una excepción
            // para ser "catcheada" más adelante
            throw new Error('Error al obtener los datos del cliente.');
        }
    })
    .then(function (data) {
        let tablaClientes = document.getElementById('tablaClientes');
        // Iteramos sobre los productos y agregamos filas a la tabla
        for (let cliente of data) {
            let fila = document.createElement('tr');
            fila.innerHTML = '<td>' + cliente.codigo + '</td>' +
                '<td>' + cliente.nombre + '</td>' +
                '<td>' + cliente.apellido + '</td>' +
                '<td align="right">' + cliente.dni + '</td>' +
                // Mostrar miniatura de la imagen
                //'<td><img src=static/img/' + cliente.imagen_url + ' alt="Imagen del cliente" style="width: 100px;"></td>' +
                '<td><img src=https://www.pythonanywhere.com/user/grupo2com23532/files/home/grupo2com23532/mysite/static/img/' + cliente.imagen_url +' alt="Imagen del cliente" style="width: 100px;"></td>' +
                '<td align="right">' + cliente.deuda + '</td>' +
                '<td align="right">' + cliente.tipo_impuesto + '</td>';
            //Una vez que se crea la fila con el contenido del producto, se agrega a la tabla utilizando el método appendChild del elemento tablaProductos.

            tablaClientes.appendChild(fila);
        }
    })
    .catch(function (error) {
        // En caso de error
        alert('Error al agregar el cliente.');
        console.error('Error:', error);
    })