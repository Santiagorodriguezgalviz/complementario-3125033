import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos
data = {
    'Language': ['Python', 'Java', 'JavaScript', 'C++', 'TypeScript', 'SQL', 'C#', 
                 'Go', 'C', 'HTML', 'Rust', 'Mathematica', 'PHP', 'Shell', 'Lua', 'SAS'],
    'Popularity': [1, 0.4855, 0.4451, 0.3749, 0.2497, 0.2258, 0.2089, 0.2052, 
                   0.1989, 0.1817, 0.1506, 0.1275, 0.1196, 0.117, 0.1041, 0.0855]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Ordenar los datos por popularidad
df = df.sort_values('Popularity', ascending=True)

# Crear gráfico
plt.figure(figsize=(12, 8))
sns.barplot(x='Popularity', y='Language', data=df, palette='plasma')

# Añadir títulos y etiquetas
plt.title('Popularity of Programming Languages')
plt.xlabel('Popularity')
plt.ylabel('Language')

# Mostrar gráfico
plt.grid(axis='x')
plt.show()
