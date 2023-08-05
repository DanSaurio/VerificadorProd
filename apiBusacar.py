import mysql.connector
def buscarProducto(producto):
    try:
        conexion = mysql.connector.connect(host='localhost',user='root',password='',database='pos')
        resultado = conexion.cursor()
        resultado.execute("SELECT * FROM productos WHERE codigo='"  + producto+"'")
        registro = resultado.fetchone()
        if registro :
            #Se regresa el precio del producto
            #return str (registro[2])
            return registro
        else:
            #Se regresa 0 cuando no se encuentra el producto
            return 0
        
    except:
        #Se regresa -1 cuando hay un error en la conexion
        return -1