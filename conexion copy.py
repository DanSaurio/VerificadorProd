import mysql.connector
def buscarProducto(producto):
    try:
        conexion = mysql.connector.connect(host='localhost',user='root',password='',database='pos')
        resultado = conexion.cursor()
        resultado.execute("SELECT * FROM productos WHERE nombre='"  + producto+"'")
        registro = resultado.fetchone()
        if registro : return str (registro[2])
        else:
            return 0
        
    except:
        return -1
     
nombre = "";
while nombre != "salir":
    nombre = input("Escriba el nombre del Producto a Buscar: ")
    if nombre =="salir": break
    respuesta = buscarProducto(nombre)
    if respuesta == 0:
        print("No Se Pudo Realizar La Busqueda, No existe el Producto Llamado "+ nombre)
    elif respuesta == -1:
        print("No Hubo Conexion.")
    else: print("El Precio Es: "+ respuesta)
 
print ("Gracias Por Usar El sistema")
