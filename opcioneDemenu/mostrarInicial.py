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

def mostrar_resumen_inicial():
    """
    Muestra un resumen inicial con información general y el producto más vendido.
    """
    # Cargar datos desde los archivos CSV
    productos = cargar_csv('productos.csv')
    ventas = cargar_csv('ventas.csv')
    clientes = cargar_csv('clientes.csv')
    
    if not productos or not ventas or not clientes:
        print("Error: Uno o más archivos no se pudieron cargar correctamente.")
        return
    
    # Número total de registros
    print("Resumen Inicial del Sistema de Ventas:")
    print(f"- Total de productos: {len(productos)}")
    print(f"- Total de ventas: {len(ventas)}")
    print(f"- Total de clientes: {len(clientes)}")
    
    # Calcular el producto con mayor cantidad de ventas
    ventas_por_producto = {}
    for venta in ventas:
        try:
            id_producto = venta['id_producto']
            cantidad = int(venta['cantidad'])
            ventas_por_producto[id_producto] = ventas_por_producto.get(id_producto, 0) + cantidad
        except (ValueError, KeyError):
            print(f"Advertencia: Datos inválidos en venta: {venta}")

    if not ventas_por_producto:
        print("No hay ventas válidas para analizar.")
        return
    
    # Identificar el producto más vendido
    producto_mas_vendido_id = max(ventas_por_producto, key=ventas_por_producto.get)
    cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido_id]
    
    # Buscar el producto más vendido
    producto_mas_vendido = next((p for p in productos if p['id_producto'] == producto_mas_vendido_id), None)
    
    if producto_mas_vendido:
        print("\nProducto más vendido:")
        print(f"- Nombre: {producto_mas_vendido['nombre']}")
        print(f"- Categoría: {producto_mas_vendido['categoria']}")
        print(f"- Cantidad vendida: {cantidad_mas_vendida}")
    else:
        print(f"Advertencia: No se encontró información del producto con ID {producto_mas_vendido_id}.")
