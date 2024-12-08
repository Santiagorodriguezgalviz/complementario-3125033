import matplotlib.pyplot as plt
import numpy as np

# Datos
lenguajes = [
    "JavaScript", "Python", "HTML/CSS", "SQL", "Java", 
    "Shell", "TypeScript", "C++", "C#", "C", "PHP", "Go", 
    "Kotlin", "Rust", "Swift", "Ruby", "Scala", "Objective-C"
]

# Popularidad en diferentes años (2017 - 2023)
años = [2017, 2018, 2019, 2020, 2021, 2022, 2023]
popularidad = [
    [65, 64, 69, 70, 69, 65, 61],  # JavaScript
    [32, 41, 49, 55, 52, 53, 54],  # Python
    [60, 55, 61, 61, 60, 54, 52],  # HTML/CSS
    [42, 47, 56, 56, 54, 49, 52],  # SQL
    [47, 51, 50, 54, 49, 48, 49],  # Java
    [0, 29, 40, 39, 37, 34, 34],   # Shell
    [12, 17, 25, 28, 29, 34, 34],  # TypeScript
    [17, 18, 20, 27, 23, 25, 24],  # C++
    [20, 22, 24, 22, 21, 20, 21],  # C#
    [15, 16, 17, 23, 19, 20, 19],  # C
    [30, 26, 29, 27, 32, 20, 18],  # PHP
    [8, 12, 18, 19, 17, 17, 17],   # Go
    [2, 9, 16, 15, 14, 16, 15],    # Kotlin
    [0, 2, 5, 7, 6, 9, 10],        # Rust
    [9, 8, 11, 9, 8, 7, 6],        # Swift
    [10, 8, 11, 8, 6, 6, 6],       # Ruby
    [7, 5, 6, 5, 4, 3, 3],         # Scala
    [7, 4, 5, 4, 3, 2, 2]          # Objective-C
]

# Estilo simple y claro
plt.figure(figsize=(14, 10))  # Aumentamos el tamaño del gráfico

# Dibujar las líneas de popularidad
for i, lenguaje in enumerate(lenguajes):
    plt.plot(años, popularidad[i], marker='o', label=lenguaje, linewidth=2)

# Añadir título y etiquetas
plt.title('Evolución de Popularidad de Lenguajes de Programación (2017-2023)', fontsize=20, fontweight='bold')
plt.xlabel('Año', fontsize=16)
plt.ylabel('Popularidad (%)', fontsize=16)

# Mejorar las etiquetas del eje x
plt.xticks(años, rotation=0, fontsize=12)
plt.yticks(np.arange(0, 101, 10), fontsize=12)

# Añadir leyenda
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)

# Añadir cuadrícula
plt.grid(True, linestyle='--', alpha=0.6)

# Ajustar el diseño
plt.tight_layout()

# Mostrar la gráfica
plt.show()
