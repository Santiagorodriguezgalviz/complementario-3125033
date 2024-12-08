import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos proporcionados
data = {
    'Rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32],
    'Database': ['Oracle', 'MySQL', 'SQL Server', 'PostgreSQL', 'MongoDB', 'Microsoft Access', 'Firebase', 'Redis', 'Splunk', 'SQLite',
                 'Elasticsearch', 'MariaDB', 'Supabase', 'SAP HANA', 'DynamoDB', 'DB2', 'Apache Hive', 'Neo4j', 'Teradata',
                 'Solr', 'FileMaker', 'Firebird', 'Ingres', 'Sybase', 'CouchBase', 'Hbase', 'Memcached', 'Riak', 'Informix',
                 'CouchDB', 'dBase', 'Netezza'],
    'Share (%)': [28.6, 16.15, 11.4, 7.12, 5.91, 5.42, 4.98, 3.67, 2.77, 2.01, 1.8, 1.4, 1.15, 1.14, 1.12, 1.05, 0.75, 0.6,
                  0.47, 0.46, 0.45, 0.27, 0.25, 0.23, 0.15, 0.15, 0.14, 0.13, 0.11, 0.06, 0.05, 0.04],
    '1-year Trend (%)': [14.3, 7.1, 5.2, 3.7, -1.0, 2.1, -1.9, -3.2, -4.1, -3.0, -3.8, -2.3, -0.4, -1.6, -2.0, -1.6, -1.8,
                          -0.7, -1.0, -0.6, -0.7, -0.4, -0.4, -0.4, -0.3, -0.3, -0.2, -0.2, -0.2, -0.1, -0.1]
}

# Verificar longitudes
lengths = {key: len(value) for key, value in data.items()}
print("Longitudes de las listas:", lengths)

# Ajustar la longitud de las listas
max_length = min(lengths.values())  # La longitud mínima entre todas las listas

for key in data:
    if len(data[key]) != max_length:
        data[key] = data[key][:max_length]  # Recortar listas largas

# Crear DataFrame
df = pd.DataFrame(data)

# Crear figura y ejes
fig, ax1 = plt.subplots(figsize=(14, 8))

# Graficar participación en el mercado
sns.barplot(x='Share (%)', y='Database', data=df, ax=ax1, color='skyblue', label='Share (%)')
ax1.set_xlabel('Share (%)')
ax1.set_ylabel('Database', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')
ax1.set_title('Database Market Share and 1-Year Trend')

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
