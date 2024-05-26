import pandas as pd
import matplotlib.pyplot as plt

pruebas = ["100", "500", "1000", "1500"]
noCumple = []
totalDatos = []
porcentaje = []

for i in pruebas:

    csv_file_path = "./Resultados/" + i + ".csv"

    column_names = ['timeStamp', 'elapsed', 'label', 'responseCode', 'responseMessage', 'threadName', 'dataType', 'success', 'failureMessage', 'bytes', 'sentBytes', 'grpThreads']

    df = pd.read_csv(csv_file_path, names=column_names)

    count_greater_than_4000 = (df['elapsed'] > 4000).sum()

    noCumple.append(count_greater_than_4000 )
    totalDatos.append(len(df))

    porcentaje.append((count_greater_than_4000/len(df))*100)

plt.plot(pruebas, porcentaje)

plt.xlabel('Numero de usuarios')
plt.ylabel('Porcentaje de request que tiene un tiempo mayor a 4s')
plt.title('Se ve feo')

plt.show()
