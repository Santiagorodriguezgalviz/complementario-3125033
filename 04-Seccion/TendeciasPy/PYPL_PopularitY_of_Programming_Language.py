import numpy as np
import matplotlib.pyplot as plt

# Datos extraídos
languages = [
    "Python", "Java", "JavaScript", "C#", "C/C++",
    "R", "PHP", "TypeScript", "Swift", "Rust",
    "Objective-C", "Go", "Kotlin", "Matlab", "Ruby",
    "VBA", "Powershell", "Ada", "Dart", "Lua",
    "Abap", "Scala", "Visual Basic", "Julia", "Groovy",
    "Cobol", "Perl", "Delphi/Pascal", "Haskell"
]

# Cambios de tendencia (último año)
trends = np.array([
    1.6, -0.2, -1.0, -0.1, -0.2,
    0.2, -0.5, 0.0, 0.0, 0.6,
    0.2, 0.2, 0.2, -0.1, -0.1,
    0.0, 0.1, -0.1, 0.0, 0.1,
    -0.0, -0.1, -0.1, -0.1, -0.1,
    -0.0, -0.2, -0.1, -0.2
])

# Crear gráfico de regresión lineal para tendencias
x = np.arange(len(languages))  # Índices de lenguajes
coeffs = np.polyfit(x, trends, 1)  # Coeficientes de regresión lineal
line = np.poly1d(coeffs)  # Ecuación de la línea de regresión

plt.figure(figsize=(14, 8))
plt.scatter(x, trends, color='blue', label='Datos reales', zorder=3)  # Puntos reales
plt.plot(x, line(x), color='red', linestyle='--', label=f'Regresión lineal\n(y = {coeffs[0]:.3f}x + {coeffs[1]:.3f})')  # Línea de regresión

# Configuración del gráfico
plt.xticks(x, languages, rotation=45, ha='right', fontsize=10)
plt.xlabel('Lenguajes de Programación')
plt.ylabel('Tendencia (%) en el Último Año')
plt.title('Regresión Lineal de Tendencias de Lenguajes de Programación (Último Año)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

# Mostrar ecuación de la línea
print(f"Ecuación de la línea: y = {coeffs[0]:.3f}x + {coeffs[1]:.3f}")
