import matplotlib.pyplot as plt
import numpy as np

# Datos
dbms = [
    "Oracle", "MySQL", "Microsoft SQL Server", "PostgreSQL", "MongoDB", 
    "Redis", "Snowflake", "Elasticsearch", "IBM Db2", "SQLite", 
    "Apache Cassandra", "Microsoft Access", "Splunk", "Databricks", "MariaDB", 
    "Microsoft Azure SQL Database", "Amazon DynamoDB", "Apache Hive", 
    "Google BigQuery", "FileMaker"
]

scores = [
    1286.59, 1029.49, 807.76, 644.36, 410.24, 
    149.43, 133.72, 128.79, 123.05, 103.35, 
    98.94, 93.76, 93.02, 84.24, 83.44, 
    72.95, 70.06, 53.07, 52.67, 45.20
]

changes_year = [
    45.72, -82.00, -94.45, 23.61, -29.18, 
    -14.26, 12.83, -10.20, -13.67, -25.85, 
    -11.11, -34.81, 1.63, 9.06, -17.01, 
    -9.78, -10.85, -18.76, -3.80, -8.40
]

# Crear gráfico de barras
plt.figure(figsize=(12, 8))
bars = plt.barh(dbms, scores, color='skyblue', edgecolor='black')

# Añadir los cambios de puntaje al final de cada barra
for i, (bar, change) in enumerate(zip(bars, changes_year)):
    plt.text(
        bar.get_width() + 20, bar.get_y() + bar.get_height()/2, 
        f'{change:+.2f}', va='center', fontsize=10, color='black', fontweight='bold'
    )

# Añadir título y etiquetas
plt.title('Ranking de DBMS por Puntaje (Sep 2024)', fontsize=18, fontweight='bold', color='darkblue')
plt.xlabel('Puntaje', fontsize=14)
plt.ylabel('DBMS', fontsize=14)
plt.grid(True, axis='x', linestyle='--', alpha=0.6)

# Añadir un fondo agradable
plt.gca().set_facecolor('#f0f0f0')

# Mostrar gráfico
plt.tight_layout()
plt.show()
