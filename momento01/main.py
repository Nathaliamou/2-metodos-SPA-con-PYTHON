# main.py
#main.py: Este archivo será el punto de entrada de tu aplicación y contendrá la función principal main().
"""
Este archivo contiene la función principal main() que ejecuta el programa y el bucle principal del menú. Aquí es donde llamas a la función cargar_datos_desde_archivo y pasarle el nombre del archivo de datos. Además, este archivo importa las clases y funciones necesarias de otros archivos.
"""
#import pathlib
#import sys
#sys.path.append('c:/Users/norozco.ADMIN/OneDrive - CESDE/Desktop/prueba/python/momento01/tienda_comic')

#from momento01.gestor_inventario import Inventario
#from momento01.producto import Producto

# Función para generar un ID único para cada producto
from momento01.tienda_comic.gestor_inventario import Inventario

def generar_id():
    global contador_id
    contador_id += 1
    return contador_id

# Función principal
def main():
    # Crear una instancia del inventario
    inventario = Inventario()

    # Registro de cómics en la base de datos
    # ...

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
