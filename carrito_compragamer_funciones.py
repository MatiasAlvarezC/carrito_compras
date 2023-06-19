class Producto:
    def __init__(self, codigo, nombre, marca, precio, stock, color, caracteristicas):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock
        self.color = color
        self.caracteristicas = caracteristicas


class CarritoCompras:
    def __init__(self, productos):
        self.productos = productos
        self.carrito = {}   # lo inicializamos como un diccionario vacio

    def mostrar_productos_detalle(self):
        print("Productos en detalle:")
        for producto_id, producto in self.productos.items():   #producto_id guarda la clave de cada elemento del diccionario
            print("Código:", producto.codigo)
            print("Nombre:", producto.nombre)
            print("Marca:", producto.marca)
            print("Precio: $", producto.precio)
            print("Stock:", producto.stock)
            print("Color:", producto.color)
            print("Características:", producto.caracteristicas)
            print("--------------------------------------------------------------")

    def mostrar_informacion_breve(self):
        print("Información breve de los productos:")
        for producto_id, producto in self.productos.items():
            print("Código:", producto.codigo)
            print("Nombre:", producto.nombre)
            print("Precio: $", producto.precio)
            print("Cantidad disponible:", producto.stock)
            print("--------------------------------------------------------------")

    def buscar_producto_por_codigo(self, codigo_producto):
        if codigo_producto in self.productos:
            producto = self.productos[codigo_producto]
            print("Información detallada del producto:")
            print("Código:", producto.codigo)
            print("Nombre:", producto.nombre)
            print("Marca:", producto.marca)
            print("Precio: $", producto.precio)
            print("Stock:", producto.stock)
            print("Color:", producto.color)
            print("Características:", producto.caracteristicas)
        else:
            print("No se encontró ningún producto con ese código.")

    def realizar_compra(self):
        self.mostrar_informacion_breve()  #para que el usuario vea mas rapido las opciones
        codigo_producto = input("Ingrese el código del producto que desea agregar al carrito: ")
        if codigo_producto in self.productos:
            producto = self.productos[codigo_producto]
            while True:
                cantidad = (input("Ingrese la cantidad que desea comprar: "))
                if cantidad.isdigit():  #verifica si el numero ingresado es entero
                    cantidad = int(cantidad)
                    break
                else:
                    print("Ingrese un numero entero")

            if cantidad > 0:
                if cantidad <= producto.stock:
                    confirmar = input("¿Desea agregar este producto al carrito? (SI/NO): ")
                    if confirmar.upper() == "SI":
                        if codigo_producto in self.carrito:
                            self.carrito[codigo_producto]["cantidad"] += cantidad  #incrementa cantidad +=
                        else:
                            self.carrito[codigo_producto] = {
                                'nombre': producto.nombre,
                                'cantidad': cantidad,
                                'precio_unitario': producto.precio,
                                'costo_total': cantidad * producto.precio
                            }
                        self.productos[codigo_producto].stock -= cantidad
                        print("Producto agregado al carrito")
                    else:
                        print("La compra no ha sido confirmada")
                else:
                    print("No hay suficiente stock disponible")
            else:
                print("La cantidad ingresada no es válida")
        else:
            print("No se encontró ningún producto con ese código")

    def modificar_compra(self):
        if self.carrito:
            self.mostrar_carrito()
            producto_modificar = input("Ingrese el código del producto que desea modificar en el carrito: ")
            if producto_modificar in self.carrito:
                nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                if nueva_cantidad > 0:
                    confirmar = input("¿Desea modificar la cantidad de este producto en el carrito? (SI/NO): ")
                    if confirmar.upper() == "SI":
                        self.productos[producto_modificar].stock += self.carrito[producto_modificar]["cantidad"]
                        self.productos[producto_modificar].stock -= nueva_cantidad
                        self.carrito[producto_modificar]["cantidad"] = nueva_cantidad
                        self.carrito[producto_modificar]["costo_total"] = nueva_cantidad * self.carrito[producto_modificar]["precio_unitario"]
                        print("Producto modificado exitosamente")
                    else:
                        print("La modificación no ha sido confirmada")
                else:
                    print("La cantidad debe ser mayor que cero")
            else:
                print("No se encontró ningún producto con ese código en el carrito")
        else:
            print("El carrito de compras está vacío")

    def eliminar_producto(self):
        if self.carrito:
            self.mostrar_carrito()
            producto_eliminar = input("Ingrese el código del producto que desea eliminar del carrito: ")
            if producto_eliminar in self.carrito:
                confirmar = input("¿Desea eliminar este producto del carrito? (SI/NO): ")
                if confirmar.upper() == "SI":
                    self.productos[producto_eliminar].stock += self.carrito[producto_eliminar]["cantidad"]
                    del self.carrito[producto_eliminar]
                    print("Producto eliminado exitosamente del carrito")
                else:
                    print("La eliminación no ha sido confirmada")
            else:
                print("No se encontró ningún producto con ese código en el carrito")
        else:
            print("El carrito de compras está vacío")

    def mostrar_carrito(self):  #lo utilizo para mostrar al usuario en opciones para que sea mas visible
        if self.carrito:
            print("Productos en el carrito:")
            for producto_id, producto_info in self.carrito.items():
                print("Código:", producto_id)
                print("Nombre:", producto_info["nombre"])
                print("Cantidad:", producto_info["cantidad"])
                print("Precio unitario: $", producto_info["precio_unitario"])
                print("Costo total: $", producto_info["costo_total"])
                print("---------------------------------------------------------------")
        else:
            print("El carrito de compras está vacío")

    def finalizar_compra(self):
        if self.carrito:
            self.mostrar_carrito()
            confirmar = input("¿Desea finalizar la compra? (SI/NO): ")
            if confirmar.upper() == "SI":
                print("Detalle de la compra:")
                total = 0.0   #inicializamos en cero
                for producto_id, producto_info in self.carrito.items():
                    print("Nombre:", producto_info["nombre"])
                    print("Cantidad:", producto_info["cantidad"])
                    print("Precio unitario: $", producto_info["precio_unitario"])
                    print("Costo total: $", producto_info["costo_total"])
                    print("--------------------------------------------------------------")
                    total += producto_info["costo_total"]
                print("Total de la compra: $",total)
                self.carrito.clear()    #dejamos el carrito en cero
                print("Compra finalizada")
            else:
                print("La finalización de la compra no ha sido confirmada")
        else:
            print("El carrito de compras está vacío")