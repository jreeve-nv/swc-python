import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('data/gapminder_gdp_oceania.csv', index_col = 'country').T

ax = data.plot()

plt.show()