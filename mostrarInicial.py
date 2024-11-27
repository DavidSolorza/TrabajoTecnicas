import os
import csv

# Ruta base donde se encuentran los archivos csv
RUTA_BASE = "./archivos"  

# Cargar los datos desde los archivos CSV que le manda la funcion resumen inicial
def cargar_csv(archivo):
    # Construir la ruta completa del archivo
    ruta_archivo = os.path.join(RUTA_BASE, archivo)
    
    try:
        # Abrir el archivo y leerlo
        with open(ruta_archivo, 'r') as archivo:
            lector = csv.DictReader(archivo)
            return [fila for fila in lector]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}' en la ruta '{RUTA_BASE}'")
        return []

# Mostrar resumen inicial
def mostrar_resumen_inicial():
    # Cargar datos de los archivos usando la funcio cargando csv 
    productos = cargar_csv('productos.csv')
    ventas = cargar_csv('ventas.csv')
    clientes = cargar_csv('clientes.csv')
    
    # Verificar que los datos se hayan cargado correctamente
    if not productos or not ventas or not clientes:
        print("Error: Uno o más archivos no se pudieron cargar correctamente.")
        return
    
    # Número total de registros
    num_productos = len(productos)
    num_ventas = len(ventas)
    num_clientes = len(clientes)
    
    print("Resumen Inicial del Sistema de Ventas:")
    print(f"- Total de productos: {num_productos}")
    print(f"- Total de ventas: {num_ventas}")
    print(f"- Total de clientes: {num_clientes}")
    
    
    
    
# Calcular el producto con mayor cantidad de ventas
    ventas_por_producto = {}
    for venta in ventas:
        id_producto = venta['id_producto']
        cantidad = int(venta['cantidad'])
        if id_producto in ventas_por_producto:
            ventas_por_producto[id_producto] += cantidad
        else:
            ventas_por_producto[id_producto] = cantidad
    
    # Identificar el producto más vendido
    producto_mas_vendido_id = max(ventas_por_producto, key=ventas_por_producto.get)
    cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido_id]
    
    # Obtener información del producto más vendido
    producto_mas_vendido = next(p for p in productos if p['id_producto'] == producto_mas_vendido_id)
    nombre_producto = producto_mas_vendido['nombre']
    categoria_producto = producto_mas_vendido['categoria']
    
    print("\nProducto más vendido:")
    print(f"- Nombre: {nombre_producto}")
    print(f"- Categoría: {categoria_producto}")
    print(f"- Cantidad vendida: {cantidad_mas_vendida}")
