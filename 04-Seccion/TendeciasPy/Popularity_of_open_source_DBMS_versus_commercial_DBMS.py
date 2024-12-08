import numpy as np
import matplotlib.pyplot as plt

# Datos extraídos
dbms = [
    "Oracle", "MySQL", "Microsoft SQL Server", "PostgreSQL", "MongoDB",
    "Redis", "Snowflake", "Elasticsearch", "IBM Db2", "SQLite",
    "Apache Cassandra", "Microsoft Access", "Splunk", "Databricks", "MariaDB",
    "Microsoft Azure SQL Database", "Amazon DynamoDB", "Apache Hive", "Google BigQuery", "FileMaker"
]

# Puntajes de popularidad (Septiembre 2024)
scores = np.array([
    1286.59, 1029.49, 807.76, 644.36, 410.24,
    149.43, 133.72, 128.79, 123.05, 103.35,
    98.94, 93.76, 93.02, 84.24, 83.44,
    72.95, 70.06, 53.07, 52.67, 45.20
])

# Ranking (usamos el ranking inverso, ya que el primero tiene el puntaje más alto)
rankings = np.array(range(1, 21))

# Crear la gráfica de popularidad
plt.figure(figsize=(12, 8))
plt.barh(dbms, scores, color='skyblue')
plt.xlabel('Puntaje (Sep 2024)')
plt.title('Puntajes de los Sistemas de Gestión de Bases de Datos (Sep 2024)')
plt.gca().invert_yaxis()  # Invertir el eje y para mostrar el DBMS con mayor puntaje en la parte superior
plt.grid(axis='x')
plt.tight_layout()
plt.show()

# Datos de tendencias históricas
years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
ranking_scores = np.array([30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52])

# Crear la gráfica de tendencias históricas
plt.figure(figsize=(10, 6))
plt.plot(years, ranking_scores, marker='o', color='green', label='Puntajes de Clasificación')

# Línea de regresión lineal
coeffs = np.polyfit(years, ranking_scores, 1)
line = np.poly1d(coeffs)
plt.plot(years, line(years), color='red', linestyle='--', label='Tendencia lineal')  # Línea de regresión

plt.xlabel('Año')
plt.ylabel('Puntajes de Clasificación (%)')
plt.title('Tendencias Históricas de Puntajes de Clasificación (2013-2024)')
plt.xticks(years)
plt.grid()
plt.legend()  # Leyenda para la línea de regresión
plt.tight_layout()
plt.show()