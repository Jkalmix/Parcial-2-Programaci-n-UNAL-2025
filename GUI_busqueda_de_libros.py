import tkinter as tk  # Crear interfaces gráficas en Python.
from tkinter import messagebox, ttk  # messagebox: para mostrar cuadros de diálogo. ttk: widgets mejorados 
from PIL import Image, ImageTk  # Ppara trabajar con imágenes. 
import json  # Para trabajar con datos en formato JSON (lectura y escritura).

#VARIABLES GLOBALES
libros = []    # guardar libros registrados 
CATEGORIAS = ["Ciencia", "Literatura", "Ingeniería"]


## FUNCIONES DE SEREIALIZACION EN .JSON ##

# definir una funcion para guardad los datos en .JSON
def guardar_datos():
    """
    Guarda la lista de libros en un archivo JSON llamado 'libros.json'.
    """
    # Abre (o crea) el archivo 'libros.json' en modo escritura  (w) con codificación UTF-8
    with open("libros.json", "w", encoding="utf-8") as f:
        # Escribe la lista 'libros' en formato JSON, con indentación de 4 para que este ordenado 
        json.dump(libros, f, indent=4, ensure_ascii=False)

# definir una funcion para traer o cargar los datos del .JSON
def cargar_datos():
    """
    Carga los datos de libros desde el archivo JSON si existe.
    Si el archivo no existe o está vacío, inicializa la lista como vacía.
    """
    global libros  # Modificar la variable global 'libros'

    try:
        # Abre el archivo 'libros.json' en modo lectura (r) con codificación UTF-8
        with open("libros.json", "r", encoding="utf-8") as f:
            # Lee todo el contenido del archivo y convierte en strip
            contenido = f.read().strip()

            # Si el archivo no está vacío, JSON a lista de Python y reemplaza el contenido de la variable global 'libros'
            # Si está vacío, deja 'libros' como una lista vacía
            libros[:] = json.loads(contenido) if contenido else []

    # Captura dos posibles errores:
    # - FileNotFoundError: si el archivo no existe
    # - JSONDecodeError: si el contenido no es un JSON válido
    except (FileNotFoundError, json.JSONDecodeError):
        libros[:] = []  # Inicializa 'libros' como una lista vacía



# FUNCIONES LÓGICAS PARA GUARDAR O BUSCAR LIBROS  ##

# crear funcion para registrar un libro 
def registrar_libro(titulo, autor, categoria):
    """
    Registra un nuevo libro en la lista y guarda los cambios en el archivo .JSON
    """
    # Crea un diccionario con los datos del libro y lo marca como disponible
    libro = {
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "disponible": True
    }

    # Agrega el nuevo libro a la lista global de libros
    libros.append(libro)

    # Guarda los datos actualizados en el archivo JSON
    guardar_datos()


# funcion para buscar libros 
def buscar_libros(valor):
    """
    Devuelve una lista de libros cuyo valor coincida con lo que se busca en la caja de texto (sin distinguir mayúsculas).
    """
    # Convierte el término de búsqueda a minúsculas para comparación insensible a mayúsculas
    valor = valor.lower()

    # Devuelve una nueva lista de libros que contienen en el título o en el autor que se busco en la caja de texto
    return [
        libro for libro in libros
        if valor in libro["titulo"].lower() or valor in libro["autor"].lower()
    ]

# Función para alternar disponibilidad de un libro
def alternar_estado_libro(indice):
    """
    cambia el estado de disponibilidad de un libro
    """
    libros[indice]["disponible"] = not libros[indice]["disponible"]  # mira el campo de disponibilidad e invirte el valor 
    # Guarda los cambios en el archivo JSON
    guardar_datos()

## Interface grafica ##
# Crea la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Simulador de Biblioteca Por Juan Camilo Rodriguez Moreno")
ventana_principal.geometry("600x400")

# Costruyo una función que me limpie la ventana principal cada vez que quiera mostrar otra cosa em la ventana principal
def limpiar_ventana():
    """
    Elimina todos los elementos visibles para cambiar de pantalla.
    """
    for widget in ventana_principal.winfo_children(): # esto me da una lista con los una widgets hijos como botones etiquetas, cuadros de texto, etc
        widget.destroy() # Esto elimina cada widget hijo de la ventana principal#

# Cras interface grafica
# 
# Crear el menu principal
#   creo una funcion que empiece limpiendo cuaquier ventana y luego me meustre nuevos elementos
def mostrar_menu_principal():
    """
    Muestra el menú principal con botones:
    - Registrar libros
    - Buscar libros
    - Ver la lista de libros
    - Gestionar préstamos
    - Salir de la aplicación
    """
    limpiar_ventana()  # Invoca la funcion limpiar_ventana

    # Título del menú en una etiqueta con fuente Arial, tamaño 16, en negrilla 
    # .pack() es para poner el widget en la ventana.
    tk.Label(
        ventana_principal,
        text="Biblioteca Universitaria Por Juan Camilo Rodriguez Moreno",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # Botones del menú principal
    tk.Button(ventana_principal, text="Registrar Libro", width=30, command=mostrar_formulario_libro).pack(pady=5) # va ala funcion de mostrar_formulario
    tk.Button(ventana_principal, text="Buscar Libro", width=30, command=mostrar_busqueda_libros).pack(pady=5) # va a la funcion Mostrar busqueda libros
    tk.Button(ventana_principal, text="Ver Todos los Libros", width=30, command=mostrar_lista_libros).pack(pady=5) # Mostrar lista de libros
    tk.Button(ventana_principal, text="Prestar / Devolver Libro", width=30, command=mostrar_gestion_prestamos).pack(pady=5) # Mostrar gestion de prestamos
    tk.Button(ventana_principal, text="Salir", width=30, command=ventana_principal.quit).pack(pady=20) # para salir
#defino una funcion para mostrar el formulario de los libros 
def mostrar_formulario_libro():
    """
    Muestra un formulario gráfico para registrar un nuevo libro.
    Ingresar:
    - Título del libro
    - Autor
    - Categoría (seleccionable desde una lista desplegable)
    Incluye botones para guardar el libro y volver al menú principal.
    """
    limpiar_ventana()  # Borra los widgets anteriores de la ventana

    # Título del formulario
    tk.Label(ventana_principal, text="Registrar Libro", font=("Arial", 14)).pack(pady=10)

    # Campo para ingresar el título
    tk.Label(ventana_principal, text="Título:").pack() 
    entry_titulo = tk.Entry(ventana_principal) # para que ingrese el titulo
    entry_titulo.pack() # para que lo muestre 

    # Campo para ingresar el autor
    tk.Label(ventana_principal, text="Autor:").pack() 
    entry_autor = tk.Entry(ventana_principal) # para ingresar el autor
    entry_autor.pack() # para mostrarl la caja de texto

    # Menú desplegable para elegir categoría
    tk.Label(ventana_principal, text="Categoría:").pack()
    combo_categoria = ttk.Combobox(ventana_principal, values=CATEGORIAS, state="readonly") # para crear una lista desplegable con las categorias 
    combo_categoria.pack()

    #  Función interna para validar y guardar los datos del libro
    def guardar():
        titulo = entry_titulo.get().strip() # consigue el titulo y lo trasforma en strip 
        autor = entry_autor.get().strip() # consigue el nombre del autor y lo trasforma en strip 
        categoria = combo_categoria.get().strip() # consigue la categoria y lo trasforma en strip 

        if titulo and autor and categoria: # revisa que ni tintulo ni autor ni categoria esten vacios 
            registrar_libro(titulo, autor, categoria) # si no estna vacios los guarda cone esta funcion logica 
            messagebox.showinfo("Éxito", "Libro registrado correctamente.") # mensaje de exito al guardar
            mostrar_menu_principal() # regresa al menu principal 
        else:
            messagebox.showwarning("Error", "Por favor completa todos los campos.") # si falta el titulo el autor o la categoria muestra un error 

    # Botones de acción
    tk.Button(ventana_principal, text="Guardar", command=guardar).pack(pady=10) # boton para guardas
    tk.Button(ventana_principal, text="Volver", command=mostrar_menu_principal).pack() # Boton para volvar atras

# Definir una funcion para Mostrar la lista de libros:

def mostrar_lista_libros():
    """
    Muestra la lista completa de libros registrados en el sistema,
    indicando si están disponibles o prestados.
    """
    limpiar_ventana() # Borra los widgets anteriores de la ventana

    # Título de la pantalla
    tk.Label(ventana_principal, text="Libros Registrados", font=("Arial", 14)).pack(pady=10)

    # Lista visual de libros
    lista = tk.Listbox(ventana_principal, width=60) # dibujo el witget de vista en la ventana principal 
    lista.pack(pady=10)

    # Agrega cada libro a la lista con su estado
    for libro in libros: # busco cada libro en la lista de libros 
        estado = "Disponible" if libro["disponible"] else "Prestado" # variable que almacena el estado disponible o prestado leyenvo el estado del libro 
        texto = f"{libro['titulo']} - {libro['autor']} ({libro['categoria']}) - {estado}" # texto que me muestra el titulo, autor, categoria 
        lista.insert(tk.END, texto) # se va agregando cada libro al final de la lista
         

    # Botón para volver al menú
    tk.Button(ventana_principal, text="Volver", command=mostrar_menu_principal).pack(pady=10)
# funcion para mostrar la interface graficapara la busqueda de libros 

def mostrar_busqueda_libros():
    """
    Permite buscar libros por título o autor
    Muestra los resultados en una lista, indicando si están disponibles o prestados.
    """
    limpiar_ventana() # Limpia la ventana principal

    # Título y campo de búsqueda
    tk.Label(ventana_principal, text="Buscar Libro", font=("Arial", 14)).pack(pady=10)
    tk.Label(ventana_principal, text="Ingrese título o autor:").pack()
    entry_busqueda = tk.Entry(ventana_principal, width=40) # caja de texto para buscar 
    entry_busqueda.pack(pady=5) # unicacion de la caja de texto

    # Lista donde se mostrarán los resultados
    resultado_lista = tk.Listbox(ventana_principal, width=60) # otra ves se usa el witget de lista para mostrar una lista en la ventana
    resultado_lista.pack(pady=10)

    # Función interna para realizar la búsqueda
    def buscar():
        """
        Realiza una búsqueda de libros por título o autor.
        Muestra los resultados en la lista.
        """
        valor = entry_busqueda.get().strip() # Consigue lo que esta en la caja de texto 
        resultado_lista.delete(0, tk.END) # limpia todos los resultados desde el primero hasta el ultimo 
        resultados = buscar_libros(valor) # invoco función definida en la parte de funcioens logicas 
        for libro in resultados: # Determina el estado del libro: "Disponible" o "Prestado"
            estado = "Disponible" if libro["disponible"] else "Prestado"
            texto = f"{libro['titulo']} - {libro['autor']} ({libro['categoria']}) - {estado}" # Crea un texto con la información del libro, bien formateado
            resultado_lista.insert(tk.END, texto) # Inserta el texto en la Listbox, al final
        if resultado_lista.size() == 0:  # Si no se encontró ningún libro, muestra un mensaje en el Listbox
            resultado_lista.insert(tk.END, "No se encontraron resultados.") 

    # Botones para buscar o salir 
    tk.Button(ventana_principal, text="Buscar", command=buscar).pack(pady=5)
    tk.Button(ventana_principal, text="Volver", command=mostrar_menu_principal).pack(pady=10)

def mostrar_gestion_prestamos():
    """
    Muestra todos los libros y permite alternar su estado entre 'prestado' y 'disponible'.

    El usuario debe seleccionar un libro para cambiar su estado.
    """
    limpiar_ventana()

    # Título
    tk.Label(ventana_principal, text="Gestionar Préstamos", font=("Arial", 14)).pack(pady=10)

    # Lista de libros con estado actual
    lista = tk.Listbox(ventana_principal, width=60)
    lista.pack(pady=10)
    for i, libro in enumerate(libros):
        estado = "Disponible" if libro["disponible"] else "Prestado"
        texto = f"{i+1}. {libro['titulo']} - {libro['autor']} ({libro['categoria']}) - {estado}"
        lista.insert(tk.END, texto)

    # Función interna para cambiar el estado de un libro seleccionado
    def alternar():
        seleccion = lista.curselection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Seleccione un libro de la lista.")
            return
        index = seleccion[0]
        alternar_estado_libro(index)
        mostrar_gestion_prestamos()  # Refresca la vista con el nuevo estado

    # Botones de acción
    tk.Button(ventana_principal, text="Cambiar estado (prestado/devuelto)", command=alternar).pack(pady=5)
    tk.Button(ventana_principal, text="Volver", command=mostrar_menu_principal).pack(pady=10)



### INCIAR LA APLICACION 

#muestra la ventana prinipal y carga los datos
mostrar_menu_principal()
cargar_datos()
ventana_principal.mainloop()
