# Universidad Nacional Abierta y a Distancia - UNAD 
# Curso: Fundamentos de Programación - Código 213022 
# Actividad: Fase 5 - Evaluación Final POA 
# Problema N.º 3: Auditoría de Inventario y Reposición
# Estudiante: Danilo Bolaño Sierra

# Definición de Funciones
def calcular_cantidad_pedir(stock_actual, stock_minimo):
    """
    Función diseñada para calcular cuántas unidades se deben solicitar 
    de un artículo determinado, basándose en los niveles de inventario.
    
    Parámetros:
        stock_actual (int): Cantidad de unidades disponibles en este momento.
        stock_minimo (int): Cantidad mínima de unidades que se requieren tener.
        
    Retorna:
        int: Cantidad de unidades que deben pedirse para completar el inventario.
    """

    # Estructura de control condicional para evaluar la condición del inventario
    if stock_actual < stock_minimo:
        # Caso 1: Hay menos cantidad de la necesaria -> Se calcula cuánto falta
        cantidad_necesaria = stock_minimo - stock_actual
    else:
        # Caso 2: Hay cantidad suficiente o excedente -> No se necesita pedir nada
        cantidad_necesaria = 0

    return cantidad_necesaria


# Datos de Entrada

# Matriz bidimensional que almacena la información de los artículos.
# Estructura de cada fila:
# [Código, Nombre del Artículo, Stock Actual, Stock Mínimo]

inventario = [
    ["ART-001", "Tornillos de acero 1/4 pulgada", 45, 50],
    ["ART-002", "Tuercas hexagonales", 120, 60],
    ["ART-003", "Arandelas planas galvanizadas", 15, 30],
    ["ART-004", "Clavos de acero de 2 pulgadas", 80, 75],
    ["ART-005", "Pijas para madera cabeza plana", 22, 40]
]


# Procesamiento y Salida

# Impresión del encabezado del informe
print("==================================================")
print("=== INFORME DE AUDITORÍA Y REPOSICIÓN DE INVENTARIO ===")
print("==================================================")

print(f"{'Artículo':<35} {'Cantidad a pedir':>15}")
print("-" * 50)

# Estructura de repetición:
# Recorre cada elemento (fila) contenido en la matriz

for articulo in inventario:

    # Extracción de datos individuales de la fila actual para mayor claridad
    codigo = articulo[0]
    nombre_articulo = articulo[1]
    cantidad_actual = articulo[2]
    cantidad_minima = articulo[3]

    # Llamado a la función definida anteriormente
    resultado_calculo = calcular_cantidad_pedir(
        cantidad_actual,
        cantidad_minima
    )

    # Impresión formateada de los resultados al usuario
    print(f"{nombre_articulo:<35} {resultado_calculo:>15} unidades")

# Pie de página del informe
print("-" * 50)
print("=== Fin del proceso de auditoría ===")