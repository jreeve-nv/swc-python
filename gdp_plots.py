import sys
import pandas
import matplotlib.pyplot as plt
import glob



def parse_arguments(argv):
    """
    Parse the argument list passed from the command line
    (after the program filename is removed) and return a list
    of filenames.

    Input:
    ------
        argument list (normally sys.argv[1:])
    
    Returns:
    ------
        filenames: list of strings, list of files to plot
    """
    if argv == []:
        print("Not enough arguments have been provided")
        print("Usage: python gdp_plots.py < filenames >")
        print("Options:")
        print("-a: plot all gdp data sets in current directory")
    
    if "-a" in argv:
        filenames = glob.glob("data/*gdp*.csv")
        if filenames == []:
            print("No files found in this folder.")
            print("Make sure data is located in current directory.")
    else:
        filenames = argv
    
    return filenames

def create_plot(filename):
    """
    Creates a plot for the specified
    data file.

    Input:
    ------
        filename: string, path to file to plot
    
    Returns:
    ------
        none
    """
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

def create_plots(filenames):
    """
    Takes in a list of filenames to plot
    and creates a plot for each file.

    Input:
    ------
        filenames: list of strings, list of files to plot
    
    Returns:
    ------
        none
    """
    for filename in filenames:
        create_plot(filename)

def main():
    """
    Does all the work :)
    """
    filenames = parse_arguments(sys.argv[1:])
    create_plots(filenames)

if __name__ == "__main__":
    main()