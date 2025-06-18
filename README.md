#  Segundo parcial Programacion de Computadoras 2025imulador de Biblioteca 

**Autor:** Juan Camilo Rodriguez Moreno  

---

## Descripción

Este proyecto implementa un **sistema de gestión básica para libros de una biblioteca**.  
Está desarrollado en Python utilizando la biblioteca gráfica `tkinter` y almacenamiento de datos en archivos `.json`

La aplicación permite:
- Registrar nuevos libros con categoría.
- Consultar libros por título o autor (búsqueda rápida).
- Ver la lista de libros y su disponibilidad.
- Marcar libros como prestado o devuelto.
- **Persistencia automática**: Los libros quedan guardados en disco.

Todo esto desde una **interfaz gráfica SENCILLA**.
Se ejecuta en una unica ventana que va cambiando los elementos visuales segun el menu seleccionado gracias a una funcion de limpiar ventana.

## Cuenta con las liguentes variables globales 

**libros**: lista que almacena los libros (cada libro es un diccionario).

**CATEGORIAS**: lista de las categorías permitidas.

## Funciones de serialización

Guardan y cargan los datos en archivos .json automáticamente.

## Funciones lógicas

Registrar, buscar y alternar estado de libros.

## Funciones de interfaz gráfica

Todo lo que se ve: menús, formularios, listas, búsqueda y préstamos.



---

## 🧰 Requisitos y Paquetes Usados

# Paquetes estándar de Python

- **tkinter**  
  Incluido en la instalación estándar de Python.  
  Permite crear ventanas, botones, cuadros de texto, menús, etc.

- **json**  
  Incluido en Python.  
  Sirve para guardar/cargar información estructurada (en este caso, los libros).

- **tkinter.ttk**  
  Incluido en Python.  
  Permite usar widgets mejorados (por ejemplo, menús desplegables).

- **tkinter.messagebox**  
  Incluido en Python.  
  Se usa para mostrar mensajes de éxito o advertencia al usuario.

---

# 🚀 ¿Cómo ejecutar?

1. Descarga el archivo `GUI_busqueda_de_libros.py`.
2. Abre una terminal/CMD en la carpeta del archivo.
3. Ejecuta: Al registrar un libro se crea el archivo libros.json 
