import pandas as pd
import matplotlib.pyplot as plt

file_name = 'EmpresasIndustria_2012_2022.csv'
#Le he cambiado el encoding porque el csv viene en UTF-8 en lugar de ISO
df = pd.read_csv(file_name, parse_dates=True, sep=',', encoding = "UTF-8")
x = df.iloc[:,0]
y = df.iloc[:,1]
plt.scatter(x,y)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de dispersión del conjunto de datos')
plt.savefig('industria_anio.png')
