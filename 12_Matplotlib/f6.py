from __future__ import print_function
import numpy as np
import statsmodels.api as sm

nsample = 50
sig = 0.25
x1 = np.linspace(0, 20, nsample)
X = np.column_stack((x1, np.sin(x1), (x1-5)**2))
X = sm.add_constant(X)
beta = [5., 0.5, 0.5, -0.02]
y_true = np.dot(X, beta)
y = y_true + sig * np.random.normal(size=nsample)
olsmod = sm.OLS(y, X)
olsres = olsmod.fit()
print(olsres.summary())
ypred = olsres.predict(X)
print(ypred)
x1n = np.linspace(20.5,25, 10)
Xnew = np.column_stack((x1n, np.sin(x1n), (x1n-5)**2))
Xnew = sm.add_constant(Xnew)
ynewpred =  olsres.predict(Xnew) # predict out of sample
print(ynewpred)
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(x1, y, 'o', label="Данные")
ax.plot(x1, y_true, 'b-', label="Точные данные")
ax.plot(np.hstack((x1, x1n)), np.hstack((ypred, ynewpred)), 'r', label="OLS прогнозирование")
ax.legend(loc="Хороший")
print("Сохраняем график")
fig.savefig('graphf6.png')
