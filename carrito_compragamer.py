from carrito_compragamer_funciones import Producto  #importamos libreria de funciones
from carrito_compragamer_funciones import CarritoCompras

# diccionario de productos
productos = {
    "1001": Producto("1001", "Procesador", "Ryzen", 93900.50, 80, "Gris plata", "5 3600 4.2GHz Turbo AM4 Wraith Stealth Cooler"),
    "1002": Producto("1002", "Memoria Ram", "Patriot", 20600.75, 156, "Negro", "Memoria Patriot DDR4 8GB 3200Mhz Signature"),
    "1003": Producto("1003", "Fuente de alimentación", "Asus", 39000.0, 56, "Negro", "Fuente ASUS TUF 550W 80 Plus Bronze 550B"),
    "1004": Producto("1004", "Disco sólido", "Crucial 3", 26620.0, 99, " Negro", "Disco Solido SSD M.2 Crucial 500GB P3 3500MB/s NVMe PCI-E x4"),
    "1005": Producto("1005", "Gabinete", "Gamemax", 24450.0, 60, "Negro y rojo", "Gabinete Gamemax H601 BR Black & Red M-ATX FAN 1 x 120mm")
}

carrito = CarritoCompras(productos) # defino objeto, para llamar a la clase utilizo (), como si fuese una funcion

while True:
    print("Bienvenidos a COMPRA GAMER")
    print("1) Mostrar productos en detalle")
    print("2) Mostrar información breve del producto")
    print("3) Buscar producto por código")
    print("4) Realizar compra")
    print("5) Modificar compra")
    print("6) Eliminar producto del carrito")
    print("7) Finalizar compra")
    print("8) Salir")

    opcion = input("Seleccione una opción: ")
    print("--------------------------------------------------------------")

    if opcion == "1":
        carrito.mostrar_productos_detalle() #accedo a ese metodo
    elif opcion == "2":
        carrito.mostrar_informacion_breve()
    elif opcion == "3":
        codigo_producto = input("Ingrese el código del producto que desea buscar: ")
        carrito.buscar_producto_por_codigo(codigo_producto)  
    elif opcion == "4":
        carrito.realizar_compra()
    elif opcion == "5":
        carrito.modificar_compra()
    elif opcion == "6":
                carrito.eliminar_producto()
    elif opcion == "7":
                carrito.finalizar_compra()
    elif opcion == "8":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
    print("--------------------------------------------------------------")

