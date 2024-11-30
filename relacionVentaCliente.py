import os
import csv

# Ruta base donde se encuentran los archivos CSV
RUTA_BASE = "ruta/a/tu/carpeta"  # Cambia esto por la ruta de tu carpeta

def cargar_csv(nombre_archivo):
    """Función para cargar un archivo CSV."""
    ruta_archivo = os.path.join(RUTA_BASE, nombre_archivo)
    try:
        with open(ruta_archivo, 'r') as archivo:
            lector = csv.DictReader(archivo)
            return [fila for fila in lector]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}' en la ruta '{RUTA_BASE}'")
        return []

def integrar_ventas_clientes():
    """Crea la relación entre ventas y clientes."""
    # Cargar los datos
    ventas = cargar_csv('ventas.csv')
    clientes = cargar_csv('clientes.csv')

    # Verificar que los datos se hayan cargado correctamente
    if not ventas or not clientes:
        print("Error: Uno o más archivos no se pudieron cargar correctamente.")
        return

    # Crear un diccionario para mapear clientes por id_cliente
    clientes_dict = {cliente['id_cliente']: cliente for cliente in clientes}

    # Relacionar ventas con clientes
    ventas_con_clientes = []
    for venta in ventas:
        cliente_id = venta.get('id_cliente')  # Obtener el id_cliente en la venta
        cliente = clientes_dict.get(cliente_id)  # Buscar el cliente correspondiente
        if cliente:
            # Agregar datos del cliente a la venta
            venta_con_cliente = venta.copy()  # Copia para no alterar el original
            venta_con_cliente.update({
                'nombre_cliente': cliente['nombre'],
                'apellido_cliente': cliente['apellido'],
                'email_cliente': cliente['email']
            })
            ventas_con_clientes.append(venta_con_cliente)
        else:
            print(f"Advertencia: No se encontró el cliente con id {cliente_id}")

    return ventas_con_clientes

def mostrar_ventas_clientes():
    """Muestra las ventas con la información del cliente."""
    ventas_clientes = integrar_ventas_clientes()
    if ventas_clientes:
        print("\nRelación Ventas-Clientes:")
        for venta in ventas_clientes:
            print(f"Venta ID: {venta['id_venta']}, Producto: {venta['id_producto']}, "
                f"Cantidad: {venta['cantidad']}, Cliente: {venta['nombre_cliente']} {venta['apellido_cliente']}, "
                f"Email: {venta['email_cliente']}")


    mostrar_ventas_clientes()