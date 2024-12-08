import numpy as np
import matplotlib.pyplot as plt

# Datos extraídos
languages = [
    "Scala", "Go", "Kotlin", "C++", "Rust",
    "C", "Shell scripting", "Java", "Python",
    "SQL", "Swift", "Dart", "TypeScript",
    "JavaScript", "C#", "PHP", "HTML/CSS"
]

# Porcentajes en formato numérico
percentages = np.array([
    60, 50, 41, 40, 40,
    38, 38, 37, 36,
    33, 32, 32, 32,
    28, 28, 25, 24
])

# Crear la gráfica de porcentajes
plt.figure(figsize=(12, 8))
plt.barh(languages, percentages, color='lightcoral')
plt.xlabel('Porcentaje (%)')
plt.title('Porcentaje de Lenguajes de Programación')
plt.gca().invert_yaxis()  # Invertir el eje y para mostrar el lenguaje más popular en la parte superior
plt.grid(axis='x')
plt.tight_layout()
plt.show()

# Crear gráfico de regresión lineal
x = np.arange(len(languages))  # Índices de los lenguajes
coeffs = np.polyfit(x, percentages, 1)  # Coeficientes de la línea de regresión
line = np.poly1d(coeffs)  # Ecuación de la línea de regresión

plt.figure(figsize=(14, 8))
plt.scatter(x, percentages, color='blue', label='Datos reales', zorder=3)  # Puntos reales
plt.plot(x, line(x), color='red', linestyle='--', label=f'Regresión lineal\n(y = {coeffs[0]:.3f}x + {coeffs[1]:.3f})')  # Línea de regresión

# Configuración del gráfico
plt.xticks(x, languages, rotation=45, ha='right', fontsize=10)
plt.xlabel('Lenguajes de Programación')
plt.ylabel('Porcentaje (%)')
plt.title('Regresión Lineal de Porcentaje de Lenguajes de Programación')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

# Mostrar ecuación de la línea
print(f"Ecuación de la línea: y = {coeffs[0]:.3f}x + {coeffs[1]:.3f}")
