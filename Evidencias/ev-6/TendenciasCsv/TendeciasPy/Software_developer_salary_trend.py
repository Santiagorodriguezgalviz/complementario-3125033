import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos
data = {
    'Lenguaje': ['Scala', 'Go', 'Kotlin', 'C++', 'Rust', 'C', 'Shell scripting', 'Java', 
                 'Python', 'SQL', 'Swift', 'Dart', 'TypeScript', 'JavaScript', 'C#', 
                 'PHP', 'HTML/CSS'],
    'Porcentaje': [60, 50, 41, 40, 40, 38, 38, 37, 36, 33, 32, 32, 32, 28, 28, 25, 24]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Ordenar los datos por porcentaje
df = df.sort_values('Porcentaje', ascending=True)

# Crear gráfico
plt.figure(figsize=(12, 8))
sns.barplot(x='Porcentaje', y='Lenguaje', data=df, palette='viridis')

# Añadir títulos y etiquetas
plt.title('Porcentaje de Uso por Lenguaje de Programación')
plt.xlabel('Porcentaje')
plt.ylabel('Lenguaje')

# Mostrar gráfico
plt.grid(axis='x')
plt.show()
