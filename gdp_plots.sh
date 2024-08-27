for filename in data/gapminder_gdp_oceania.csv data/gapminder_gdp_africa.csv
do
    python gdp_plots_bash.py $filename
done