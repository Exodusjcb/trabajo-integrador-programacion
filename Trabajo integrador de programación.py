# Integrador de Programación - Gestión de datos de países
# Autor: Julián García
# Descripción: Programa para cargar, modificar, buscar, filtrar, ordenar y mostrar estadísticas.

import csv


# Carga de datos ---
def cargar_datos_csv(ruta_archivo):
    """Lee el CSV y devuelve una lista de diccionarios con los datos limpios."""
    lista_paises = []
    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip(),
                    }
                    lista_paises.append(pais)
                except (ValueError, KeyError):
                    continue
    except FileNotFoundError:
        print(" Archivo 'paises.csv' no encontrado. Se iniciará vacío.")
    return lista_paises


def guardar_datos_csv(ruta_archivo, lista_paises):
    """Guarda la lista de países actualizada en el archivo CSV."""
    try:
        with open(ruta_archivo, mode="w", encoding="utf-8", newline="") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for pais in lista_paises:
                escritor.writerow(pais)
    except Exception as e:
        print(f" Error al guardar el archivo: {e}")


# Funciones del menú.
# 1. Agregar país.


def agregar_pais(lista_paises):
    """Módulo interactivo para dar de alta un nuevo país con validación estricta."""
    print("\n--- Registrar Nuevo País ---")

    # Validación del Nombre del País
    while True:
        nombre = input("Nombre del país: ").strip()
        if not nombre:
            print(" El nombre no puede estar vacío.")
            continue

        # Filtro de seguridad: evita números y caracteres especiales
        if not nombre.replace(" ", "").isalpha():
            print(" El nombre del país debe contener únicamente letras.")
            continue

        if any(p["nombre"].lower() == nombre.lower() for p in lista_paises):
            print(" Ese país ya está registrado.")
            continue
        break

    # Validación de Población
    while True:
        try:
            poblacion = int(input("Población (entero positivo): "))
            if poblacion < 0:
                raise ValueError
            break
        except ValueError:
            print(" Ingrese un número entero válido.")

    # Validación de Superficie
    while True:
        try:
            superficie = int(input("Superficie en km² (entero positivo): "))
            if superficie < 0:
                raise ValueError
            break
        except ValueError:
            print(" Ingrese un número entero válido.")

    # Selección de Continente con menú numérico.
    print("\nSeleccione el continente:")
    print("1. América")
    print("2. Asia")
    print("3. Europa")
    print("4. Oceanía")
    print("5. África")
    print("6. Antártida")

    while True:
        opcion_cont = input("Seleccione una opción (1-6): ").strip()

        if opcion_cont == "1":
            continente = "América"
            break
        elif opcion_cont == "2":
            continente = "Asia"
            break
        elif opcion_cont == "3":
            continente = "Europa"
            break
        elif opcion_cont == "4":
            continente = "Oceanía"
            break
        elif opcion_cont == "5":
            continente = "África"
            break
        elif opcion_cont == "6":
            continente = "Antártida"
            break
        else:
            print(" Opción inválida. Ingrese un número del 1 al 6.")

    # Guardado.
    lista_paises.append(
        {
            "nombre": nombre.title(),
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente,
        }
    )
    print(f" ¡{nombre.title()} registrado con éxito!")


# 2. Actualizar datos de población y superficie de un país.
def actualizar_pais(lista_paises):
    """Actualiza población y superficie de un país existente."""
    print("\n---  Actualizar datos de un país ---")
    if not lista_paises:
        print(" No hay países registrados.")
        return

    nombre_buscar = input("Ingrese el nombre del país a modificar: ").strip().lower()

    encontrado = None
    for p in lista_paises:
        if p["nombre"].lower() == nombre_buscar:
            encontrado = p
            break

    if not encontrado:
        print(" No se encontró el país especificado.")
        return

    print(f"Modificando datos para: {encontrado['nombre']}")
    while True:
        try:
            encontrado["poblacion"] = int(
                input(f"Nueva población (Actual: {encontrado['poblacion']}): ")
            )
            if encontrado["poblacion"] < 0:
                raise ValueError
            break
        except ValueError:
            print(" Ingrese un número entero válido.")

    while True:
        try:
            encontrado["superficie"] = int(
                input(f"Nueva superficie en km² (Actual: {encontrado['superficie']}): ")
            )
            if encontrado["superficie"] < 0:
                raise ValueError
            break
        except ValueError:
            print(" Ingrese un número entero válido.")

    print(f" ¡Datos de {encontrado['nombre']} actualizados correctamente!")


# 3. Búsqueda de pais por nombre.
def buscar_por_nombre(lista_paises):
    """Busca países mediante coincidencia parcial o exacta."""
    print("\n---  Buscar país ---")
    busqueda = input("Ingrese el nombre (o parte de él): ").strip().lower()

    resultados = [p for p in lista_paises if busqueda in p["nombre"].lower()]

    if not resultados:
        print(" No se encontraron países que coincidan con la búsqueda.")
    else:
        print(f"\nResultados encontrados ({len(resultados)}):")
        for p in resultados:
            print(
                f" {p['nombre']} | Pob: {p['poblacion']} | Sup: {p['superficie']} km² | Cont: {p['continente']}"
            )


# 4. Filtrar países por continente, población o superficie.
def filtrar_paises(lista_paises):
    """Submenú interactivo para filtrar la lista de países."""
    print("\n--- Filtrar países ---")
    print("1. Por Continente")
    print("2. Por Rango de Población")
    print("3. Por Rango de Superficie")
    opc = input("Seleccione opción de filtrado: ").strip()

    resultados = []

    if opc == "1":
        # CAMBIO CLAVE: Menú numérico idéntico para evitar errores de tipeo y acentos
        print("\nSeleccione el continente a filtrar:")
        print("1. América")
        print("2. Asia")
        print("3. Europa")
        print("4. Oceanía")
        print("5. África")
        print("6. Antártida")

        opcion_cont = input("Seleccione una opción (1-6): ").strip()

        if opcion_cont == "1":
            cont_buscar = "América"
        elif opcion_cont == "2":
            cont_buscar = "Asia"
        elif opcion_cont == "3":
            cont_buscar = "Europa"
        elif opcion_cont == "4":
            cont_buscar = "Oceanía"
        elif opcion_cont == "5":
            cont_buscar = "África"
        elif opcion_cont == "6":
            cont_buscar = "Antártida"
        else:
            print(" Opción de continente incorrecta.")
            return

        # Filtra buscando la coincidencia exacta con mayúscula y tilde oficiales
        resultados = [p for p in lista_paises if p["continente"] == cont_buscar]

    elif opc == "2":
        try:
            min_pob = int(input("Población mínima: "))
            max_pob = int(input("Población máxima: "))
            resultados = [
                p for p in lista_paises if min_pob <= p["poblacion"] <= max_pob
            ]
        except ValueError:
            print(" Rangos inválidos.")
            return

    elif opc == "3":
        try:
            min_sup = int(input("Superficie mínima: "))
            max_sup = int(input("Superficie máxima: "))
            resultados = [
                p for p in lista_paises if min_sup <= p["superficie"] <= max_sup
            ]
        except ValueError:
            print(" Rangos inválidos.")
            return
    else:
        print(" Opción de filtro incorrecta.")
        return

    # Muestra los resultados obtenidos
    if not resultados:
        print(" No hay países que cumplan con los criterios del filtro.")
    else:
        print(f"\n--- Resultados del Filtro ({len(resultados)} encontrados) ---")
        for p in resultados:
            print(
                f"• {p['nombre']} ({p['continente']}) - Pob: {p['poblacion']} - Sup: {p['superficie']} km²"
            )


# 5. Ordenar paises.
def ordenar_paises(lista_paises):
    """Ordena la lista clonada según el criterio elegido."""
    if not lista_paises:
        print(" No hay datos para ordenar.")
        return

    print("\n---  Ordenar países ---")
    print("Criterios: 1. Nombre | 2. Población | 3. Superficie")
    criterio_opc = input("Seleccione criterio: ").strip()
    sentido = input("¿Sentido? (A: Ascendente / D: Descendente): ").strip().upper()

    llave = "nombre"
    if criterio_opc == "2":
        llave = "poblacion"
    elif criterio_opc == "3":
        llave = "superficie"

    copia = list(lista_paises)
    n = len(copia)

    for i in range(n):
        for j in range(0, n - i - 1):
            val1 = copia[j][llave]
            val2 = copia[j + 1][llave]

            if isinstance(val1, str):
                val1, val2 = val1.lower(), val2.lower()

            condicion = val1 > val2 if sentido == "A" else val1 < val2
            if condicion:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]

    print("\n---  Lista ordenada ---")
    for p in copia:
        print(
            f"• {p['nombre']} | {llave.capitalize()}: {p[llave]} | Cont: {p['continente']}"
        )


# 6. Estadísticas.
def mostrar_estadisticas(lista_paises):
    """Calcula y muestra métricas clave del dataset."""
    if not lista_paises:
        print(" No hay países cargados para generar estadísticas.")
        return

    print("\n---  Estadisticas de dataset ---")

    max_pob = lista_paises[0]
    min_pob = lista_paises[0]
    suma_pob = 0
    suma_sup = 0
    por_continente = {}

    for p in lista_paises:
        suma_pob += p["poblacion"]
        suma_sup += p["superficie"]

        if p["poblacion"] > max_pob["poblacion"]:
            max_pob = p
        if p["poblacion"] < min_pob["poblacion"]:
            min_pob = p

        cont = p["continente"]
        por_continente[cont] = por_continente.get(cont, 0) + 1

    cant = len(lista_paises)
    print(f" Mayor Población: {max_pob['nombre']} ({max_pob['poblacion']} hab.)")
    print(f" Menor Población: {min_pob['nombre']} ({min_pob['poblacion']} hab.)")
    print(f" Promedio de Población: {suma_pob / cant:.2f} habitantes")
    print(f" Promedio de Superficie: {suma_sup / cant:.2f} km²")
    print("\n Cantidad de países por continente:")
    for c, q in por_continente.items():
        print(f" - {c}: {q}")


# Menú principal.
def menu():
    ruta = "paises.csv"
    lista_paises = cargar_datos_csv(ruta)

    while True:
        print("\n==================================")
        print("     Gestión de datos de países.       ")
        print("==================================")
        print("1. Agregar país")
        print("2. Actualizar población/superficie")
        print("3. Buscar país por nombre")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Guardar y Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_pais(lista_paises)
        elif opcion == "2":
            actualizar_pais(lista_paises)
        elif opcion == "3":
            buscar_por_nombre(lista_paises)
        elif opcion == "4":
            filtrar_paises(lista_paises)
        elif opcion == "5":
            ordenar_paises(lista_paises)
        elif opcion == "6":
            mostrar_estadisticas(lista_paises)
        elif opcion == "7":
            print("\n Guardando cambios en 'paises.csv'...")
            guardar_datos_csv(ruta, lista_paises)
            break
        else:
            print(" Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
