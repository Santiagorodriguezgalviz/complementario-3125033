import numpy as np
import matplotlib.pyplot as plt

# Datos extraídos
languages = [
    "Python", "Java", "JavaScript", "C++", 
    "TypeScript", "SQL", "C#", "Go", 
    "C", "HTML", "Rust", "Mathematica", 
    "PHP", "Shell", "Lua", "SAS"
]

# Valores de popularidad en formato numérico
popularity = np.array([
    1, 0.4855, 0.4451, 0.3749, 
    0.2497, 0.2258, 0.2089, 0.2052, 
    0.1989, 0.1817, 0.1506, 0.1275, 
    0.1196, 0.117, 0.1041, 0.0855
])

# Crear la gráfica de popularidad
plt.figure(figsize=(12, 8))
plt.barh(languages, popularity, color='skyblue')
plt.xlabel('Popularidad')
plt.title('Popularidad de Lenguajes de Programación')
plt.gca().invert_yaxis()  # Invertir el eje y para mostrar el lenguaje más popular en la parte superior
plt.grid(axis='x')
plt.tight_layout()
plt.show()

# Crear gráfico de regresión lineal
x = np.arange(len(languages))  # Índices de los lenguajes
coeffs = np.polyfit(x, popularity, 1)  # Coeficientes de la línea de regresión
line = np.poly1d(coeffs)  # Ecuación de la línea de regresión

plt.figure(figsize=(14, 8))
plt.scatter(x, popularity, color='blue', label='Datos reales', zorder=3)  # Puntos reales
plt.plot(x, line(x), color='red', linestyle='--', label=f'Regresión lineal\n(y = {coeffs[0]:.3f}x + {coeffs[1]:.3f})')  # Línea de regresión

# Configuración del gráfico
plt.xticks(x, languages, rotation=45, ha='right', fontsize=10)
plt.xlabel('Lenguajes de Programación')
plt.ylabel('Popularidad')
plt.title('Regresión Lineal de Popularidad de Lenguajes de Programación')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

# Mostrar ecuación de la línea
print(f"Ecuación de la línea: y = {coeffs[0]:.3f}x + {coeffs[1]:.3f}")
