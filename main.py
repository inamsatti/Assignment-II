import pandas as pd
import graphs


def read_file_data(filename):
    df = pd.read_csv(filename, header=2)
    
    # transpose
    df_year = df.set_index('Country Name').T
    # clean up column headers
    df_year.columns.name = ''
    # transpose
    df_country = df_year.T
    df_country.columns.name = 'Country Name'
    # clean up
    df_year.fillna('', inplace=True)
    df_country.fillna('', inplace=True)
    # return
    return df_country, df_year

df_country, df_year = read_file_data('urban-development.csv')

# print data
print(df_country,df_year)


# Read data
df = pd.read_csv('urban-development.csv', skiprows=4)
# clean data
df.fillna('', inplace=True)

# Countries of interest
countries_array = ['China','France','India','South Africa','Romania','United Kingdom','United States']


# Indicators of interest
indicators_array = ['Urban population', 'Population in the largest city (% of urban population)','Access to electricity, urban (% of urban population)', 'Pump price for diesel fuel (US$ per liter)', 'Urban population growth (annual %)']


# Subset the data
df_sub = df[(df['Country Name'].isin(countries_array)) & (df['Indicator Name'].isin(indicators_array))]

# Calculate statistics with describe
stats = df_sub.groupby(['Country Name', 'Indicator Name']).describe()

# Print the statistics
print(stats)

# get years colums
year = [col for col in df_sub.columns if col.isdigit()]

# graphs
graphs.bar_graph(df_sub, year, 'Urban population', 'Country Name', '')
graphs.bar_graph(df_sub, year, 'Urban population growth (annual %)', 'Country Name', '')
graphs.heatmap(df_sub, 'China', indicators_array,'crest')
graphs.heatmap(df_sub, 'United Kingdom', indicators_array,'BuPu')
