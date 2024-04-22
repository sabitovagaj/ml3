#Обобщенный метод наименьших квадратов
from __future__ import print_function
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.iolib.table import (SimpleTable, default_txt_fmt)

data = sm.datasets.longley.load()
data.exog = sm.add_constant(data.exog)
print(data.exog[:5])
ols_resid = sm.OLS(data.endog, data.exog).fit().resid
resid_fit = sm.OLS(ols_resid[1:], sm.add_constant(ols_resid[:-1])).fit()
print(resid_fit.tvalues[1])
print(resid_fit.pvalues[1])
rho = resid_fit.params[1]
from scipy.linalg import toeplitz

toeplitz(range(5))
order = toeplitz(range(len(ols_resid)))
sigma = rho**order
gls_model = sm.GLS(data.endog, data.exog, sigma=sigma)
gls_results = gls_model.fit()
glsar_model = sm.GLSAR(data.endog, data.exog, 1)
glsar_results = glsar_model.iterative_fit(1)
print(glsar_results.summary())
print(gls_results.params)
print(glsar_results.params)
print(gls_results.bse)
print(glsar_results.bse)
