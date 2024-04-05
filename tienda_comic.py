"""
Codificar un programa que le permita a un organizador de una tienda de comics administrar el inventario de la tienda,
el software debe tener un menú de opciones realizado en Python que permita registrar un producto de la tienda con los siguientes atributos:+ Id generado automáticamente (1-100 y sin repetir),
+ Nombre del producto
+ Precio unitario del producto
+ Ubicación en la tienda (la tienda tiene 4 zonas (A,B,C,D) cada una con una capacidad máxima de 50 productos
+ Descripción del producto
+ Casa a la que pertenece el producto (Marvel, DC,etc)
+ Referencia (código alfanumérico)
+ País de origen del producto
+ Numero de unidades compradas del producto
+ Producto con garantía extendida (true/false)
-Buscar y mostrar en consola todos los productos en bodega
—Buscar y mostrar en consola (el id, el nombre, el preciounitario y la descripción) de un producto especifico este
debe buscarse por nombre.
-Buscar y modificar el numero de unidades compradas delproducto, esta modificación nunca podrá ser mayor al
número inicial ingresado.
-Eliminar un producto del inventario buscándolo por nombre,debe pedir confirmación antes de borrarlo
"""
# Importar la biblioteca necesaria
import random
import subprocess
import shutil
# Definir las clases Producto e Inventario
class Producto:
    def __init__(self, id, nombre, precio, ubicacion, descripcion, casa, referencia, pais, unidades, garantia):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.ubicacion = ubicacion
        self.descripcion = descripcion
        self.casa = casa
        self.referencia = referencia
        self.pais = pais
        self.unidades = unidades
        self.garantia = garantia

class Inventario:
    def __init__(self):
        self.productos = []

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print("ID:", producto.id)
            print("Nombre:", producto.nombre)
            print("Precio unitario:", producto.precio)
            print("Ubicación:", producto.ubicacion)
            print("Descripción:", producto.descripcion)
            print("Casa:", producto.casa)
            print("Referencia:", producto.referencia)
            print("País de origen:", producto.pais)
            print("Número de unidades:", producto.unidades)
            print("Garantía extendida:", producto.garantia)
            print("--------------------")

    def buscar_producto_por_nombre(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                print("ID:", producto.id)
                print("Nombre:", producto.nombre)
                print("Precio unitario:", producto.precio)
                print("Descripción:", producto.descripcion)
                return
        print("Producto no encontrado.")

    def modificar_unidades_compradas(self, nombre, nuevas_unidades):
        for producto in self.productos:
            if producto.nombre == nombre:
                if nuevas_unidades <= producto.unidades:
                    producto.unidades = nuevas_unidades
                    print("Unidades modificadas exitosamente.")
                    return
                else:
                    print("La modificación excede el número inicial de unidades.")
                    return
        print("Producto no encontrado.")

    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                confirmacion = input("¿Estás seguro que deseas eliminar este producto? (s/n): ")
                if confirmacion.lower() == 's':
                    self.productos.remove(producto)
                    print("Producto eliminado.")
                    return
                else:
                    print("Operación cancelada.")
                    return
        print("Producto no encontrado.")

# Función para generar un ID único para cada producto
def generar_id():
    global contador_id
    contador_id += 1
    return contador_id

# Inicializar el contador de ID global
contador_id = 0

# Función principal
def main():
    # Crear una instancia del inventario
    inventario = Inventario()

    # Registro de cómics en la base de datos
    inventario.registrar_producto(Producto(1, "Spider-Man", 15.99, "Zona A", "Tomo recopilatorio de cómics de Spider-Man", "Marvel", "SM001", "Estados Unidos", 50, False))
    inventario.registrar_producto(Producto(2, "Batman: El regreso del Caballero Oscuro", 19.99, "Zona B", "Cómic de Batman escrito y dibujado por Frank Miller", "DC", "BROCO001", "Estados Unidos", 30, False))
    inventario.registrar_producto(Producto(3, "X-Men: La era de Apocalipsis", 24.99, "Zona C", "Saga de cómics de X-Men ambientada en un mundo gobernado por Apocalipsis", "Marvel", "XMA002", "Estados Unidos", 20, False))
    inventario.registrar_producto(Producto(4, "Watchmen", 18.50, "Zona D", "Novela gráfica escrita por Alan Moore e ilustrada por Dave Gibbons", "DC", "WATCH001", "Reino Unido", 40, False))
    inventario.registrar_producto(Producto(5, "Saga", 12.99, "Zona A", "Saga de ciencia ficción/fantasía escrita por Brian K. Vaughan e ilustrada por Fiona Staples", "Image Comics", "SAGA001", "Estados Unidos", 60, False))
    inventario.registrar_producto(Producto(6, "Sandman", 16.75, "Zona B", "Serie de cómics escrita por Neil Gaiman e ilustrada por diversos artistas", "DC", "SAND001", "Estados Unidos", 25, False))
    inventario.registrar_producto(Producto(7, "The Walking Dead", 14.99, "Zona C", "Serie de cómics de zombies escrita por Robert Kirkman", "Image Comics", "TWD001", "Estados Unidos", 35, False))
    inventario.registrar_producto(Producto(8, "Daredevil: Born Again", 17.25, "Zona D", "Arco argumental de Daredevil escrito por Frank Miller", "Marvel", "DD001", "Estados Unidos", 45, False))
    inventario.registrar_producto(Producto(9, "V de Vendetta", 21.00, "Zona A", "Novela gráfica de Alan Moore e ilustrada por David Lloyd", "DC", "V001", "Reino Unido", 15, False))
    inventario.registrar_producto(Producto(10, "The Boys", 20.50, "Zona B", "Serie de cómics escrita por Garth Ennis e ilustrada por Darick Robertson", "Dynamite Entertainment", "BOYS001", "Estados Unidos", 22, False))

    while True:
        print("\n1. Mostrar todos los productos en bodega")
        print("2. Buscar producto por nombre")
        print("3. Modificar unidades compradas")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            inventario.mostrar_productos()
        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)
        elif opcion == '3':
            nombre = input("Ingrese el nombre del producto a modificar: ")
            nuevas_unidades = int(input("Ingrese el nuevo número de unidades: "))
            inventario.modificar_unidades_compradas(nombre, nuevas_unidades)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()