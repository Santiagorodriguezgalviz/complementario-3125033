import numpy as np
import matplotlib.pyplot as plt

# Datos extraídos
languages = [
    "JavaScript", "Python", "HTML/CSS", "SQL", "Java",
    "Shell", "TypeScript", "C++", "C#", "C",
    "PHP", "Go", "Kotlin", "Rust", "Swift",
    "Ruby", "Scala", "Objective-C"
]

# Porcentajes por año
data = np.array([
    [65, 64, 69, 70, 69, 65, 61, 63],  # JavaScript
    [32, 41, 49, 55, 52, 53, 54, 56],  # Python
    [60, 55, 61, 61, 60, 54, 52, 51],  # HTML/CSS
    [42, 47, 56, 56, 54, 49, 52, 53],  # SQL
    [47, 51, 50, 54, 49, 48, 49, 48],  # Java
    [29, 40, 39, 37, 34, 34, 35, 36],  # Shell
    [12, 17, 25, 28, 29, 34, 34, 37],  # TypeScript
    [17, 18, 20, 27, 23, 25, 24, 25],  # C++
    [20, 22, 24, 22, 21, 20, 21, 22],  # C#
    [15, 16, 17, 23, 19, 20, 19, 20],  # C
    [30, 26, 29, 27, 32, 20, 18, 17],  # PHP
    [8, 12, 18, 19, 17, 17, 17, 19],   # Go
    [2, 9, 16, 15, 14, 16, 15, 17],    # Kotlin
    [0, 2, 5, 7, 6, 9, 10, 12],        # Rust
    [9, 8, 11, 9, 8, 7, 6, 6],         # Swift
    [10, 8, 11, 8, 6, 6, 6, 5],        # Ruby
    [7, 5, 6, 5, 4, 3, 3, 3],          # Scala
    [7, 4, 5, 4, 3, 2, 2, 1]           # Objective-C
])

years = np.array([2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])

# Crear la gráfica con líneas de regresión
plt.figure(figsize=(16, 10))

# Paleta de colores más suave
colors = plt.cm.tab20(np.linspace(0, 1, len(languages)))

for i, language in enumerate(languages):
    # Datos originales
    plt.scatter(years, data[i], color=colors[i], alpha=0.7, label=f'{language} (Datos)')
    
    # Línea de regresión lineal
    coeffs = np.polyfit(years, data[i], 1)
    line = np.poly1d(coeffs)
    plt.plot(years, line(years), color=colors[i], linestyle='--', 
             label=f'{language} (Tendencia lineal)')

# Títulos y etiquetas
plt.title('Tendencia de Adopción de Lenguajes de Programación (2017-2024)\nAnálisis de Regresión Lineal', fontsize=15)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Porcentaje de Adopción', fontsize=12)
plt.xticks(years, rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()