import os
import csv
from datetime import datetime

# Definimos la ruta base donde se encuentran los archivos CSV
RUTA_BASE = "./archivos"


def cargar_csv(archivo):
    """
    Cargo un archivo CSV y devuelvo su contenido como una lista de diccionarios.
    """
    ruta_archivo = os.path.join(RUTA_BASE, archivo)
    try:
        with open(ruta_archivo, 'r') as archivo:
            lector = csv.DictReader(archivo)
            # Leo todas las filas del archivo y las devuelvo como lista de diccionarios
            return [fila for fila in lector]
    except FileNotFoundError:
        # Si el archivo no se encuentra, informo del error y devuelvo una lista vacía
        print(f"Error: No se encontró el archivo '{archivo}' en la ruta '{RUTA_BASE}'.")
        return []


def filtrar_ventas_por_producto(ventas, id_producto):
    """
    Filtro las ventas de un producto específico y las convierto en un formato procesable.
    """
    try:
        # Procesamos cada venta, convirtiendo la fecha y la cantidad a los formatos esperados.
        return [
            {
                "fecha": datetime.strptime(venta["fecha"], "%Y-%m-%d"),
                "cantidad": int(venta["cantidad"])
            }
            for venta in ventas if venta["id_producto"] == id_producto
        ]
    except Exception as e:
        # Si ocurre un error al procesar las ventas, lo informo.
        print(f"Error al procesar las ventas: {e}")
        return []


def dividir_y_vencer_ventas(ventas):
    """
    Aplico el enfoque Divide y Vencerás para calcular el promedio de las cantidades de ventas.
    """
    if len(ventas) == 1:  # Caso base: si solo hay una venta, devuelvo la cantidad.
        return ventas[0]["cantidad"]

    # Divido la lista en dos mitades.
    mitad = len(ventas) // 2
    promedio_izquierda = dividir_y_vencer_ventas(ventas[:mitad])
    promedio_derecha = dividir_y_vencer_ventas(ventas[mitad:])

    # Combino los resultados calculando el promedio de ambas mitades.
    return (promedio_izquierda + promedio_derecha) / 2


def calcular_tasa_cambio(ventas):
    """
    Calculo la tasa de cambio promedio entre las cantidades de ventas mensuales.
    """
    if len(ventas) < 2:
        # Si hay menos de dos ventas, no es posible calcular tendencias.
        return 0

    tasas = []
    for i in range(1, len(ventas)):
        cantidad_actual = ventas[i]["cantidad"]
        cantidad_anterior = ventas[i - 1]["cantidad"]
        # Calculo la tasa de cambio entre la venta actual y la anterior.
        tasa = (cantidad_actual - cantidad_anterior) / cantidad_anterior if cantidad_anterior != 0 else 0
        tasas.append(tasa)

    # Devuelvo el promedio de todas las tasas calculadas.
    return sum(tasas) / len(tasas) if tasas else 0


def estimar_ventas_futuras():
    """
    Estimo las ventas futuras para un producto utilizando Divide y Vencerás y tasa de cambio.
    """
    # Cargo el archivo de ventas.
    ventas = cargar_csv("ventas.csv")
    if not ventas:
        print("No se pudieron cargar las ventas.")
        return

    # Solicito el ID del producto para el que se desea estimar las ventas.
    id_producto = input("Ingresa el ID del producto para estimar las ventas futuras: ").strip()

    # Filtrar ventas del producto seleccionado.
    ventas_producto = filtrar_ventas_por_producto(ventas, id_producto)
    ventas_producto.sort(key=lambda x: x["fecha"])  # Ordeno las ventas por fecha.

    if not ventas_producto:
        print(f"No se encontraron ventas para el producto con ID {id_producto}.")
        return

    # Calculo el promedio histórico de las ventas usando Divide y Vencerás.
    promedio_historico = dividir_y_vencer_ventas(ventas_producto)

    # Calculo la tasa de cambio promedio entre las ventas consecutivas.
    tasa_cambio = calcular_tasa_cambio(ventas_producto)

    # Proyección para el próximo mes.
    ultima_cantidad = ventas_producto[-1]["cantidad"]  # Tomo la última cantidad registrada.
    proyeccion = ultima_cantidad * (1 + tasa_cambio)  # Aplico la tasa de cambio al último dato.

    # Muestro la estimación de ventas futuras.
    print(f"\nEstimación de Ventas Futuras para el Producto {id_producto}:")
    print(f"Promedio histórico: {round(promedio_historico, 2)} unidades.")
    print(f"Proyección estimada para el próximo mes: {round(proyeccion, 2)} unidades.")
