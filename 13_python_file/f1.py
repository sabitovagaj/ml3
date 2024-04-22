import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import radviz


ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
