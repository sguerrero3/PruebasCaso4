import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

pruebas = ["50", "100", "150", "200", "250", "300", "350", "400", "600", "700", "1000", "1500"]
noCumple = []
totalDatos = []
porcentaje = []
average = []

for i in pruebas:
    csv_file_path = "./Resultados/" + i + ".csv"
    column_names = ['timeStamp', 'elapsed', 'label', 'responseCode', 'responseMessage', 'threadName', 'dataType', 'success', 'failureMessage', 'bytes', 'sentBytes', 'grpThreads']
    df = pd.read_csv(csv_file_path, names=column_names)
    
    count_greater_than_4000 = (df['elapsed'] > 4000).sum()
    
    noCumple.append(count_greater_than_4000)
    totalDatos.append(len(df))
    porcentaje.append((count_greater_than_4000 / len(df)) * 100)
    average.append(df[['elapsed']].mean().values[0])



# Convert pruebas to numeric values for regression
pruebas_numeric = np.array([int(p) for p in pruebas])
x_dense = np.linspace(min(pruebas_numeric), max(pruebas_numeric), 500)

# Calculate linear regression
slope, intercept, r_value, p_value, std_err = linregress(pruebas_numeric, porcentaje)

# Generate regression line values
regression_line = slope * x_dense + intercept


# Plot data
plt.plot(pruebas_numeric, porcentaje, label='Data')

# Plot regression line
plt.plot(x_dense, regression_line,linestyle='--', label=f'y = {slope:.2f}x + {intercept:.2f}', color='green')

# Add horizontal line at y = 6%
plt.axhline(y=6, color='r', linestyle='--', label='y = 6%')

# Add labels and title
plt.xlabel('Numero de usuarios')
plt.ylabel('Porcentaje de request que tiene un tiempo mayor a 4s')
plt.title('Porcentaje de usuarios con tiempo de respuesta\nmayor a 4s  por numero total de usuarios')
plt.legend()
plt.show()
