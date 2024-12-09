import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF

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

# Guardar el gráfico en un archivo de imagen
plt.savefig("rating_change_plot.png")

# Crear el documento PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Título
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, txt="Análisis de Cambios en el Rating de Lenguajes de Programación", ln=True, align='C')

# Agregar el gráfico como una imagen al PDF
pdf.ln(10)
pdf.image("rating_change_plot.png", x=10, y=30, w=180)

# Hipótesis
pdf.ln(120)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, txt="""Hipótesis:

1. Hipótesis nula (H0): No hay correlación entre los ratings y los cambios en los ratings de los lenguajes de programación. Esto significa que los cambios en los ratings no están relacionados con los ratings actuales.

2. Hipótesis alternativa (H1): Existe una correlación entre los ratings y los cambios en los ratings de los lenguajes de programación. Esto implica que a medida que los ratings cambian, los ratings actuales también tienden a cambiar de manera significativa.
""")

# Conclusión
pdf.ln(10)
pdf.multi_cell(0, 10, txt="""Conclusión:

Después de ejecutar el código y observar el coeficiente de correlación, se podrá aceptar o rechazar la hipótesis nula. Si el coeficiente es significativamente diferente de cero, se puede concluir que hay una relación entre los ratings y los cambios en los ratings de los lenguajes de programación, lo que podría indicar que los lenguajes con mejores ratings tienden a experimentar cambios más positivos o negativos en sus ratings.
""")

# Guardar el PDF
pdf_output = "rating_change_analysis.pdf"
pdf.output(pdf_output)

print(f"El análisis ha sido guardado en: {pdf_output}")
