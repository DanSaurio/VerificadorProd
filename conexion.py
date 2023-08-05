import mysql.connector
try:
    conexion = mysql.connector.connect(host='localhost',user='root',password='',database='pos')
    resultado = conexion.cursor()
    nombre = "";
    while nombre != "salir":
        nombre = input("Escriba el nombre del Producto a Buscar: ")
        if nombre =="salir":
            break
        resultado.execute("SELECT * FROM empleados WHERE nombre='"  + nombre+"'")
        registro = resultado.fetchone()
        if registro:
            print("Mail: " + str (registro[4]) + "\nPassword: "+str(registro[5]))
        else: print("No Se Pudo Realizar La Busqueda, Usuario No Encontrado")
except:
    print("No se pude Realizar la Conexion") 
print ("Gracias Por Usar El sistema")
