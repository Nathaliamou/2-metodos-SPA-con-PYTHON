# Definición de la clase Producto
class Producto:
    def __init__(self, id, nombre, precio_unitario, pais_origen, unidades_existentes, garantia):
        self.id = id
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.pais_origen = pais_origen
        self.unidades_existentes = unidades_existentes
        self.garantia = garantia

    # Método para calcular el costo total del producto
    def costo_total(self):
        return self.precio_unitario * self.unidades_existentes

# Definición de la clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def registrar_producto(self, producto):
        self.productos.append(producto)

# Función principal 
def main():
    # Crear una instancia del inventario
    inventario = Inventario()
    
    # Registro de frutas en el inventario
    inventario.registrar_producto(Producto(1, "Manzana",750, "Estados Unidos", 10, True))
    inventario.registrar_producto(Producto(2, "Papaya",500, "Ecuador", 8, True))
    inventario.registrar_producto(Producto(3, "Fresa",1200, "Espana", 6, False))
    inventario.registrar_producto(Producto(4, "Pina",1800, "Costa Rica", 7, True))
    inventario.registrar_producto(Producto(5, "Uva", 2000, "Italia", 9, False))
    inventario.registrar_producto(Producto(6, "Mango",1500, "Mexico", 5, True))
    inventario.registrar_producto(Producto(7, "Sandia",5000, "Espana", 4, False))
    inventario.registrar_producto(Producto(8, "Kiwi",1300, "Nueva Zelanda", 7, True))
    inventario.registrar_producto(Producto(9, "Naranja",900, "Espana", 8, True))
    inventario.registrar_producto(Producto(10, "Uchuva",600, "Mexico", 6, False))
    
    while True:
        print("\n1. Mostrar frutas existentes")
        print("2. Agregar nueva fruta al inventario")
        print("3. Mostrar costo total del salpicón")
        print("4. Mostrar frutas ordenadas por costo")
        print("5. Mostrar fruta más barata")
        print("6. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            print("\nFrutas existentes:")
            for producto in inventario.productos:
                print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio unitario: {producto.precio_unitario}, Cantidad: {producto.unidades_existentes}")
        
        elif opcion == 2:
            nueva_fruta = recibir_fruta_por_teclado()
            inventario.registrar_producto(nueva_fruta)
            print("¡Fruta agregada al inventario!")
        
        elif opcion == 3:
            mostrar_costo_total(inventario.productos)
            
        
        elif opcion == 4:
            mostrar_productos_ordenados_por_costo(inventario.productos)
        
        elif opcion == 5:
            mostrar_producto_mas_barato(inventario.productos)
        
        elif opcion == 6:
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Intente de nuevo.")

# recibir datos de un nuevo producto por teclado
def recibir_fruta_por_teclado():
    id = int(input("Ingrese el ID del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    precio_unitario = int(input("Ingrese el precio unitario del producto: "))
    unidades_existentes = int(input("Ingrese la cantidad de unidades existentes del producto: "))
    pais_origen = input("Ingrese el país de origen del producto: ")
    garantia = bool(input("El producto tiene garantía? (True/False): "))
    return Producto(id, nombre, precio_unitario, pais_origen, unidades_existentes, garantia)

# mostrar el costo total del salpicón
def mostrar_costo_total(productos):
    costo_total = sum(producto.costo_total() for producto in productos)
    print(f"El costo total del salpicón es: {costo_total}")
"""
# mostrar los productos ordenados por costo de mayor a menor
def mostrar_productos_ordenados_por_costo(productos):
# Ordena los productos utilizando la función sorted() o sort(), donde se especifica la clave de ordenamiento
    # La clave de ordenamiento es una función lambda que devuelve el costo total del producto
    #key toma la funcion que se aplicara a a cada elemento de la lista. Junto con lambda en funcines de ordenamiento
    # Se utiliza reverse=True para ordenar de mayor a menor costo
    #lambda crea funciones anonimas, con cualquier num de argumentos y una expres. se usa para ordenamiento y filtrado.
    productos_ordenados = sorted(productos, key=lambda x: x.costo_total(), reverse=True)
    print("Productos ordenados de mayor a menor costo:")
    for producto in productos_ordenados:
        print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio unitario: {producto.precio_unitario}, Cantidad: {producto.unidades_existentes}")
"""
"""
# mostrar los productos ordenados por costo de mayor a menor
def mostrar_productos_ordenados_por_costo(productos):
    productos.sort(key=lambda x: x.costo_total(), reverse=True)
    print("Productos ordenados de mayor a menor costo:")
    for producto in productos:
        print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio unitario: {producto.precio_unitario}, Cantidad: {producto.unidades_existentes}")
"""
# obtener el precio unitario de un producto
def obtener_precio_unitario(producto):
    #retorna precio unitario de la fruta
    return producto.precio_unitario

# mostrar los productos ordenados por costo de mayor a menor
def mostrar_productos_ordenados_por_costo(productos):
# Ordena los productos con método sort(),
    # La clave de ordenamiento:obtener_precio_unitario
    # reverse=True para ordenar M a m.
    productos.sort(key=obtener_precio_unitario, reverse=True)
    print("Productos ordenados por precio unitario de mayor a menor:")
    #itera
    for producto in productos:
        print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio unitario: {producto.precio_unitario}, Cantidad: {producto.unidades_existentes}")




# mostrar el producto más barato
def mostrar_producto_mas_barato(productos):
    producto_mas_barato = min(productos, key=lambda x: x.precio_unitario)
    print(f"El producto más barato es: {producto_mas_barato.nombre}, Precio unitario: {producto_mas_barato.precio_unitario}")

# Llamada a la función principal del programa
if __name__ == "__main__":
    main()
