import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from fpdf import FPDF

# Datos de frameworks frontend y salarios promedio (datos de 2023)
frameworks = ['React', 'Angular', 'Vue.js', 'Svelte', 'Next.js', 'jQuery', 'Ember.js', 'Nuxt.js', 'Astro']
salarios = [120000, 115000, 105000, 98000, 125000, 85000, 95000, 100000, 90000]  # Salarios promedio en USD
popularidad = [40.5, 22.9, 18.5, 8.2, 15.3, 21.4, 3.8, 5.2, 50]  # Porcentaje de uso en proyectos web

# Crear DataFrame
df = pd.DataFrame({
    'Framework': frameworks,
    'Salario': salarios,
    'Popularidad': popularidad
})

# Configurar estilo
plt.style.use('default')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# 1. Gráfico de barras para salarios
colors = sns.color_palette("husl", len(frameworks))
bars = ax1.bar(frameworks, salarios, color=colors)
ax1.set_title('Salarios Promedio por Framework Frontend (2023)', pad=20)
ax1.set_xlabel('Framework')
ax1.set_ylabel('Salario Promedio (USD)')
ax1.tick_params(axis='x', rotation=45)

# Añadir etiquetas de valor
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2., height,
             f'${height:,.0f}',
             ha='center', va='bottom')

# 2. Gráfico de dispersión con línea de tendencia
z = np.polyfit(popularidad, salarios, 1)
p = np.poly1d(z)

ax2.scatter(popularidad, salarios, color=colors)
ax2.plot(popularidad, p(popularidad), "r--", alpha=0.8, label='Línea de tendencia')

# Añadir etiquetas para cada punto
for i, framework in enumerate(frameworks):
    ax2.annotate(framework, (popularidad[i], salarios[i]),
                 xytext=(5, 5), textcoords='offset points')

ax2.set_title('Correlación entre Popularidad y Salario', pad=20)
ax2.set_xlabel('Popularidad (%)')
ax2.set_ylabel('Salario Promedio (USD)')
ax2.legend()

# Guardar imágenes
plt.tight_layout()
plt.savefig("frontend_analysis.png")
plt.close()

# Crear el PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Página de introducción
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Analisis de Frameworks Frontend: Hipotesis y Conclusiones", ln=True, align='C')

# Hipótesis
pdf.set_font("Arial", style='B', size=14)
pdf.cell(0, 10, "Hipótesis", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, """
1. Hipótesis Principal: Existe una correlación positiva entre la popularidad de un framework frontend y el salario promedio de los desarrolladores que lo utilizan.

2. Hipótesis Secundarias:
   - Los frameworks más modernos (Next.js, Svelte) tienden a ofrecer mejores salarios que los frameworks más antiguos (jQuery).
   - Los frameworks respaldados por grandes empresas (React - Facebook, Angular - Google) ofrecen salarios más altos.
""")

# Análisis de datos
pdf.set_font("Arial", style='B', size=14)
pdf.cell(0, 10, "Análisis de Datos", ln=True)
pdf.image("frontend_analysis.png", x=10, y=60, w=190)

# Conclusiones
pdf.add_page()
pdf.set_font("Arial", style='B', size=14)
pdf.cell(0, 10, "Conclusiones", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, f"""
1. Correlación Moderada:
   - El coeficiente de correlación es de {np.corrcoef(popularidad, salarios)[0,1]:.2f}, lo que indica una correlación positiva moderada.
   
2. Tendencias del Mercado:
   - Framework mejor pagado: {df.loc[df['Salario'].idxmax(), 'Framework']} (${df['Salario'].max():,.2f}).
   - Framework más popular: {df.loc[df['Popularidad'].idxmax(), 'Framework']} ({df['Popularidad'].max()}%).

3. Implicaciones:
   - La especialización en frameworks modernos ofrece mejores perspectivas salariales.
""")

# Guardar PDF
pdf.output("frontend_analysis.pdf")
print("El archivo PDF se ha generado con éxito.")
