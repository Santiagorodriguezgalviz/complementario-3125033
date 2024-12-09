import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos Share
data_share = {
    'Language': ['Python', 'Java', 'JavaScript', 'C#', 'C/C++', 'R', 'PHP', 'TypeScript', 'Swift', 'Rust', 
                 'Objective-C', 'Go', 'Kotlin', 'Matlab', 'Ruby', 'VBA', 'Powershell', 'Ada', 'Dart', 
                 'Lua', 'Abap', 'Scala', 'Visual Basic', 'Julia', 'Groovy', 'Cobol', 'Perl', 'Delphi/Pascal', 
                 'Haskell'],
    'Share': [29.66, 15.64, 8.3, 6.64, 6.46, 4.66, 4.35, 2.96, 2.69, 2.65, 2.45, 2.08, 1.95, 1.45, 
              0.99, 0.97, 0.96, 0.96, 0.94, 0.69, 0.59, 0.57, 0.47, 0.29, 0.23, 0.21, 0.08, 0.07, 0.06]
}

# Datos Trend - Ajustamos las longitudes para que coincidan con los datos de 'Share'
data_trend = {
    'Language': ['Python', 'Java', 'JavaScript', 'C#', 'C/C++', 'R', 'PHP', 'TypeScript', 'Swift', 'Rust', 
                 'Objective-C', 'Go', 'Kotlin', 'Matlab', 'Ruby', 'VBA', 'Powershell', 'Ada', 'Dart', 
                 'Lua', 'Abap', 'Scala', 'Visual Basic', 'Julia', 'Groovy', 'Cobol', 'Perl', 'Delphi/Pascal', 
                 'Haskell'],
    '1-year Trend': [1.6, -0.2, -1.0, -0.1, -0.2, 0.2, -0.5, -0.0, 0.0, 0.6, 0.2, 0.2, 0.2, -0.1, 
                     -0.1, 0.0, 0.1, -0.1, -0.0, 0.1, -0.0, -0.1, -0.1, -0.0, -0.2]
}

# Asegurar que las listas tengan la misma longitud
min_length = min(len(data_trend['Language']), len(data_trend['1-year Trend']))

# Cortar las listas de 'data_trend' para que coincidan en longitud
data_trend['Language'] = data_trend['Language'][:min_length]
data_trend['1-year Trend'] = data_trend['1-year Trend'][:min_length]

# Crear los DataFrames
df_share = pd.DataFrame(data_share)
df_trend = pd.DataFrame(data_trend)

# Fusionar ambos DataFrames por 'Language'
merged_df = pd.merge(df_share, df_trend, on='Language', how='inner')

# Verificación de los DataFrames fusionados
print("DataFrame Share:")
print(df_share.head())
print("\nDataFrame Trend:")
print(df_trend.head())
print("\nMerged DataFrame:")
print(merged_df.head())

# Graficar
plt.figure(figsize=(14, 10))
sns.scatterplot(x='Share', y='Language', size='1-year Trend', sizes=(20, 200), 
                hue='1-year Trend', palette='coolwarm', data=merged_df, legend=None, marker='o')

# Añadir etiquetas de tendencia
for index, row in merged_df.iterrows():
    plt.text(row['Share'], row['Language'], f'{row["1-year Trend"]:.1f}%', 
             color='black', ha='right', va='center')

plt.xlabel('Share (%)')
plt.ylabel('Language')
plt.title('Programming Languages Share vs. 1-year Trend')
plt.grid(True)
plt.show()
