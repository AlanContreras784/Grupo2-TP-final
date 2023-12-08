//const URL = "http://127.0.0.1:5000/"
const URL = "https://grupo2com23532.pythonanywhere.com/"

const app = Vue.createApp({
    data() {
        return {
            codigo: '',
            nombre: '',
            apellido: '',
            dni: '',
            deuda: '',
            tipo_impuesto: '',
            imagen_url: '',
            imagenUrlTemp: null,
            mostrarDatosCliente: false,
        };
    },

    methods: {
        obtenerCliente() {
            fetch(URL + 'clientes/' + this.codigo)
                .then(response => {
                    if (response.ok) {
                        return response.json()
                    } else {
                        //Si la respuesta es un error, lanzamos una excepción para ser "catcheada" más adelante en el catch.
                        throw new Error('Error al obtener los datos del cliente.')

                    }
                })

                .then(data => {
                    this.nombre = data.nombre;
                    this.apellido = data.apellido;
                    this.dni = data.dni;
                    this.deuda = data.deuda;
                    this.tipo_impuesto = data.tipo_impuesto;
                    this.imagen_url = data.imagen_url;
                    this.mostrarDatosCliente = true;
                })
                .catch(error => {
                    console.log(error);
                    alert('Código no encontrado.');
                })
        },
        seleccionarImagen(event) {
            const file = event.target.files[0];
            this.imagenSeleccionada = file;
            this.imagenUrlTemp = URL.createObjectURL(file);
            // Crea una URL temporal para la vista previa
        },
        guardarCambios() {
            const formData = new FormData();
            formData.append('codigo', this.codigo);
            formData.append('nombre', this.nombre);
            formData.append('apellido', this.apellido);
            formData.append('dni', this.dni);
            formData.append('deuda', this.deuda);
            formData.append('tipo_impuesto', this.tipo_impuesto);

            if (this.imagenSeleccionada) {
                formData.append('imagen', this.imagenSeleccionada, this.imagenSeleccionada.name);
            }

            //Utilizamos fetch para realizar una solicitud PUT a la API y guardar los cambios.
            fetch(URL + 'clientes/' + this.codigo, {
                method: 'PUT',
                body: formData,
            })
            .then(response => {
                //Si la respuesta es exitosa, utilizamos response.json() para parsear la respuesta en formato JSON.
                if (response.ok) {
                    return response.json()
                } else {
                    //Si la respuesta es un error, lanzamos una excepción.
                    throw new Error('Error al guardar los cambios del cliente.')
                }
            })
            .then(data => {
                alert('Cliente actualizado correctamente ');
                this.limpiarFormulario();
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al actualizar el cliente.');
            });
        },
        limpiarFormulario() {
            this.codigo = '';
            this.nombre = '';
            this.apellido = '';
            this.dni = '';
            this.deuda = '';
            this.tipo_impuesto = '';
            this.imagen_url = '';
            this.imagenSeleccionada = null;
            this.imagenUrlTemp = null;
            this.mostrarDatosCliente = false;

        }
    }
});

app.mount('#app');