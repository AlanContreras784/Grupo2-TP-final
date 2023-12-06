# Instalar con pip install Flask
from flask import Flask, request, jsonify
#from flask import request
# Instalar con pip install flask-cors
from flask_cors import CORS
# Instalar con pip install mysql-connector-python
import mysql.connector
# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename
# No es necesario instalar, es parte del sistema standard de Python
import os
import time
#--------------------------------------------------------------------

app = Flask(__name__)
CORS(app) # Esto habilitará CORS para todas las rutas

class Gestor_Clientes:
    # Constructor de la clase
    def __init__(self, host, user, password, database):

        # Primero, establecemos una conexión sin especificar la base de datos
        self.conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
        )
        self.cursor = self.conn.cursor()
        
        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err
    
        # Una vez que la base de datos está establecida, creamos la tabla si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                            codigo INT, 
                            nombre VARCHAR(50) NOT NULL, 
                            apellido VARCHAR(50) NOT NULL,
                            dni INT NOT NULL,
                            imagen_url VARCHAR(255), 
                            deuda DECIMAL(10, 2) NOT NULL,  
                            tipo_impuesto VARCHAR(50))''') 
        self.conn.commit()
        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)


#--------------------------------------------------------------------
    def listar_clientes(self):
        self.cursor.execute("SELECT * FROM clientes")
        clientes = self.cursor.fetchall()
        return clientes
 
#--------------------------------------------------------------------
    def consultar_cliente(self, codigo):
        # Consultamos un producto a partir de su código
        self.cursor.execute(f"SELECT * FROM clientes WHERE codigo = {codigo}")
        return self.cursor.fetchone()
#--------------------------------------------------------------------

    def mostrar_cliente(self, codigo):
        # Mostramos los datos de un producto a partir de su código
        cliente = self.consultar_cliente(codigo)
        if cliente:
            print("-" * 40)
            print(f"Código.............: {cliente['codigo']}")
            print(f"Nombre.............: {cliente['nombre']}")
            print(f"Apellido...........: {cliente['apellido']}")
            print(f"DNI................: {cliente['dni']}")
            print(f"Imagen.............: {cliente['imagen_url']}")
            print(f"Deuda..............: {cliente['deuda']}")
            print(f"Tipo de Impuesto...: {cliente['tipo_impuesto']}")
            print("-" * 40)
        else:
            print("Cliente no encontrado.")
#--------------------------------------------------------------------
    def agregar_cliente(self, codigo, nombre, apellido, dni, imagen, deuda, tipo_impuesto):
        # Verificamos si ya existe un producto con el mismo código
        self.cursor.execute(f"SELECT * FROM clientes WHERE codigo = {codigo}")
        cliente_existe = self.cursor.fetchone()
        if cliente_existe:
            return False
        # Si no existe, agregamos el nuevo producto a la tabla
        sql = "INSERT INTO clientes (codigo, nombre,  apellido, dni, imagen_url, deuda, tipo_impuesto) VALUES (%s, %s, %s, %s, %s, %s,%s)"
        valores = (codigo, nombre, apellido, dni, imagen, deuda, tipo_impuesto)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return True
#--------------------------------------------------------------------
    def eliminar_cliente(self, codigo):
        # Eliminamos un producto de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM clientes WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0
 #-------------------------------------------------------------------   
    def modificar_cliente(self, codigo, nuevo_nombre, nuevo_apellido, nuevo_dni,nueva_imagen, nueva_deuda, nuevo_impuesto):
        sql = "UPDATE clientes SET nombre = %s, apellido = %s, dni = %s, imagen_url = %s, deuda = %s, tipo_impuesto = %s WHERE codigo = %s"
        valores = (nuevo_nombre, nuevo_apellido, nuevo_dni, nueva_imagen, nueva_deuda, nuevo_impuesto, codigo)
        self.cursor.execute(sql,valores)
        self.conn.commit()
        return self.cursor.rowcount > 0  
        
#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------
# Crear una instancia de la clase Catalogo
#gestor_cliente = Gestor_Clientes(host='localhost', user='root', password='', database='miapp')
gestor_cliente = Gestor_Clientes(host='grupo2com23532.mysql.pythonanywhere-services.com', user='grupo2com23532', password='asecon23532', database='grupo2com23532$miapp')

# Carpeta para guardar las imagenes
#ruta_destino = 'static/img/'
ruta_destino = '/home/grupo2com23532/mysite/static/img/'


@app.route("/clientes", methods=["GET"])
def listar_clientes():
    clientes = gestor_cliente.listar_clientes()
    return jsonify(clientes)


@app.route("/clientes/<int:codigo>", methods=["GET"])
def mostrar_cliente(codigo):
    gestor_cliente.mostrar_cliente(codigo)
    cliente = gestor_cliente.consultar_cliente(codigo)
    if cliente:
        return jsonify(cliente)
    else:
        return "Producto no encontrado", 404  

@app.route("/clientes", methods=["POST"])
def agregar_cliente():
# Recojo los datos del form
    codigo = request.form['codigo']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    dni = request.form['dni']
    deuda = request.form['deuda']
    tipo_impuesto = request.form['tipo_impuesto']
    imagen = request.files['imagen']
    nombre_imagen = secure_filename(imagen.filename)

    nombre_base, extension = os.path.splitext(nombre_imagen)
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
    imagen.save(os.path.join(ruta_destino, nombre_imagen))
    
    if gestor_cliente.agregar_cliente(codigo, nombre, apellido, dni, nombre_imagen, deuda, tipo_impuesto):
        return jsonify({"mensaje": "Cliente agregado"}), 201
    else:
        return jsonify({"mensaje": "Cliente ya existe"}), 400 



@app.route("/clientes/<int:codigo>", methods=["DELETE"])
def eliminar_cliente(codigo):
# Primero, obtén la información del producto para encontrar la imagen
    cliente = gestor_cliente.consultar_cliente(codigo)
    if cliente:
        #Eliminar la imagen asociada si existe
        ruta_imagen = os.path.join(ruta_destino, cliente['imagen_url'])
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)

        # Luego, elimina el producto del catálogo
        if gestor_cliente.eliminar_cliente(codigo):
            return jsonify({"mensaje": "Cliente eliminado"}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar el cliente"}), 500
    else:
        return jsonify({"mensaje": "Cliente no encontrado"}), 404


@app.route("/clientes/<int:codigo>", methods=["PUT"])
def modificar_cliente(codigo):
    # Recojo los datos del form
    nuevo_nombre = request.form.get("nombre")
    nuevo_apellido = request.form.get("apellido")
    nuevo_dni = request.form.get("dni")
    nueva_deuda = request.form.get("deuda")
    nuevo_impuesto = request.form.get("tipo_impuesto")

    # Procesamiento de la imagen
    imagen = request.files['imagen']
    nombre_imagen = secure_filename(imagen.filename)
    nombre_base, extension = os.path.splitext(nombre_imagen)
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
    imagen.save(os.path.join(ruta_destino, nombre_imagen))  

    # Actualización del producto
    if gestor_cliente.modificar_cliente(codigo, nuevo_nombre, nuevo_apellido, nuevo_dni, nombre_imagen, nueva_deuda, nuevo_impuesto):
        return jsonify({"mensaje": "Cliente modificado"}), 200
    else:
        return jsonify({"mensaje": "Cliente no encontrado"}), 404




if __name__ == "__main__":
    app.run(debug=True)