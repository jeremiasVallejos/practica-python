# Función para crear una lista a partir de una entrada del usuario
def crear_lista():
    try:
        entrada = input("Ingresa una serie de lenguajes de programación separados por comas: ")
        lista = [lenguaje.strip() for lenguaje in entrada.split(",")]
        return lista
    except Exception as e:
        print(f"Error al crear la lista: {e}")
        return []

# Función para agregar un nuevo lenguaje a la lista
def agregar_lenguaje(lista, nuevo_lenguaje):
    try:
        lista.append(nuevo_lenguaje)
        return lista
    except Exception as e:
        print(f"Error al agregar el lenguaje: {e}")
        return lista

# Función para eliminar un lenguaje de la lista
def eliminar_lenguaje(lista, lenguaje_a_eliminar):
    try:
        lista.remove(lenguaje_a_eliminar)
        return lista
    except ValueError:
        print(f"El lenguaje '{lenguaje_a_eliminar}' no está en la lista.")
        return lista
    except Exception as e:
        print(f"Error al eliminar el lenguaje: {e}")
        return lista

# Función para encontrar el lenguaje con el nombre más extenso
def encontrar_mas_extenso(lista):
    try:
        return max(lista, key=len)
    except ValueError:
        print("La lista está vacía.")
        return None
    except Exception as e:
        print(f"Error al encontrar el lenguaje más extenso: {e}")
        return None

print("Bienvenido al programa de gestión de lenguajes de programación.")
print("Primero, crearemos una lista de lenguajes.")
lenguajes = crear_lista()

print(f"\nLista actual de lenguajes: {lenguajes}")

print("\nAhora, vamos a agregar un nuevo lenguaje.")
nuevo_lenguaje = input("Ingresa el nuevo lenguaje: ")
lenguajes = agregar_lenguaje(lenguajes, nuevo_lenguaje)
print(f"Lista actualizada: {lenguajes}")

print("\nVamos a eliminar un lenguaje.")
lenguaje_a_eliminar = input("Ingresa el lenguaje que deseas eliminar: ")
lenguajes = eliminar_lenguaje(lenguajes, lenguaje_a_eliminar)
print(f"Lista actualizada: {lenguajes}")

print("\nVamos a encontrar el lenguaje más extenso.")
mas_extenso = encontrar_mas_extenso(lenguajes)
if mas_extenso:
    print(f"El lenguaje más extenso es: {mas_extenso}")

print("\n¡Gracias por usar el programa!")
