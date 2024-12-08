import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos extraídos
databases = [
    "Oracle", "MySQL", "SQL Server", "PostgreSQL", 
    "MongoDB", "Microsoft Access", "Firebase", "Redis", 
    "Splunk", "SQLite", "Elasticsearch", "MariaDB", 
    "Supabase", "SAP HANA", "DynamoDB", "DB2", 
    "Apache Hive", "Neo4j", "Teradata", "Solr", 
    "FileMaker", "Firebird", "Ingres", "Sybase", 
    "CouchBase", "Hbase", "Memcached", "Riak", 
    "Informix", "CouchDB", "dBase", "Netezza"
]

# Participación en porcentaje
share = np.array([
    28.6, 16.15, 11.4, 7.12, 
    5.91, 5.42, 4.98, 3.67, 
    2.77, 2.01, 1.8, 1.4, 
    1.15, 1.14, 1.12, 1.05, 
    0.75, 0.6, 0.47, 0.46, 
    0.45, 0.27, 0.25, 0.23, 
    0.15, 0.15, 0.14, 0.13, 
    0.11, 0.06, 0.05, 0.04
])

# Índices numéricos para las bases de datos
x = np.arange(len(databases)).reshape(-1, 1)  # Reshape para modelo de sklearn
y = share

# Ajustar el modelo de regresión lineal
model = LinearRegression()
model.fit(x, y)

# Predicciones
y_pred = model.predict(x)

# Gráfica
plt.figure(figsize=(12, 8))
plt.scatter(x, y, color='blue', label='Datos reales')  # Puntos originales
plt.plot(x, y_pred, color='red', label='Regresión lineal')  # Línea de regresión
plt.xlabel('Índice de Bases de Datos', fontsize=12)
plt.ylabel('Participación (%)', fontsize=12)
plt.title('Regresión Lineal: Participación de Bases de Datos en el Mercado', fontsize=16)
plt.xticks(ticks=x.flatten(), labels=databases, rotation=90)
plt.legend()
plt.grid(alpha=0.6)
plt.tight_layout()
plt.show()
