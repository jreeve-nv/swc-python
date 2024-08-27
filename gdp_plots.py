import sys
import pandas
import matplotlib.pyplot as plt
import glob

if "-a" in sys.argv:
    filenames = glob.glob("data/*gdp*.csv")
else:
    filenames = sys.argv[1:]

for filename in filenames:

    data = pandas.read_csv(filename, index_col = 'country').T
    split_name1 = filename.split('.')[0]
    split_name2 = split_name1.split('/')[1]
    save_name = 'figs/' + split_name2 + '.png'

    ax = data.plot(title = filename)

    ax.set_xlabel("Year")
    ax.set_ylabel("GDP Per Capita")

    ax.set_xticks(range(len(data.index)))
    ax.set_xticklabels(data.index, rotation = 45)

    plt.savefig(save_name)
