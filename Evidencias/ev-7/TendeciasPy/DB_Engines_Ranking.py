import numpy as np
import matplotlib.pyplot as plt

# Datos extraídos
rank = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                    11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
score = np.array([1286.59, 1029.49, 807.76, 644.36, 410.24,
                    149.43, 133.72, 128.79, 123.05, 103.35,
                    98.94, 93.76, 93.02, 84.24, 83.44,
                    72.95, 70.06, 53.07, 52.67, 45.20])

# Calcular la línea de tendencia exponencial
log_score = np.log(score)  # Usamos el logaritmo para la regresión exponencial
coefficients = np.polyfit(rank, log_score, 1)  # Regresión lineal en el espacio logarítmico
exponential_trend = np.exp(coefficients[0] * rank + coefficients[1])  # Regresar al espacio original

# Calcular el coeficiente de correlación de Pearson
correlation_coefficient = np.corrcoef(rank, score)[0, 1]  # Calcula la correlación
print(f'Coeficiente de correlación de Pearson: {correlation_coefficient}')  # Imprimir el resultado

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.scatter(rank, score, color='blue', label='Datos')
plt.plot(rank, exponential_trend, color='red', label='Línea de tendencia exponencial')
plt.title('Gráfica de tendencia exponencial')
plt.xlabel('Rank')
plt.ylabel('Score')
plt.legend()
plt.grid()
plt.show()