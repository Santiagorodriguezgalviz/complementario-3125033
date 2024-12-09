import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from fpdf import FPDF

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

# Gráfica de dispersión con la línea de regresión
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

# Guardar la gráfica como imagen
plt.savefig("db_participation_regression.png")

# Crear el documento PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Título
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, txt="Análisis de Participación de Bases de Datos y Regresión Lineal", ln=True, align='C')

# Agregar la gráfica como imagen al PDF
pdf.ln(10)
pdf.image("db_participation_regression.png", x=10, y=30, w=180)

# Hipótesis
pdf.ln(100)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, txt="""Hipótesis:

1. Hipótesis nula (H0): No hay correlación entre la participación de las bases de datos y su popularidad. Esto significa que los cambios en la participación no están relacionados con la popularidad de las bases de datos.

2. Hipótesis alternativa (H1): Existe una correlación entre la participación de las bases de datos y su popularidad. Esto implica que a medida que la participación cambia, la popularidad de las bases de datos también tiende a cambiar de manera significativa.
""")

# Conclusión
pdf.ln(10)
pdf.multi_cell(0, 10, txt="""Conclusión:

Después de ejecutar el código y observar el coeficiente de correlación, se podrá aceptar o rechazar la hipótesis nula. Si el coeficiente es significativamente diferente de cero, se puede concluir que hay una relación entre la participación de las bases de datos y su popularidad, lo que podría indicar que las bases de datos más populares tienden a tener una mayor participación en el mercado.
""")

# Guardar el PDF
pdf_output = "db_participation_analysis_report.pdf"
pdf.output(pdf_output)

print(f"El análisis ha sido guardado en: {pdf_output}")
