# Python lists
# Numpy arrays

# Python dictionaries
# Pandas Dataframes
# Pandas groupby

# Bokeh ColumnDataSource

west_top_2 = (standings[(standings['teamAbbr'] == 'HOU') | (standings['teamAbbr'] == 'GS')]
               .loc[:, ['stDate', 'teamAbbr', 'gameWon']]
               .sort_values(['teamAbbr','stDate']))

west_top_2.head()
