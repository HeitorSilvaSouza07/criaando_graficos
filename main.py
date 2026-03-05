import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('crescimento_ano.csv', sep=";")

plt.plot(df['Ano'],df['Faturamento total'])
plt.xlabel('Ano')
plt.ylabel('Faturamento')
plt.title('Crescimento')
plt.show()
print(df)