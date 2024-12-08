import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Datos de frameworks frontend y salarios promedio (datos de 2023)
frameworks = ['React', 'Angular', 'Vue.js', 'Svelte', 'Next.js', 'jQuery', 'Ember.js', 'Nuxt.js', 'astro']
salarios = [120000, 115000, 105000, 98000, 125000, 85000, 95000, 10000, 9000 ]  # Salarios promedio en USD
popularidad = [40.5, 22.9, 18.5, 8.2, 15.3, 21.4, 3.8, 5.2, 50]  # Porcentaje de uso en proyectos web

# Crear DataFrame
df = pd.DataFrame({
    'Framework': frameworks,
    'Salario': salarios,
    'Popularidad': popularidad
})

# Configurar el estilo de la visualización
plt.style.use('default')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# 1. Gráfico de barras para salarios
colors = sns.color_palette("husl", len(frameworks))
bars = ax1.bar(frameworks, salarios, color=colors)
ax1.set_title('Salarios Promedio por Framework Frontend (2023)', pad=20)
ax1.set_xlabel('Framework')
ax1.set_ylabel('Salario Promedio (USD)')
ax1.tick_params(axis='x', rotation=45)

# Añadir etiquetas de valor en las barras
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
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

# Calcular y mostrar el coeficiente de correlación
correlation = np.corrcoef(popularidad, salarios)[0,1]
plt.figtext(0.5, -0.05, f'Coeficiente de correlación: {correlation:.2f}', 
            ha='center', va='center', fontsize=10)

# Ajustar el diseño y mostrar el gráfico
plt.tight_layout()
plt.show()

# Imprimir análisis estadístico
print("\nAnálisis Estadístico:")
print(f"Framework mejor pagado: {df.loc[df['Salario'].idxmax(), 'Framework']} (${df['Salario'].max():,.2f})")
print(f"Framework más popular: {df.loc[df['Popularidad'].idxmax(), 'Framework']} ({df['Popularidad'].max()}%)")
print(f"\nCorrelación entre popularidad y salario: {correlation:.2f}")
