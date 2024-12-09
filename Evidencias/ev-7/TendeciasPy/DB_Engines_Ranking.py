import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from fpdf import FPDF

# Crear una clase personalizada para manejar texto y gráficos
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Análisis de Tendencia Exponencial", 0, 1, "C")
        self.ln(10)

    def add_hypothesis(self):
        self.set_font("Arial", size=12)
        self.multi_cell(0, 10, """
## Hipótesis

1. **Hipótesis nula (H0)**: No hay correlación entre el rango y el puntaje de los motores de bases de datos. Esto significa que los cambios en el rango no afectan el puntaje.

2. **Hipótesis alternativa (H1)**: Existe una correlación entre el rango y el puntaje de los motores de bases de datos. Esto implica que a medida que el rango cambia, el puntaje también cambia de manera significativa.
""", 0, "L")
        self.ln(10)

    def add_conclusion(self, coefficient):
        self.set_font("Arial", size=12)
        conclusion = f"""
## Conclusión

Después de calcular el coeficiente de correlación de Pearson, el valor obtenido es **{coefficient:.2f}**. 
Basado en este resultado:

- Si el coeficiente es significativamente diferente de cero, se rechaza la hipótesis nula y se acepta la hipótesis alternativa.
- Esto indicaría que los motores con un mejor rendimiento (puntaje más alto) tienden a tener un rango más bajo (mejor posición en el ranking).
"""
        self.multi_cell(0, 10, conclusion, 0, "L")
        self.ln(10)

# Datos extraídos
rank = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
score = np.array([1286.59, 1029.49, 807.76, 644.36, 410.24,
                  149.43, 133.72, 128.79, 123.05, 103.35,
                  98.94, 93.76, 93.02, 84.24, 83.44,
                  72.95, 70.06, 53.07, 52.67, 45.20])

# Calcular la línea de tendencia exponencial y coeficiente de correlación
log_score = np.log(score)
coefficients = np.polyfit(rank, log_score, 1)
exponential_trend = np.exp(coefficients[0] * rank + coefficients[1])
correlation_coefficient = np.corrcoef(rank, score)[0, 1]

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.scatter(rank, score, color='blue', label='Datos')
plt.plot(rank, exponential_trend, color='red', label='Línea de tendencia exponencial')
plt.title('Gráfica de tendencia exponencial')
plt.xlabel('Rank')
plt.ylabel('Score')
plt.legend()
plt.grid()

# Guardar en un archivo temporal
plt.savefig("grafico_temp.png")
plt.close()

# Crear el PDF
pdf = PDF()
pdf.add_page()

# Agregar texto de hipótesis
pdf.add_hypothesis()

# Agregar la gráfica
pdf.image("grafico_temp.png", x=10, y=None, w=190)

# Agregar conclusión
pdf.add_conclusion(correlation_coefficient)

# Guardar el PDF
pdf.output("analisis_tendencia_exponencial.pdf")
print("El archivo PDF se ha generado como 'analisis_tendencia_exponencial.pdf'")
