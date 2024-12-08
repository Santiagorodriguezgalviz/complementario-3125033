import numpy as np
import matplotlib.pyplot as plt

# Datos de cambio de rating
programming_languages = [
    "Python", "C++", "Java", "C", "C#",
    "JavaScript", "Visual Basic", "Go", "SQL", "Fortran",
    "Delphi/Object Pascal", "MATLAB", "PHP", "Rust", "R",
    "Ruby", "Scratch", "Kotlin", "COBOL", "Swift"
]
changes = np.array([6.01, 0.09, -0.04, -2.38, -1.22, 0.62, 0.48, 1.16, 0.50, 0.49,
                    0.75, 0.28, -0.09, 0.35, 0.23, 0.18, 0.03, 0.20, 0.22, 0.09])

# Eje x como índices de los lenguajes
x = np.arange(len(programming_languages))

# Ajuste de regresión lineal
coeffs = np.polyfit(x, changes, 1)  # Coeficientes de la regresión lineal
line = np.poly1d(coeffs)  # Ecuación de la línea

# Crear el gráfico de regresión lineal
plt.figure(figsize=(12, 6))
plt.scatter(x, changes, color='blue', label='Datos reales', zorder=3)  # Puntos reales
plt.plot(x, line(x), color='red', linestyle='--', label=f'Regresión lineal\n(y = {coeffs[0]:.2f}x + {coeffs[1]:.2f})')  # Línea de regresión

# Configuración de la gráfica
plt.xticks(x, programming_languages, rotation=45, ha='right')
plt.xlabel('Lenguajes de Programación')
plt.ylabel('Cambio en el Rating (%)')
plt.title('Regresión Lineal de Cambios en el Rating (Sep 2024)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

# Mostrar la ecuación de la línea
print(f"Ecuación de la línea: y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}")
