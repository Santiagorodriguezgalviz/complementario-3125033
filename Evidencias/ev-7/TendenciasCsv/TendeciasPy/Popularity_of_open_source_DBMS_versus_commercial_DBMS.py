import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Datos
data = {
    'Rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'DBMS': ['Oracle', 'MySQL', 'Microsoft SQL Server', 'PostgreSQL', 'MongoDB', 'Redis',
             'Snowflake', 'Elasticsearch', 'IBM Db2', 'SQLite', 'Apache Cassandra', 
             'Microsoft Access', 'Splunk', 'Databricks', 'MariaDB', 'Microsoft Azure SQL Database',
             'Amazon DynamoDB', 'Apache Hive', 'Google BigQuery', 'FileMaker'],
    'Score (Sep 2024)': [1286.59, 1029.49, 807.76, 644.36, 410.24, 149.43, 133.72, 128.79, 
                          123.05, 103.35, 98.94, 93.76, 93.02, 84.24, 83.44, 72.95, 70.06, 
                          53.07, 52.67, 45.20],
    'Change (Sep 2024)': [28.11, 2.63, -7.41, 6.97, -10.74, -3.28, -2.25, -1.04, 0.04, 
                           -1.44, 1.94, -2.61, -3.08, -0.22, -3.09, -2.08, 1.15, -2.17, -2.86, 
                           -1.47]
}

df = pd.DataFrame(data)

# Configuración visual de la gráfica
plt.figure(figsize=(14, 10))
sns.barplot(x='Score (Sep 2024)', y='DBMS', data=df, palette='viridis')

# Añadir etiquetas y título
plt.xlabel('Score (Sep 2024)')
plt.ylabel('DBMS')
plt.title('Popularidad de DBMS en Septiembre 2024')

# Añadir etiquetas de cambio en la gráfica
for index, row in df.iterrows():
    plt.text(row['Score (Sep 2024)'], index, f'{row["Change (Sep 2024)"]:.2f}', 
             color='black', ha='left', va='center')

plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()
