import os
import csv
from datetime import datetime

# Ruta base donde se encuentran los archivos CSV
RUTA_BASE = "./archivos"  # Cambia esto por la ruta de tu carpeta

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

def filtrar_ventas_por_producto(ventas, id_producto):
    """Filtra las ventas de un producto específico."""
    return [
        {
            "fecha": datetime.strptime(venta["fecha"], "%Y-%m-%d"),
            "cantidad": int(venta["cantidad"])
        }
        for venta in ventas if venta["id_producto"] == id_producto
    ]

def dividir_y_vencer_ventas(ventas):
    """
    Divide y vence: Estima el promedio de ventas usando recursión.
    Calcula el promedio de las cantidades de ventas.
    """
    if len(ventas) == 1:  # Caso base: Si solo hay una venta, devuelve la cantidad
        return ventas[0]["cantidad"]
    
    # Dividir los datos en dos mitades
    mitad = len(ventas) // 2
    izquierda = dividir_y_vencer_ventas(ventas[:mitad])
    derecha = dividir_y_vencer_ventas(ventas[mitad:])
    
    # Combinar los resultados calculando el promedio
    return (izquierda + derecha) / 2

def estimar_ventas_futuras(id_producto):
    """Estima las ventas futuras para un producto utilizando Divide y Vencerás."""
    ventas = cargar_csv("ventas.csv")
    
    # Filtrar las ventas del producto específico
    ventas_producto = filtrar_ventas_por_producto(ventas, id_producto)
    
    # Ordenar ventas por fecha
    ventas_producto.sort(key=lambda x: x["fecha"])
    if not ventas_producto:
        print(f"No se encontraron ventas para el producto con ID {id_producto}.")
        return
    
    
    # Estimar ventas futuras
    promedio_ventas = dividir_y_vencer_ventas(ventas_producto)
    print(f"\nEstimación de Ventas Futuras para el Producto {id_producto}:")
    print(f"Promedio de ventas estimado para el próximo mes: {round(promedio_ventas, 2)} unidades.")


    # Solicitar el ID del producto al usuario
id_producto = input("Ingresa el ID del producto para estimar las ventas futuras: ")
estimar_ventas_futuras(id_producto)