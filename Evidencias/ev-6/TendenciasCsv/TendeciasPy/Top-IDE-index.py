import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos proporcionados
data = {
    'Rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33],
    'IDE': ['Visual Studio', 'Visual Studio Code', 'Eclipse', 'pyCharm', 'Android Studio', 'IntelliJ', 'NetBeans', 'Xcode',
            'RStudio', 'Sublime Text', 'Atom', 'Code::Blocks', 'Vim', 'PhpStorm', 'Qt Creator', 'Komodo', 'Emacs', 'geany',
            'Xamarin', 'JCreator', 'JDeveloper', 'Light Table', 'RAD Studio', 'Eric Python', 'Monkey Studio', 'RubyMine',
            'Aptana', 'SharpDevelop', 'MonoDevelop', 'DrJava', 'Julia Studio', 'SlickEdit', 'Zend Studio'],
    'Share (%)': [27.57, 14.16, 11.89, 10.67, 9.89, 8.03, 3.81, 2.98, 2.77, 2.52, 2.08, 1.4, 0.87, 0.38, 0.3, 0.18, 0.18, 0.15,
                  0.11, 0.02, 0.02, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    '1-year Trend (%)': [-0.3, 0.3, 0.6, 1.2, 0.7, 0.4, -0.3, -0.3, -0.2, -0.5, -0.8, -0.2, -0.0, -0.0, +0.0, -0.0, -0.0, +0.0,
                         -0.1, -0.0, -0.1, -0.1, -0.1, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, +0.0, -0.0]
}

# Asegúrate de que todas las listas tengan la misma longitud
max_length = 33  # La longitud deseada

for key in data:
    current_length = len(data[key])
    if current_length < max_length:
        data[key].extend([None] * (max_length - current_length))
    elif current_length > max_length:
        data[key] = data[key][:max_length]  # Recorta si hay más elementos de los necesarios

# Crear DataFrame
df = pd.DataFrame(data)

# Crear figura y ejes
fig, ax1 = plt.subplots(figsize=(14, 8))

# Graficar participación en el mercado
sns.barplot(x='Share (%)', y='IDE', data=df, ax=ax1, color='skyblue', label='Share (%)')
ax1.set_xlabel('Share (%)')
ax1.set_ylabel('IDE', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')
ax1.set_title('IDE Market Share and 1-Year Trend')

# Crear un segundo eje y para la tendencia
ax2 = ax1.twinx()
sns.lineplot(x='Share (%)', y='1-year Trend (%)', data=df, ax=ax2, color='red', marker='o', label='1-year Trend (%)')
ax2.set_ylabel('1-year Trend (%)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Añadir leyendas
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Mostrar gráfico
plt.tight_layout()
plt.show()
