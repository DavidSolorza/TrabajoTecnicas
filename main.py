import opcioneDemenu.mostrarInicial as mostrarInicial
import opcioneDemenu.ventasFuturas as ventasFuturas




def menu_principal():
    print("----------------------------------------------------------")
    while True:
        print("Sistema de Análisis de Ventas - Menú Principal")
        print("1. Mostrar resumen inicial")
        print("2. Estimar ventas futuras de un producto")
        print("3. Simular compra")
        print("4. Revisión de productos dentro de un presupuesto")
        print("5. Análisis de clientes y productos")
        print("6. Informes gráficos")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrarInicial.mostrar_resumen_inicial()
        elif opcion == "2":
            ventasFuturas.estimar_ventas_futuras()
        # elif opcion == "3":
        #     simular_compra()
        # elif opcion == "4":
        #     revisar_presupuesto()
        # elif opcion == "5":
        #     analizar_clientes_productos()
        # elif opcion == "6":
        #     mostrar_informes_graficos()
        elif opcion == "7":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
    print("----------------------------------------------------------")


menu_principal()