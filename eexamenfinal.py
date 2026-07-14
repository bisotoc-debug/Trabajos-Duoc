Diccionario_Peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False]
}

Diccionario_Cartera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3]
}


def cupos_genero(genero):

    total = 0

    for codigo, datos in Diccionario_Peliculas.items():

        if datos[1].lower() == genero.lower():

            total += Diccionario_Cartera[codigo][1]

    print(f"El total de cupos disponibles es: {total}")


def busqueda_precio(p_min, p_max):

    lista = []

    for codigo, datos in Diccionario_Cartera.items():

        precio = datos[0]
        cupos = datos[1]

        if p_min <= precio <= p_max and cupos > 0:

            titulo = Diccionario_Peliculas[codigo][0]
            lista.append(f"{titulo}--{codigo}")

    if len(lista) == 0:
        print("No hay películas en ese rango de precios.")
    else:

        lista.sort()

        for pelicula in lista:
            print(pelicula)


def buscar_codigo(codigo):

    codigo = codigo.upper()

    for cod in Diccionario_Peliculas:

        if cod.upper() == codigo:
            return True

    return False


def actualizar_precio(codigo, nuevo_precio):

    codigo = codigo.upper()

    if buscar_codigo(codigo):

        Diccionario_Cartera[codigo][0] = nuevo_precio
        return True

    return False


def eliminar_pelicula(codigo):

    codigo = codigo.upper()

    if buscar_codigo(codigo):

        del Diccionario_Peliculas[codigo]
        del Diccionario_Cartera[codigo]

        return True

    return False

def validar_codigo(codigo):

    if codigo.strip() == "":
        return False

    if buscar_codigo(codigo):
        return False

    return True


def validar_texto(texto):

    return texto.strip() != ""


def validar_duracion(duracion):

    return duracion > 0


def validar_clasificacion(clasificacion):

    return clasificacion.upper() in ["A", "B", "C"]


def validar_idioma(idioma):

    return idioma.strip() != ""


def validar_es3d(valor):

    return valor.lower() in ["s", "n"]


def validar_precio(precio):

    return precio > 0


def validar_cupos(cupos):

    return cupos >= 0


def agregar_pelicula(codigo, titulo, genero, duracion,
                     clasificacion, idioma, es_3d,
                     precio, cupos):

    codigo = codigo.upper()

    if buscar_codigo(codigo):
        return False

    Diccionario_Peliculas[codigo] = [
        titulo,
        genero,
        duracion,
        clasificacion.upper(),
        idioma,
        es_3d
    ]

    Diccionario_Cartera[codigo] = [
        precio,
        cupos
    ]

    return True


def Leer_Opciones():

    print("\n======= MENÚ PRINCIPAL =======")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")




def cine():

    while True:

        Leer_Opciones()

        try:

            opcion = int(input("Ingrese opción: "))

            if opcion == 1:

                genero = input("Ingrese género a consultar: ")
                cupos_genero(genero)

            elif opcion == 2:

                while True:

                    try:

                        p_min = int(input("Ingrese precio mínimo: "))
                        p_max = int(input("Ingrese precio máximo: "))

                        if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                            break

                        print("Rango inválido")

                    except ValueError:
                        print("Debe ingresar valores enteros")

                busqueda_precio(p_min, p_max)

            elif opcion == 3:

                seguir = "s"

                while seguir.lower() == "s":

                    codigo = input("Ingrese código: ").upper()

                    try:

                        nuevo_precio = int(input("Ingrese nuevo precio: "))

                        if actualizar_precio(codigo, nuevo_precio):
                            print("Precio actualizado")
                        else:
                            print("El código no existe")

                    except ValueError:
                        print("Debe ingresar un precio válido")

                    seguir = input("¿Desea actualizar otro precio (s/n)? ")

            elif opcion == 4:

                codigo = input("Código: ").upper()
                titulo = input("Título: ")
                genero = input("Género: ")

                try:

                    duracion = int(input("Duración: "))
                    clasificacion = input("Clasificación (A/B/C): ")
                    idioma = input("Idioma: ")
                    es3d_txt = input("¿Es 3D? (s/n): ")

                    precio = int(input("Precio: "))
                    cupos = int(input("Cupos: "))

                except ValueError:
                    print("Datos numéricos inválidos")
                    continue

                if not validar_codigo(codigo):
                    print("Código inválido")
                    continue

                if not validar_texto(titulo):
                    print("Título inválido")
                    continue

                if not validar_texto(genero):
                    print("Género inválido")
                    continue

                if not validar_duracion(duracion):
                    print("Duración inválida")
                    continue

                if not validar_clasificacion(clasificacion):
                    print("Clasificación inválida")
                    continue

                if not validar_idioma(idioma):
                    print("Idioma inválido")
                    continue

                if not validar_es3d(es3d_txt):
                    print("Valor 3D inválido")
                    continue

                if not validar_precio(precio):
                    print("Precio inválido")
                    continue

                if not validar_cupos(cupos):
                    print("Cupos inválidos")
                    continue

                es3d = es3d_txt.lower() == "s"

                if agregar_pelicula(
                        codigo, titulo, genero,
                        duracion, clasificacion,
                        idioma, es3d,
                        precio, cupos):

                    print("Película agregada")

                else:
                    print("El código ya existe")

            elif opcion == 5:

                codigo = input("Ingrese código: ").upper()

                if eliminar_pelicula(codigo):
                    print("Película eliminada")
                else:
                    print("El código no existe")

            elif opcion == 6:

                print("Programa finalizado.")
                break

            else:
                print("Opción inválida")

        except ValueError:

            print("Debe ingresar un número entero")


cine()