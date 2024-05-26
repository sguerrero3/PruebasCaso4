import pandas as pd

csv_file_path = "./Resultados/100.csv"


column_names = ['timeStamp', 'elapsed', 'label', 'responseCode', 'responseMessage', 'threadName', 'dataType', 'success', 'failureMessage', 'bytes', 'sentBytes', 'grpThreads']


df = pd.read_csv(csv_file_path, names=column_names)


