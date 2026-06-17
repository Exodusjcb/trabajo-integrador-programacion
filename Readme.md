# Trabajo integrador de programación -UTN

Este proyecto es una aplicación de consola interactiva desarrollada en Python para la administración, filtrado, ordenamiento y análisis estadístico de un dataset de países almacenado en formato CSV. El desarrollo cumple estrictamente con los requerimientos técnicos fijados por la cátedra para el Trabajo Práctico Integrador (TPI) de la Tecnicatura Universitaria en Programación (TUP).

*Alumno:** Julián García

# Funcionalidades Principales.

El sistema ofrece una interfaz interactiva parametrizada en consola con las siguientes capacidades:
1. **Gestión de Datos (Alta robusta):** Registro de nuevos países con validación estricta de formatos (evita ingresos alfabéticos erróneos o campos vacíos).
2. **Menú de Continentes:** Mapeo y normalización automática de datos mediante una interfaz enumerada (1-6) para garantizar la consistencia de caracteres y acentos en el dataset.
3. **Actualización Directa:** Modificación de población y superficie de registros existentes en la base de datos.
4. **Búsqueda Flexible:** Localización de países por coincidencia exacta o parcial de nombres.
5. **Filtros Avanzados Sincronizados:** Segmentación multivariable por catálogo numérico de continentes y rangos numéricos de población/superficie.
6. **Módulo Estadístico Global:** Cálculo automatizado de promedios, máximos/mínimos generales y recuento de países agrupados por continente.
7. **Persistencia Externa:** Lectura y escritura automatizada mediante el módulo nativo `csv` para resguardar los cambios en el almacenamiento secundario.

# 🛠️ Instrucciones de Uso y Ejecución

# Requisitos Previos
*   Tener instalado Python 3.x en el sistema operativo.
*   Mantener el archivo `paises.csv` en la misma raíz que el script principal.

### Ejecución
Para iniciar la aplicación, abra una terminal en el directorio del proyecto y ejecute:
```bash
python main.py
```

### Ejemplo de Interacción (Carga Normalizada y Blindada)
```text
=== MENÚ DE OPCIONES ===
1. Agregar País
2. Actualizar Datos
...
Seleccione una opción: 1

Nombre del país: argentina123
 [ERROR] El nombre del país debe contener únicamente letras.

Nombre del país: argentina
Población (entero positivo): 45000000
Superficie en km² (entero positivo): 2780400

Seleccione el continente:
1. América
2. Asia
3. Europa
4. Oceanía
5. África
6. Antártida
Seleccione una opción (1-6): 1

 ¡Argentina registrado con éxito! (Texto normalizado con formato .title())
```

---

## 🎥 Enlace a la Video Demostración
El video explicativo del funcionamiento del código, la arquitectura de la lista de diccionarios y los flujos del sistema se encuentra disponible en el siguiente enlace público:
👉 **https://youtu.be/ylbFB448VNw**

---

## 📄 Documentación y Fuentes Oficiales
El informe teórico-técnico con el marco conceptual, decisiones de diseño de software y diagramas de flujo está adjunto directamente en la raíz de este proyecto (`Informe_TPI_Prog1_Garcia.pdf`). Para el desarrollo se consultaron los siguientes recursos institucionales:

*   **Cátedra de Programación I - UTN.** *Unidad 7: Estructuras de Datos Complejos*. SIED UTN. [https://utn.edu.ar](https://utn.edu.ar)
*   **GitHub Docs.** *About READMEs and managing repositories*. [https://github.com](https://github.com)
*   **Píldoras Informáticas.** *Manejo de Archivos y Estructuras de Datos Tabulares (CSV) en Python*. [https://youtube.com](https://youtube.com)
*   **Python Software Foundation.** *Built-in Types (Sets, Lists, Dictionaries)*. [https://python.org](https://python.org)
*   **Wikipedia.** *Anexo:Países y territorios dependientes por población*. [https://wikipedia.org](https://wikipedia.org)
