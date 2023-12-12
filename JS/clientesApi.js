let contenido = document.querySelector('#contenido')

function traerUsuario() {
       fetch('https://randomuser.me/api')
        .then(res => res.json())
        .then(res => {
          console.log(res)
          console.log(res.results[0].email)
          contenido.innerHTML = `
                <img src="${res.results[0].picture.large}" width="100px" class="img-fluid rounded-circle">
                 <p>Nombre: ${res.results[0].name.first}</p>
                 <p>País: ${res.results[0].location.country}</p>
                 `
         })
        .catch(error => console.log("Ocurrió un error", error)) // si hay un error será atrapado por catch
   }
        // const random = Math.floor(Math.random()*(5-0))+0
        // console.log(random)
        // fetch('https://grupo2com23532.pythonanywhere.com/clientes')
        //     .then(res => res.json())
        //     .then(res => {
        //       console.log(res)
        //       console.log(res.clientes[random].codigo)
        //       contenido.innerHTML = `
        //           <img src="${res.clientes[random].imagen_url}" width="100px" class="img-fluid rounded-circle">
        //           <p>Nombre: ${res.clientes[random].nombre}</p>
        //           <p>Apellido: ${res.clientes[random].apellido}</p>
        //           `
        //     })
        //     .catch(error => console.log("Ocurrió un error", error)) // si hay un error será atrapado por catch
        // }

