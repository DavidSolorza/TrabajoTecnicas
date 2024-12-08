import os
import csv

# Ruta base donde se encuentran los archivos csv
RUTA_BASE = "./archivos"

def cargar_csv(nombre_archivo):
    """
    Lee un archivo CSV y devuelve su contenido como una lista de diccionarios.
    """
    ruta_archivo = os.path.join(RUTA_BASE, nombre_archivo)
    try:
        with open(ruta_archivo, 'r') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            return [fila for fila in lector]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}' en la ruta '{RUTA_BASE}'.")
        return []

def backtracking_productos(productos, presupuesto, indice=0, seleccionados=None, total=0, cantidad_total=0):
    """
    Función de Backtracking para encontrar las mejores combinaciones de productos dentro de un presupuesto.
    """
    if seleccionados is None:
        seleccionados = []

    # Si ya excedimos el presupuesto o hemos probado todos los productos, retornamos
    if total > presupuesto or indice >= len(productos):
        return seleccionados, cantidad_total

    # Caso 1: No seleccionar el producto actual
    mejor_seleccion = backtracking_productos(productos, presupuesto, indice + 1, seleccionados, total, cantidad_total)

    # Caso 2: Seleccionar el producto actual (si no excede el presupuesto)
    producto_actual = productos[indice]
    precio = float(producto_actual['precio'])
    cantidad = int(producto_actual['cantidad'])
    nueva_total = total + precio
    nueva_cantidad_total = cantidad_total + cantidad

    if nueva_total <= presupuesto:
        # Agregamos el producto a la selección y continuamos
        seleccionados.append(producto_actual)  # Asegúrate de que 'producto_actual' sea un diccionario
        seleccionados_temp, cantidad_total_temp = backtracking_productos(
            productos, presupuesto, indice + 1, seleccionados, nueva_total, nueva_cantidad_total
        )
        
        # Si la nueva selección tiene más unidades compradas, la actualizamos
        if cantidad_total_temp > cantidad_total:
            mejor_seleccion = seleccionados_temp
            cantidad_total = cantidad_total_temp

        # Volver atrás para explorar otras opciones
        seleccionados.pop()

    return mejor_seleccion, cantidad_total

def revisar_presupuesto():
    """
    Permite al cliente encontrar las mejores combinaciones de productos dentro de su presupuesto.
    """
    # Cargar productos
    productos = cargar_csv('productos.csv')
    
    if not productos:
        print("Error: No se pudieron cargar los productos.")
        return

    # Solicitar presupuesto
    try:
        presupuesto = float(input("\nIngresa tu presupuesto disponible: $"))
    except ValueError:
        print("Error: Por favor, ingresa un valor numérico para el presupuesto.")
        return

    # Ejecutar el algoritmo de Backtracking
    seleccionados, cantidad_total = backtracking_productos(productos, presupuesto)

    # Mostrar el resultado
    if seleccionados:
        print("\nProductos seleccionados:")
        for producto in seleccionados:
            print(f"{producto['nombre']} - {producto['categoria']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}")
        print(f"\nTotal de unidades compradas: {cantidad_total}")
    else:
        print("No se encontraron productos que se ajusten a tu presupuesto.")


def revisar_presupuesto():
    """
    Permite al cliente encontrar las mejores combinaciones de productos dentro de su presupuesto.
    """
    # Cargar productos
    productos = cargar_csv('productos.csv')
    
    if not productos:
        print("Error: No se pudieron cargar los productos.")
        return

    # Solicitar presupuesto
    try:
        presupuesto = float(input("\nIngresa tu presupuesto disponible: $"))
    except ValueError:
        print("Error: Por favor, ingresa un valor numérico para el presupuesto.")
        return

    # Ejecutar el algoritmo de Backtracking
    seleccionados, cantidad_total = backtracking_productos(productos, presupuesto)

    # Mostrar el resultado
    if seleccionados:
        print("\nProductos seleccionados:")
        for producto in seleccionados:
            print(f"{producto['nombre']} - {producto['categoria']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}")
        print(f"\nTotal de unidades compradas: {cantidad_total}")
    else:
        print("No se encontraron productos que se ajusten a tu presupuesto.")
