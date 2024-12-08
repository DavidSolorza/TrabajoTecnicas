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

def relacionProductoCliente():
    """
    Encuentra los clientes que han comprado más productos en las categorías seleccionadas usando fuerza bruta.
    """
    # Cargar los datos desde los archivos CSV
    productos = cargar_csv('productos.csv')
    ventas = cargar_csv('ventas.csv')
    clientes = cargar_csv('clientes.csv')

    if not productos or not ventas or not clientes:
        print("Error: No se pudieron cargar los datos necesarios.")
        return

    # Solicitar al usuario que seleccione las categorías de productos
    print("\nCategorias disponibles:")
    categorias = set([producto['categoria'] for producto in productos])  # Obtengo un conjunto único de categorías
    for idx, categoria in enumerate(categorias, 1):
        print(f"{idx}. {categoria}")
    
    seleccionadas = input("\nIngresa las categorías seleccionadas (por ejemplo, 1,2 para seleccionar múltiples): ")
    seleccionadas = [int(i.strip()) - 1 for i in seleccionadas.split(',')]

    categorias_seleccionadas = [list(categorias)[i] for i in seleccionadas]
    print(f"\nCategorías seleccionadas: {categorias_seleccionadas}")
    
    # Crear un diccionario para contar la cantidad de productos comprados por cada cliente en las categorías seleccionadas
    compras_por_cliente = {cliente['id_cliente']: {'nombre': cliente['nombre'], 'total_compras': 0} for cliente in clientes}

    # Fuerza bruta: iterar sobre todas las ventas y contar las compras en las categorías seleccionadas
    for venta in ventas:
        id_producto = venta['id_producto']
        id_cliente = venta['id_cliente']
        cantidad = int(venta['cantidad'])

        # Encontrar el producto correspondiente
        producto = next((p for p in productos if p['id_producto'] == id_producto), None)
        if producto and producto['categoria'] in categorias_seleccionadas:
            compras_por_cliente[id_cliente]['total_compras'] += cantidad

    # Ordenar a los clientes por la cantidad total de productos comprados
    clientes_ordenados = sorted(compras_por_cliente.values(), key=lambda x: x['total_compras'], reverse=True)

    # Mostrar los resultados
    print("\nClientes que más han comprado productos en las categorías seleccionadas:")
    for cliente in clientes_ordenados:
        if cliente['total_compras'] > 0:  # Solo mostrar clientes con compras
            print(f"{cliente['nombre']} - Total de productos comprados: {cliente['total_compras']}")

