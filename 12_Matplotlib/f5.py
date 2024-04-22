import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from pandas_datareader.data import DataReader
from datetime import datetime
from pandas.core import datetools
usrec = DataReader('USREC', 'fred', start=datetime(1947, 1, 1), 
end=datetime(2013, 4, 1))

# Get the federal funds rate data
from statsmodels.tsa.regime_switching.tests.test_markov_regression import fedfunds
dta_fedfunds = pd.Series(fedfunds, index=pd.date_range('1954-07-01', '2010-10-01', freq='QS'))

# Plot the data
dta_fedfunds.plot(title='Federal funds rate', figsize=(12,3))

# Fit the model
# (a switching mean is the default of the MarkovRegession model)
mod_fedfunds = sm.tsa.MarkovRegression(dta_fedfunds, k_regimes=2)
res_fedfunds = mod_fedfunds.fit()
res_fedfunds.summary()
res_fedfunds.smoothed_marginal_probabilities[1].plot(title=
'Probability of being in the high regime', figsize=(12,3))
print(res_fedfunds.expected_durations)
# Fit the model
mod_fedfunds2 = sm.tsa.MarkovRegression(
    dta_fedfunds.iloc[1:], k_regimes=2, exog=dta_fedfunds.iloc[:-1])
res_fedfunds2 = mod_fedfunds2.fit()
res_fedfunds2.summary()
res_fedfunds2.smoothed_marginal_probabilities[0].plot(
    title='Probability of being in the high regime', figsize=(12,3))
print(res_fedfunds2.expected_durations)
# Get the additional data
from statsmodels.tsa.regime_switching.tests.test_markov_regression import ogap, inf
dta_ogap = pd.Series(ogap, index=pd.date_range('1954-07-01', '2010-10-01', freq='QS'))
dta_inf = pd.Series(inf, index=pd.date_range('1954-07-01', '2010-10-01', freq='QS'))

exog = pd.concat((dta_fedfunds.shift(), dta_ogap, dta_inf), axis=1).iloc[4:]

# Fit the 2-regime model
mod_fedfunds3 = sm.tsa.MarkovRegression(
    dta_fedfunds.iloc[4:], k_regimes=2, exog=exog)
res_fedfunds3 = mod_fedfunds3.fit()

# Fit the 3-regime model
np.random.seed(12345)
mod_fedfunds4 = sm.tsa.MarkovRegression(
    dta_fedfunds.iloc[4:], k_regimes=3, exog=exog)
res_fedfunds4 = mod_fedfunds4.fit(search_reps=20)
res_fedfunds3.summary()
res_fedfunds4.summary()
fig, axes = plt.subplots(3, figsize=(10,7))

ax = axes[0]
ax.plot(res_fedfunds4.smoothed_marginal_probabilities[0])
ax.set(title='Smoothed probability of a low-interest rate regime')

ax = axes[1]
ax.plot(res_fedfunds4.smoothed_marginal_probabilities[1])
ax.set(title='Smoothed probability of a medium-interest rate regime')

ax = axes[2]
ax.plot(res_fedfunds4.smoothed_marginal_probabilities[2])
ax.set(title='Smoothed probability of a high-interest rate regime')

fig.tight_layout()    




print("Сохраняем график")
fig.savefig('graph_Arima2.png')