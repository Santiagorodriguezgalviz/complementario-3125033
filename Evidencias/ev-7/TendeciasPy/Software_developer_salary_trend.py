import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF

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

# Guardar la gráfica de porcentajes como imagen
plt.savefig("percentage_bar_chart.png")

# Crear gráfico de regresión lineal
x = np.arange(len(languages))  # Índices de los lenguajes
coeffs = np.polyfit(x, percentages, 1)  # Coeficientes de la línea de regresión
line = np.poly1d(coeffs)  # Ecuación de la línea de regresión

plt.figure(figsize=(14, 8))
plt.scatter(x, percentages, color='blue', label='Datos reales', zorder=3)  # Puntos reales
plt.plot(x, line(x), color='red', linestyle='--', label=f'Regresión lineal\n(y = {coeffs[0]:.3f}x + {coeffs[1]:.3f})')  # Línea de regresión

# Configuración del gráfico de regresión
plt.xticks(x, languages, rotation=45, ha='right', fontsize=10)
plt.xlabel('Lenguajes de Programación')
plt.ylabel('Porcentaje (%)')
plt.title('Regresión Lineal de Porcentaje de Lenguajes de Programación')
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
pdf.cell(200, 10, txt="Análisis de Porcentajes y Regresión Lineal de Lenguajes de Programación", ln=True, align='C')

# Agregar la gráfica de porcentajes como imagen al PDF
pdf.ln(10)
pdf.image("percentage_bar_chart.png", x=10, y=30, w=180)

# Agregar el gráfico de regresión lineal como imagen al PDF
pdf.ln(100)
pdf.image("regression_line_plot.png", x=10, y=30, w=180)

# Hipótesis
pdf.ln(190)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, txt="""Hipótesis:

1. Hipótesis nula (H0): No hay correlación entre los porcentajes de los lenguajes de programación. Esto significa que los porcentajes no están relacionados entre sí.

2. Hipótesis alternativa (H1): Existe una correlación entre los porcentajes de los lenguajes de programación. Esto implica que a medida que los porcentajes de un lenguaje cambian, los porcentajes de otros lenguajes también tienden a cambiar de manera significativa.
""")

# Conclusión
pdf.ln(10)
pdf.multi_cell(0, 10, txt="""Conclusión:

Después de ejecutar el código y observar el coeficiente de correlación, se podrá aceptar o rechazar la hipótesis nula. Si el coeficiente es significativamente diferente de cero, se puede concluir que hay una relación entre los porcentajes de los lenguajes de programación, lo que podría indicar que los lenguajes más populares tienden a tener porcentajes más altos en comparación con otros.
""")

# Guardar el PDF
pdf_output = "language_percentage_analysis_report.pdf"
pdf.output(pdf_output)

print(f"El análisis ha sido guardado en: {pdf_output}")
