import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    for libro in libros:
        if libro['cant_ej_pr'] > 0:
            print(f"Libro: {libro['titulo']} por {libro['autor']}")
            print(f"Cantidad de ejemplares prestados: {libro['cant_ej_pr']}")
    else:
        print("No hay ejemplares prestados en este momento.")
    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    titulo = input("Ingrese el título del nuevo libro: ")
    autor = input("Ingrese el autor del nuevo libro: ")
    cant_ej_ad = int(input("Ingrese la cantidad de ejemplares adquiridos: "))
    cod = generar_codigo()
    nuevo_libro = {
        'cod': cod,
        'cant_ej_ad': cant_ej_ad,
        'cant_ej_pr': 0,
        'titulo': titulo,
        'autor': autor
    }
    libros.append(nuevo_libro)
    print(f"Libro registrado con éxito. Código: {cod}")
    return None

def eliminar_ejemplar_libro():
    #completar
    return None

def prestar_ejemplar_libro():
    codigo = input("Ingrese el código del libro: ")
    for libro in libros:
        if libro['cod'] == codigo:
            if libro['cant_ej_ad'] > libro['cant_ej_pr']:
                print(f"Libro: {libro['titulo']} por {libro['autor']}")
                print(f"Cantidad de ejemplares disponibles: {libro['cant_ej_ad'] - libro['cant_ej_pr']}")
                confirmacion = input("¿Desea realizar el préstamo? (S/N): ").upper()
                if confirmacion == 'S':
                    libro['cant_ej_pr'] += 1
                    print("Préstamo realizado con éxito.")
                else:
                    print("Préstamo cancelado.")
            else:
                print("No quedan ejemplares disponibles para préstamo.")
            return
    print("Libro no encontrado o código incorrecto.")
    return None

def devolver_ejemplar_libro():
    #completar
    return None

def nuevo_libro():
    #completar
    return None