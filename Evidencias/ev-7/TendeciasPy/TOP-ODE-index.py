import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF

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

# Guardar la gráfica de participación como imagen
plt.savefig("share_bar_chart.png")

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

# Guardar el gráfico de regresión como imagen
plt.savefig("regression_line_plot.png")

# Crear el documento PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Título
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, txt="Análisis de Participación de IDEs en Línea y Regresión Lineal", ln=True, align='C')

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

1. Hipótesis nula (H0): No hay correlación entre la participación de los IDEs en línea y su popularidad. Esto significa que los cambios en la participación no están relacionados con la popularidad de los IDEs.

2. Hipótesis alternativa (H1): Existe una correlación entre la participación de los IDEs en línea y su popularidad. Esto implica que a medida que la participación cambia, la popularidad de los IDEs también tiende a cambiar de manera significativa.
""")

# Conclusión
pdf.ln(10)
pdf.multi_cell(0, 10, txt="""Conclusión:

Después de ejecutar el código y observar el coeficiente de correlación, se podrá aceptar o rechazar la hipótesis nula. Si el coeficiente es significativamente diferente de cero, se puede concluir que hay una relación entre la participación de los IDEs en línea y su popularidad, lo que podría indicar que los IDEs más populares tienden a tener una mayor participación en el mercado.
""")

# Guardar el PDF
pdf_output = "ide_participation_analysis_report.pdf"
pdf.output(pdf_output)

print(f"El análisis ha sido guardado en: {pdf_output}")
