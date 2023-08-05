import apiBusacar
codigo = "";
while codigo != "salir":
    codigo = input("Escriba el codigo(id) del Producto a Buscar Codigo= ")
    if codigo =="salir": break
    respuesta = apiBusacar.buscarProducto(codigo)
    if respuesta == 0:
        print("No Se Pudo Realizar La Busqueda, No existe el Producto Con el Codigo "+ codigo)
    elif respuesta == -1:
        print("No Hubo Conexion.")
    else: print("Producto: "+str(respuesta[1])+"\nEl Precio Es: "+ str(respuesta[2])+ "\nCodigo: "+str(respuesta[0]))
 
print ("Gracias Por Usar El sistema")
