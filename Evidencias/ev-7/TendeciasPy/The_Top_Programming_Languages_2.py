import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF

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

# Guardar la gráfica de participación como imagen
plt.savefig("share_bar_chart.png")

# Crear gráfico de regresión lineal
x = np.arange(len(ides))  # Índices de los IDEs
coeffs = np.polyfit(x, share, 1)  # Coeficientes de la línea de regresión
line = np.poly1d(coeffs)  # Ecuación de la línea de regresión

plt.figure(figsize=(14, 8))
plt.scatter(x, share, color='blue', label='Datos reales', zorder=3)  # Puntos reales
plt.plot(x, line(x), color='red', linestyle='--', label=f'Regresión lineal\n(y = {coeffs[0]:.3f}x + {coeffs[1]:.3f})')  # Línea de regresión

# Configuración del gráfico de regresión
plt.xticks(x, ides, rotation=45, ha='right', fontsize=10)
plt.xlabel('IDEs')
plt.ylabel('Participación (%)')
plt.title('Regresión Lineal de Participación de IDEs')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Guardar el gráfico de regresión como imagen
plt.savefig("regression_line_plot.png")

# Crear el documento PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Título
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, txt="Análisis de Participación y Regresión Lineal de IDEs", ln=True, align='C')

# Agregar la gráfica de participación como imagen al PDF
pdf.ln(10)
pdf.image("share_bar_chart.png", x=10, y=30, w=180)

# Agregar el gráfico de regresión lineal como imagen al PDF
pdf.ln(100)
pdf.image("regression_line_plot.png", x=10, y=30, w=180)

# Hipótesis
pdf.ln(190)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, txt="""Hipótesis:

1. Hipótesis nula (H0): No hay correlación entre la participación de los IDEs y su popularidad. Esto significa que los cambios en la participación no están relacionados con la popularidad de los IDEs.

2. Hipótesis alternativa (H1): Existe una correlación entre la participación de los IDEs y su popularidad. Esto implica que a medida que la participación cambia, la popularidad de los IDEs también tiende a cambiar de manera significativa.
""")

# Conclusión
pdf.ln(10)
pdf.multi_cell(0, 10, txt="""Conclusión:

Después de ejecutar el código y observar el coeficiente de regresión, si el coeficiente es significativamente diferente de cero, se puede concluir que existe una relación entre la participación de los IDEs y su popularidad.
""")

# Guardar el PDF
pdf_output = "ides_participation_analysis_report.pdf"
pdf.output(pdf_output)

print(f"El análisis ha sido guardado en: {pdf_output}")
