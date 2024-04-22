# %matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15,5)  # Размер картинок
fixed_df = pd.read_csv('data/bikes.csv',sep=';', encoding='latin1',parse_dates=['Date'], dayfirst=True,index_col='Date')  # Это то, куда вы скачали файл
print(fixed_df[:3])
fixed_df['Kartoshka'].plot()
fixed_df['Pshenisa'].plot()
plt.show()