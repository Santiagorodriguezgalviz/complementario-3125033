import numpy as np
import matplotlib.pyplot as plt

# Datos extraídos
ides = [
    "Visual Studio", "Visual Studio Code", "Eclipse", "PyCharm", 
    "Android Studio", "IntelliJ", "NetBeans", "Xcode", 
    "RStudio", "Sublime Text", "Atom", "Code::Blocks", 
    "Vim", "PhpStorm", "Qt Creator", "Komodo", 
    "Emacs", "Geany", "Xamarin", "JCreator", 
    "JDeveloper", "Light Table", "RAD Studio", "Eric Python", 
    "Monkey Studio", "RubyMine", "Aptana", "SharpDevelop", 
    "MonoDevelop", "DrJava", "Julia Studio", "SlickEdit", 
    "Zend Studio"
]

# Participación en porcentaje
share = np.array([
    27.57, 14.16, 11.89, 10.67, 
    9.89, 8.03, 3.81, 2.98, 
    2.77, 2.52, 2.08, 1.4, 
    0.87, 0.38, 0.3, 0.18, 
    0.18, 0.15, 0.11, 0.02, 
    0.02, 0.02, 0.0, 0.0, 
    0.0, 0.0, 0.0, 0.0, 
    0.0, 0.0, 0.0, 0.0, 
    0.0
])

# Crear la gráfica de participación
plt.figure(figsize=(12, 8))
plt.barh(ides, share, color='lightcoral')
plt.xlabel('Participación (%)')
plt.title('Participación de IDEs en el Mercado')
plt.gca().invert_yaxis()  # Invertir el eje y para mostrar el IDE más popular en la parte superior
plt.grid(axis='x')
plt.tight_layout()
plt.show()

# Crear gráfico de regresión lineal
x = np.arange(len(ides))  # Índices de los IDEs
coeffs = np.polyfit(x, share, 1)  # Coeficientes de la línea de regresión
line = np.poly1d(coeffs)  # Ecuación de la línea de regresión

plt.figure(figsize=(14, 8))
plt.scatter(x, share, color='blue', label='Datos reales', zorder=3)  # Puntos reales
plt.plot(x, line(x), color='red', linestyle='--', label=f'Regresión lineal\n(y = {coeffs[0]:.3f}x + {coeffs[1]:.3f})')  # Línea de regresión

# Configuración del gráfico
plt.xticks(x, ides, rotation=45, ha='right', fontsize=10)
plt.xlabel('IDEs')
plt.ylabel('Participación (%)')
plt.title('Regresión Lineal de Participación de IDEs')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

# Mostrar ecuación de la línea
print(f"Ecuación de la línea: y = {coeffs[0]:.3f}x + {coeffs[1]:.3f}")
