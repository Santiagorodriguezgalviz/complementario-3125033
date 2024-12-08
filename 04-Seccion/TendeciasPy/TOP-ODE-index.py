import numpy as np
import matplotlib.pyplot as plt

# Datos extraídos
online_ides = [
    "JSFiddle", "PythonAnywhere", "Codio", "Koding", 
    "DartPad", "Cloud9 AWS", "Ideone", "Repl.it", 
    "Goorm", "Codeanywhere", "Cloud9 IDE", "Python Fiddle", 
    "Online PHP IDE", "SourceLair", "Codiad", "Codenvy", 
    "Orion IDE", "IceCoder", "ShiftEdit", "Nitrous.io", 
    "CodePicnic"
]

# Participación en porcentaje
share = np.array([
    21.2, 19.29, 16.71, 15.2, 
    10.07, 5.52, 4.46, 3.78, 
    1.56, 1.2, 0.36, 0.3, 
    0.25, 0.03, 0.01, 0.01, 
    0.01, 0.0, 0.0, 0.0, 
    0.0
])

# Crear la gráfica de participación
plt.figure(figsize=(12, 8))
plt.barh(online_ides, share, color='skyblue')
plt.xlabel('Participación (%)')
plt.title('Participación de IDEs en Línea en el Mercado')
plt.gca().invert_yaxis()  # Invertir el eje y para mostrar el IDE más popular en la parte superior
plt.grid(axis='x')
plt.tight_layout()
plt.show()

# Crear gráfico de regresión lineal
x = np.arange(len(online_ides))  # Índices de los IDEs
coeffs = np.polyfit(x, share, 1)  # Coeficientes de la línea de regresión
line = np.poly1d(coeffs)  # Ecuación de la línea de regresión

plt.figure(figsize=(14, 8))
plt.scatter(x, share, color='blue', label='Datos reales', zorder=3)  # Puntos reales
plt.plot(x, line(x), color='red', linestyle='--', label=f'Regresión lineal\n(y = {coeffs[0]:.3f}x + {coeffs[1]:.3f})')  # Línea de regresión

# Configuración del gráfico
plt.xticks(x, online_ides, rotation=45, ha='right', fontsize=10)
plt.xlabel('IDEs en Línea')
plt.ylabel('Participación (%)')
plt.title('Regresión Lineal de Participación de IDEs en Línea')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

# Mostrar ecuación de la línea
print(f"Ecuación de la línea: y = {coeffs[0]:.3f}x + {coeffs[1]:.3f}")
