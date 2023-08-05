from tkinter import *
from PIL import Image , ImageTk

ventana = Tk()
ventana.title("imagen")
ventana.geometry('500x500')
#Creamos Variable para la imagen
try:
    image = Image.open("./Img/huevos.jpg")
    image = image.resize((500, 500))
    test = ImageTk.PhotoImage(image)
    labela=Label(ventana,image=test)
except:
    labela = Label(ventana,Text='imagen no encontrada')

labela.place(x=10,y=0)

ventana.mainloop()
