import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF

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

# Crear el gráfico
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

# Guardar el gráfico como imagen
plt.savefig("trend_analysis_plot.png")

# Crear el documento PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Título
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, txt="Análisis de Tendencias de Lenguajes de Programación", ln=True, align='C')

# Agregar el gráfico como imagen al PDF
pdf.ln(10)
pdf.image("trend_analysis_plot.png", x=10, y=30, w=180)

# Hipótesis
pdf.ln(120)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, txt="""Hipótesis:

1. Hipótesis nula (H0): No hay correlación entre la participación de los lenguajes de programación y sus cambios de tendencia en el último año. Esto significa que los cambios en la participación no están relacionados con las tendencias de cambio.

2. Hipótesis alternativa (H1): Existe una correlación entre la participación de los lenguajes de programación y sus cambios de tendencia en el último año. Esto implica que a medida que la participación cambia, las tendencias de cambio también tienden a cambiar de manera significativa.
""")

# Conclusión
pdf.ln(10)
pdf.multi_cell(0, 10, txt="""Conclusión:

Después de ejecutar el código y observar los coeficientes de correlación, se podrá aceptar o rechazar la hipótesis nula. Si los coeficientes son significativamente diferentes de cero, se puede concluir que hay una relación entre la participación de los lenguajes de programación y sus cambios de tendencia, lo que podría indicar que los lenguajes más populares tienden a tener tendencias más positivas o negativas en su participación.
""")

# Guardar el PDF
pdf_output = "trend_analysis_report.pdf"
pdf.output(pdf_output)

print(f"El análisis ha sido guardado en: {pdf_output}")
