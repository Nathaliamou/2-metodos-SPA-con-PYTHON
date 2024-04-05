# inventario.py
#Este archivo contendrá la definición de la clase Inventario y 
#las funciones relacionadas con la gestión del inventario.
#from producto import Producto

"""
 Este archivo contiene la definición de la clase Inventario y las funciones relacionadas con la gestión del inventario. Aquí es donde almacena la clase Inventario y sus métodos, así como otras funciones relacionadas con la gestión del inventario.
"""
from momento01.producto import Producto  # Asegúrate de que la ruta sea correcta según la ubicación de tu archivo Producto.py

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

    # Otras funciones relacionadas con la gestión del inventario...
    """
    La función cargar_datos_desde_archivo se encarga de cargar datos desde archivo de texto y devolverlos en forma de diccionario.
    """
def cargar_datos_desde_archivo(archivo):
    datos = {}
    with open(archivo, 'r') as f:
        for linea in f:
            partes = linea.strip().split()
            # Verificar si hay el mismo número de partes que de atributos
            if len(partes) != 9:
                print("Error: El número de columnas en la línea no coincide con el número de atributos.")
                continue  # Saltar esta línea y pasar a la siguiente

            # Definir una lista de nombres de atributos en el orden correcto
            nombres_atributos = ["id", "nombre", "precio", "casa", "referencia", "pais", "unidades", "garantia", "descripcion"]

            # Asignar los valores de las partes a los atributos correspondientes
            producto = Producto(
    id=int(partes[0]),
    nombre=partes[1],
    precio=float(partes[2]),
    ubicacion=partes[3],  # Asegúrate de incluir la ubicación
    casa=partes[3],
    referencia=partes[4],
    pais=partes[5],
    unidades=int(partes[6]),
    garantia=partes[7] == "True",
    descripcion=" ".join(partes[8:])
)
            datos[producto.nombre] = producto

    return datos
def main():
    # Cargar datos desde el archivo
    datos_comics = cargar_datos_desde_archivo('./tienda_comic/datos_comics.txt')

    # Crear una instancia del inventario
    inventario = Inventario()

    # Agregar productos al inventario
    for producto in datos_comics.values():
        inventario.registrar_producto(producto)

    # Resto del código...

if __name__ == "__main__":
    main()

