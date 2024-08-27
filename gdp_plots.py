import pandas
import matplotlib.pyplot as plt

filename = 'data/gapminder_gdp_oceania.csv'

data = pandas.read_csv(filename, index_col = 'country').T

ax = data.plot(title = filename)

ax.set_xlabel("Year")
ax.set_ylabel("GDP Per Capita")

ax.set_xticks(range(len(data.index)))
ax.set_xticklabels(data.index, rotation = 45)

plt.show()
