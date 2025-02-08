# Se importan los módulos esenciales
from modulos import productos, materiales, inventario, calculos
import tkinter as tk

# ventana principal
ventana = tk.Tk()
ventana.title("Control de inventario")

# Bienvenida
bienvenida_label = tk.Label(
    ventana, text="Bienvenidos al Control de Inventario", font=('Consolas', 18))
bienvenida_label.pack()

# Definición de los Botones principales del menú
boton_materiales = tk.Button(ventana, text="Materiales", font=(
    'Consolas'), command=materiales.modulo_materiales)
boton_productos = tk.Button(ventana, text="Productos", font=(
    'Consolas'), command=productos.modulo_productos)
boton_calcular = tk.Button(ventana, text="Calcular", font=(
    'Consolas'), command=calculos.modulo_calculos)
boton_inventario = tk.Button(ventana, text="Ver Inventario", font=(
    'Consolas'), command=inventario.modulo_inventario)

# Botones menu Materiales

# Botones menu Productos

# Botones menu Calcular

# Botones menu Inventario

boton_materiales.pack()
boton_productos.pack()
boton_calcular.pack()
boton_inventario.pack()


ventana.mainloop()
