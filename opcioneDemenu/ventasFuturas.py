import os
import csv
from datetime import datetime

# Ruta base donde se encuentran los archivos CSV
RUTA_BASE = "./archivos"  # Cambia esto por la ruta de tu carpeta

def cargar_csv(archivo):
    """Carga un archivo CSV y devuelve su contenido como una lista de diccionarios."""
    ruta_archivo = os.path.join(RUTA_BASE, archivo)
    try:
        with open(ruta_archivo, 'r') as archivo:
            lector = csv.DictReader(archivo)
            return [fila for fila in lector]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}' en la ruta '{RUTA_BASE}'.")
        return []

def filtrar_ventas_por_producto(ventas, id_producto):
    """Filtra las ventas de un producto específico."""
    try:
        return [
            {
                "fecha": datetime.strptime(venta["fecha"], "%Y-%m-%d"),
                "cantidad": int(venta["cantidad"])
            }
            for venta in ventas if venta["id_producto"] == id_producto
        ]
    except Exception as e:
        print(f"Error al procesar las ventas: {e}")
        return []

def dividir_y_vencer_ventas(ventas):
    """
    Divide y vence: Calcula el promedio de las cantidades de ventas.
    """
    if len(ventas) == 1:  # Caso base
        return ventas[0]["cantidad"]
    
    mitad = len(ventas) // 2
    promedio_izquierda = dividir_y_vencer_ventas(ventas[:mitad])
    promedio_derecha = dividir_y_vencer_ventas(ventas[mitad:])
    
    return (promedio_izquierda + promedio_derecha) / 2

def calcular_tasa_cambio(ventas):
    """
    Calcula la tasa de cambio promedio entre las cantidades de ventas mensuales.
    """
    if len(ventas) < 2:
        return 0  # No hay suficientes datos para calcular tendencias

    tasas = []
    for i in range(1, len(ventas)):
        cantidad_actual = ventas[i]["cantidad"]
        cantidad_anterior = ventas[i - 1]["cantidad"]
        tasa = (cantidad_actual - cantidad_anterior) / cantidad_anterior if cantidad_anterior != 0 else 0
        tasas.append(tasa)

    return sum(tasas) / len(tasas) if tasas else 0

def estimar_ventas_futuras():
    """
    Estima las ventas futuras para un producto utilizando Divide y Vencerás y tasa de cambio.
    """
    ventas = cargar_csv("ventas.csv")
    if not ventas:
        print("No se pudieron cargar las ventas.")
        return

    id_producto = input("Ingresa el ID del producto para estimar las ventas futuras: ").strip()

    # Filtrar ventas del producto seleccionado
    ventas_producto = filtrar_ventas_por_producto(ventas, id_producto)
    ventas_producto.sort(key=lambda x: x["fecha"])

    if not ventas_producto:
        print(f"No se encontraron ventas para el producto con ID {id_producto}.")
        return

    # Calcular promedio histórico
    promedio_historico = dividir_y_vencer_ventas(ventas_producto)

    # Calcular tasa de cambio promedio
    tasa_cambio = calcular_tasa_cambio(ventas_producto)

    # Proyección para el próximo mes
    ultima_cantidad = ventas_producto[-1]["cantidad"]
    proyeccion = ultima_cantidad * (1 + tasa_cambio)

    print(f"\nEstimación de Ventas Futuras para el Producto {id_producto}:")
    print(f"Promedio histórico: {round(promedio_historico, 2)} unidades.")
    print(f"Proyección estimada para el próximo mes: {round(proyeccion, 2)} unidades.")
