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

def simular_compra():
    """
    Permite al cliente simular una compra seleccionando productos hasta que su presupuesto se agote.
    """
    # Cargar productos
    productos = cargar_csv('productos.csv')
    
    if not productos:
        print("Error: No se pudieron cargar los productos.")
        return

    # Mostrar productos disponibles
    print("Productos disponibles:")
    for idx, producto in enumerate(productos, 1):
        print(f"{idx}. {producto['nombre']} - {producto['categoria']} - Precio: ${producto['precio']}")
    
    # Solicitar presupuesto
    try:
        presupuesto = float(input("\nIngresa tu presupuesto disponible: $"))
    except ValueError:
        print("Error: Por favor, ingresa un valor numérico para el presupuesto.")
        return
    
    # Variables para realizar la compra
    productos_comprados = []
    total_compra = 0

    while True:
        # Solicitar al cliente que elija un producto
        try:
            eleccion = int(input("\nSelecciona el número del producto que deseas comprar (0 para terminar): "))
            if eleccion == 0:
                break
            if eleccion < 1 or eleccion > len(productos):
                print("Error: Producto no válido. Intenta nuevamente.")
                continue
            cantidad = int(input(f"¿Cuántas unidades de '{productos[eleccion - 1]['nombre']}' deseas comprar? "))
        except ValueError:
            print("Error: Por favor ingresa un número válido.")
            continue

        # Validar si el cliente tiene suficiente presupuesto
        producto = productos[eleccion - 1]
        precio_total = cantidad * float(producto['precio'])
        
        if total_compra + precio_total > presupuesto:
            print("Error: No tienes suficiente presupuesto para esta compra.")
        else:
            # Agregar el producto a la lista de productos comprados
            productos_comprados.append({
                'producto': producto['nombre'],
                'cantidad': cantidad,
                'precio_total': precio_total
            })
            total_compra += precio_total
            print(f"Has agregado {cantidad} unidades de '{producto['nombre']}' a tu carrito.")

    # Mostrar el resumen de la compra
    print("\nResumen de tu compra:")
    for item in productos_comprados:
        print(f"{item['cantidad']} x {item['producto']} - ${item['precio_total']:.2f}")
    
    print(f"\nTotal de la compra: ${total_compra:.2f}")
    if total_compra > presupuesto:
        print("¡Has excedido tu presupuesto!")
    else:
        print("¡Compra realizada con éxito!")
