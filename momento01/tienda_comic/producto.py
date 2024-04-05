# producto.py
# Este archivo contendrá la definición de la clase Producto, aqui definir la clase Producto y sus atributos.
class Producto:
    def __init__(self, id, nombre, precio, ubicacion, casa, referencia, pais, unidades, garantia, descripcion):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.ubicacion = ubicacion  # Asegúrate de tener este atributo
        self.casa = casa
        self.referencia = referencia
        self.pais = pais
        self.unidades = unidades
        self.garantia = garantia
        self.descripcion = descripcion
