# grupo-2
Grupo II Asesoramiento Empresarial Integral

El presente Trabajo Practico, se trata de un ejercicio real. Formalizando a traves de una pagina web los servicios de asesoramiento que prestan un grupo de profesionales, en las Areas de Contabilidad-Impositivo, Servicios Juridicos y Previsionales, y por ultimo, Seguridad e Higiene en el Trabajo y Seguridad Informatica y Mantenimiento de redes.
A efectos del TP, se redujeron las cantidades de hojas .HTML , utilizando una para 2 tipos de asesoramiento, quedando una pagina principal o Index.html, otra de servicios de asesoramiento de Contabilidad-Impositivo.html, Juridico-Previsional.html, Seg-Higiene.html y un formulario de contacto.
Adicionalmente se le agrego un Bot, para enviar mensajes de WhatsApp a un numero cargado.

2. PUBLICO Y OBJETIVOS:

La pagina esta orientada hacia contribuyentes unipersonales como empresas a los cuales se les ofrece los servicios detallados en la misma para lograr que sus actividades, recursos (tanto humanos como economicos),  se potencien y logren brindar un servicio de excelencia para sus clientes.

3. ESTRUCTURA DEL SITIO:

La estructura basica del sitio es la siguiente:

Etiqueta <!DOCTYPE html>:
Indica la version de HTML que se esta utilizando (en este caso, HTML5).
<html lang="es">:
Define el comienzo del documento HTML y especifica que el idioma utilizado es castellano ("es").
Encabezado (<head>):
Contiene metadatos y enlaces a recursos externos. Algunos elementos importantes son:
meta charset="UTF-8": Define la codificacion de caracteres como UTF-8.
meta name="viewport": Define como se debe ajustar la escala en dispositivos moviles.
meta http-equiv="X-UA-Compatible": Indica la compatibilidad con Internet Explorer.
link rel="icon": Especifica el icono que se mostrara en la pestana del navegador.
meta name="author": Indica los autores del sitio.
link rel="stylesheet": Enlaza la hoja de estilos externa (estilos.css).
script defer src="JS/app.js": Enlaza el archivo de script JavaScript externo (app.js).
title: Establece el titulo de la pagina.
Cuerpo (<body>):
Contiene el contenido visible de la pagina. Algunas secciones notables son:
<div class="contenedor">: Envuelve todo el contenido de la pagina.
<header id="idheader" class="header">: Seccion para el encabezado.
<div class="slider-frame">: Contiene un carrusel de imagenes.
<div class="contenido2">: Seccion que contiene tres bloques con imagenes y descripciones.
<div class="widget-1">: Contiene un bot�n que activa la funcion traerUsuario() y muestra el contenido en el elemento con el id "contenido".
<footer id="idfooter" class="pie-pagina">: Seccion para el pie de pagina.
Scripts JavaScript:
Al final del cuerpo, se enlazan varios archivos JavaScript (JS/clientesApi.js, JS/headerFooter.js, JS/script.js, JS/script2.js).
Seccion flotante de WhatsApp:
Agrega un boton de WhatsApp flotante y una ventana emergente para interactuar con los visitantes.


La estructura de navegacion se realiza por diferentes enlaces que nos llevan a otras secciones de la pagina: Nosotros, Asesoramiento Contable, Asesoramiento Juridico, Seguridad e higiene y Contacto que ofrece la posibilidad de validaciones varias de los casilleros.

4. DISENO Y ESTILO
Para la realizacion del proyecto, se utilizaron en CSS diferentes estilos:
Reset de Estilos (* { margin: 0; padding: 0; }):
Establece margenes y rellenos a cero para todos los elementos, proporcionando un reseteo basico de estilos.
Estilos Generales (body { color: #5c5c5c; font-family: ...; font-size: 14px; }):
Define estilos generales para el cuerpo de la pagina, como el color de texto, la fuente y el tamano de fuente.
Estilos del Contenedor Principal (.contenedor { ... }):
Establece la estructura del contenedor principal utilizando la cuadricula (grid) con areas para el encabezado, el carrusel, el contenido, el widget y el pie de pagina. Estilos de la Barra de Navegacion (.header { ... }, .menu li a:hover { ... }, .submenu { ... }):
Define estilos para la barra de navegacion, incluyendo el color de fondo, la alineacion y la apariencia de los elementos del menu y submenu.
Estilos de Secciones Especificas (#contenido2, #contenido3):
Establece estilos especificos para las secciones de contenido2 y contenido3, como colores de fondo y disposicion de elementos.
Estilos del Widget con API (.widget-1 { ... }):
Define estilos para el widget que muestra informacion de la API, incluyendo colores de fondo, alineacion y formato del texto.
Estilos del Pie de Pagina (.pie-pagina { ... }):
Establece el estilo del pie de pagina, incluyendo colores de fondo y estilos para los elementos dentro del pie de pagina.
Estilos del Carrusel (.slider-frame { ... }, @keyframes slide { ... }):
Define estilos para el carrusel de imagenes, incluyendo el diseno, la animacion y los tamanos de imagen.
Estilos Responsivos (@media screen and (max-width: 768px) { ... }):
Ajusta el diseno para pantallas mas pequenas, cambiando el tamano y la disposicion de algunos elementos para mejorar la experiencia en dispositivos moviles.
Estilos para el Formulario (.contenedorFormulario { ... }, .formulario { ... }):
Establece estilos para el formulario, incluyendo diseno, margenes y colores de fondo.
Estilos Especificos para Imagenes (.contenedor img { ... }):
Define estilos para las imagenes dentro del contenedor, especificando que ocupen el 100% del ancho y alto, y que se ajusten segun sea necesario.
Estos son solo algunos de los estilos clave utilizados en la pagina web. Cada bloque de estilos se aplica a elementos especificos en la pagina para lograr un diseno y apariencia particulares.


5. PRINCIPIO DEL FORMULARIO
Tambien se aplico Java Script para validar el formulario de contacto y se detalla una descripcion de sus funciones principales:
Expresiones Regulares (expresiones):
Se definen expresiones regulares para validar el formato de correo electronico (correo) y el formato de numero de telofono (telefono).
Evento de Envio del Formulario (fvalida.addEventListener('submit', e => { ... }):
Cancela el envio estandar del formulario cuando se intenta enviar, utilizando e.preventDefault(). Esto permite realizar validaciones personalizadas antes de enviar los datos.
Funcion de Validacion Principal (validarEnviar()):
Realiza diversas validaciones en los campos del formulario antes de permitir su envio.
Validacion de Nombre y Apellido:
Asegura que se haya ingresado un nombre y un apellido.
Validacion de Correo Electronico:
Asegura que se haya ingresado un correo electronico y valida su formato utilizando la expresion regular definida.
Validacion de Telefono:
Asegura que se haya ingresado un numero de telefono y valida su formato utilizando la expresion regular definida.
Validacion de Edad:
Asegura que se haya ingresado un numero entero mayor de 18 anos.
Validacion de Residencia:
Asegura que se haya seleccionado una opcion de residencia en un menu desplegable.
Validacion de Opciones de Consulta:
Asegura que al menos una opcion de consulta este seleccionada.
Validacion de Opcion unica:
Asegura que solo se haya seleccionado una opcion de un conjunto de opciones.
Validacion de Aceptacion de Terminos:
Asegura que se haya marcado la casilla de aceptacion de terminos y condiciones.
Envio del Formulario:
Si todas las validaciones son exitosas, se muestra un mensaje de agradecimiento y se envia el formulario.
Funciones Auxiliares (validarEntero(), esMail(), esTelefono()):
validarEntero(valor): Convierte el valor a entero si es posible y devuelve la cadena vacia si no es un numero.
esMail(dato): Utiliza la expresion regular para verificar si el dato proporcionado es un correo electronico valido.
esTelefono(dato): Utiliza la expresion regular para verificar si el dato proporcionado es un numero de telefono valido.
En resumen, este codigo JavaScript se encarga de validar diferentes campos de un formulario antes de permitir su envio, asegurando que los datos ingresados cumplan con ciertos criterios especificados mediante expresiones regulares y logica de validacion.
Principio del formulario

Tambien utilizamos Java Script para la creacion de un boton de WatsApp:
Tiene la funcion de crear un boton de WhatsApp en la pagina web y gestionar la apertura de un popup de WhatsApp al hacer clic en dicho boton. Aqui hay una descripcion concisa de su utilidad:
Boton de WhatsApp:
Genera un boton de WhatsApp que se puede abrir al hacer clic en el.
Popup de WhatsApp:
Muestra un popup (ventana emergente) de WhatsApp al hacer clic en el boton correspondiente.
Permite cerrar el popup al hacer clic en un boton de cierre dentro de el.

Animacion del Popup:
Aplica una animacion de fade-in al abrir el popup para mejorar la experiencia del usuario.
Envio de Mensaje a WhatsApp:
Permite al usuario escribir un mensaje en el popup de WhatsApp.
Al hacer clic en el boton de enviar en el popup, el script construye un enlace de WhatsApp con el mensaje proporcionado.
Abre una nueva ventana del navegador con el enlace de WhatsApp, lo que permite al usuario iniciar una conversacion de WhatsApp con el numero y el mensaje predefinidos.
Temporizador de Aparicion Automatica:
Configura un temporizador para que el popup de WhatsApp aparezca automaticamente despuus de 3 segundos de carga de la pagina.
En resumen, este script proporciona una forma interactiva y atractiva para que los usuarios se comuniquen con el propietario del sitio web a traves de WhatsApp. El popup facilita el inicio de una conversacion en WhatsApp con un mensaje predefinido y se presenta de manera automatica despues de un breve periodo de tiempo.

Tambien se utilizo otro fragmento en Java Script:

Este fragmento de JavaScript utiliza el objeto fetch para realizar una solicitud a la API de "randomuser.me". La funcion traerUsuario() se llama para obtener informacion de usuario aleatoria y actualizar el contenido de un elemento HTML con esa informacion. Aqui hay una explicacion mas detallada:
let contenido = document.querySelector('#contenido'):
Selecciona un elemento HTML con el ID contenido y lo almacena en la variable contenido.
function traerUsuario() { ... }:
Define una funcion llamada traerUsuario que realizara la solicitud a la API y actualizara el contenido HTML.
fetch('https://randomuser.me/api'):
Utiliza la funcion fetch para realizar una solicitud a la URL proporcionada, que es la API de "randomuser.me". Esta API proporciona datos de usuarios aleatorios.
.then(res => res.json()):
Encadena una funcion .then() que convierte la respuesta de la solicitud a JSON. La respuesta es procesada como un objeto JSON.
.then(res => { ... }):
Encadena otra funcion .then() que maneja los datos obtenidos de la respuesta JSON.
Imprime la respuesta en la consola para propositos de depuracion.
Actualiza el contenido del elemento HTML seleccionado (#contenido) con informacion especifica del usuario obtenida de la respuesta.
.catch(error => console.log("Ocurrio un error", error)):
Encadena una funcion .catch() que maneja cualquier error que pueda ocurrir durante la solicitud y lo imprime en la consola.
En resumen, este codigo utiliza fetch para obtener datos de usuario aleatorios de una API, procesa la respuesta JSON y actualiza dinamicamente el contenido de un elemento HTML en la pagina con informacion especifica del usuario. Esto es comunmente utilizado para mostrar contenido dinamico o actualizaciones en una pagina web sin tener que recargarla completamente.


6. CONTENIDO Y FUNCIONALIDADES:
El contenido de la pagina esta conformado por una serie de imagenes que apoyan la tematica misma de la actividad de la empresa, tambien cuenta con una seccion de SITIOS DE INTERES que se conforman por una lista de navegacion redireccionada a los mismos.
Al igual que los sitios de interes, tambien en el footer se encuentra una breve descripcion de la actividad de la empresa y el enlace a diferentes redes sociales.
Tambien cuenta con un formulario de contacto y registracion para los clientes o futuros clientes que deseen contactarse con nosotros.

7. RESPONSABILIDADES DEL EQUIPO:
El equipo en su etapa inicial se encontro con desersiones de integrantes, quedando lugares libres, los que luego fueron completados por otros companeros.
El equipo se encuentra conformado por las siguientes personas:
Elvira M. Maggiolo, Maria Eugenia Jacord, Alan Contreras y Marcelo Alejandro Galarza.
En general se trato de un trabajo totalmente en grupo, con mucha comunicacion entre los mismos y aunque algunos por distintos motivos se sumaron mas tarde al proyecto, aportaron muchisimo a la tarea inicial de ELVIRA MAGGIOLO de la conformacion de la pagina inicial en html y CSS, MARIA EUGENIA JACORD Y MARCELO ALEJANDRO GALARZA se ocuparon sobre todo de la maquetacion y de darle un tinte mas profesional a la pagina, y Alan Contreras se ocupo del tema de Formularios y API aplicados al mismo. En suma, fue una tarea en equipo y con el uso de las habilidades blandas brindada por CODO A CODO que sirvio muchisimo para la buena convivencia, respeto y apoyo de todo el exelente grupo que hemos logrado conformar.

EQUIPO2 - COMISION 23532 - 2 CUATRIMESTRE 2023

Informamos mails de los integrantes del grupo por cualquier consulta en particular:

CONTRERAS FLORES, Alan Benito
alancontreras784@gmail.com
JACCOD, Maria Eugenia
eugenia.jaccod@gmail.com
MAGGIOLO, Elvira Maria
asistente.contable.cg@gmail.com
GALARZA, Marcelo Alejandro
galarza.marcelo.alejandro@gmail.com




GRUPO II ASESORAMIENTO INTEGRAL EMPESARIAL