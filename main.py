import opcioneDemenu.mostrarInicial as mostrarInicial
import opcioneDemenu.ventasFuturas as ventasFuturas
import opcioneDemenu.simularCompra as simularCompra
import opcioneDemenu.revisionPresupuesto as revisionPresupuesto
import opcioneDemenu.relacionProductoCliente as relacionProductoCliente



def menu_principal():
    print("----------------------------------------------------------")
    while True:
        print("\n\n\nSistema de Análisis de Ventas - Menú Principal")
        print("1. Mostrar resumen inicial")
        print("2. Estimar ventas futuras de un producto")
        print("3. Simular compra")
        print("4. Revisión de productos dentro de un presupuesto")
        print("5. Análisis de clientes y productos")
        print("6. Informes gráficos")
        print("7. Salir ")
        
        opcion = input("Seleccione una opción: ")
        print("\n\n\n")
        if opcion == "1":
            # Llamo al módulo para mostrar el resumen inicial
            mostrarInicial.mostrar_resumen_inicial()
        elif opcion == "2":
            # Llamo al módulo para estimar ventas futuras
            ventasFuturas.estimar_ventas_futuras()
        elif opcion == "3":
            # Llamo al módulo para simular una compra
            simularCompra.simular_compra()
        elif opcion == "4":
            # Llamo al módulo para revisión de productos por presupuesto
            revisionPresupuesto.revisar_presupuesto()
        elif opcion == "5":
            # Llamo al módulo para analizar clientes y productos
            relacionProductoCliente.relacionProductoCliente()
        elif opcion == "6":
            # Llamo al módulo para mostrar informes gráficos
            informesGraficos.mostrar_informes_graficos()
        elif opcion == "7":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
    print("----------------------------------------------------------")

if __name__ == '__main__':
    menu_principal()
