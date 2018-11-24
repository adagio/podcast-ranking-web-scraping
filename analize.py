import pandas as pd
import timeit

from modules.storage import Storage


def describe_values(df, colname):
    values_df = df[[colname]]
    print(values_df.describe())


def analize():

    df = Storage.load_csv('storage/ranking.csv')

    #df = df[['title','time','likes','comments']]
    #df = df.dropna() # remove rows with NaN values

    #print(df.describe())

    total = df.count()[0]
    print(f'total: {total}')

    #top by quantity of episodes
    #top(min) by stair

    df_sorted_by_episodes = df[['category_id','title', 'episodes']].sort_values(by='episodes', ascending=False)
    print(df_sorted_by_episodes.head(10))
    describe_values(df_sorted_by_episodes, 'episodes')

    df_sorted_by_stair = df[['title', 'stair']].sort_values(by='stair')
    df_sorted_by_stair_unique = df_sorted_by_stair.drop_duplicates()

    print(df_sorted_by_stair_unique.head(10))
    #describe_values(df_sorted_by_stair, 'stair')
