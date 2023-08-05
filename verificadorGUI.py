from tkinter import *
import tkinter.messagebox
import apiBusacar
from PIL import Image , ImageTk
ventana=Tk()
ventana.title('Operaciones Aritmeticas')
ventana['bg']='#456789'
ventana.geometry('500x500')

def llamarDatos():
    try:
        label_resultado["text"]="Resultado\n"+entrya.get()
        codigo = entrya.get()
        resultado = apiBusacar.buscarProducto(codigo)

        if resultado is None:
            label_resultado.config(text="Producto no encontrado")

        else
            #Mostrar Imagen
            nombre_producto = resultado [1]
            nombre_producto = resultado [2]
            image = Image.open({resultado[3]})
            image = image.resize((500, 500))
            test = ImageTk.PhotoImage(image)
            labela=Label(ventana,image=test)
            lbl_image = Label(ventana, image=test)
            label_resultado(Text="nombre: {nombre_producto} \nPrecio: ${precio_producto}" )


    except:
        tkinter.messagebox.showerror(message="A Ocurrido Un Error Con Los Datos Ingresados", title="Error")

#labels
label_codigo=Label(ventana,text="Codigo Del Producto",font = "Helvetica 16 bold italic")
label_codigo.place(x=10,y=110)

label_resultado=Label(ventana,text="Producto",font = "Helvetica 16 bold italic")
label_resultado.place(x=200,y=200)

#Entrys
entrya=Entry(ventana,font = "Helvetica 16 bold italic")
entrya.insert(END,"001")
entrya.place(x=265,y=110)
#buttons
buttonbusca=Button(ventana, text="Buscar",font = "Helvetica 16 bold italic",command= llamarDatos : ())
buttonbusca.place(x=210,y=150)

lbl_image = Label(ventana)
lbl_image.pack(pady=20)
ventana.mainloop()