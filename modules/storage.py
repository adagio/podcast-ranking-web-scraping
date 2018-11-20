import pickle
import pandas as pd

class Storage:

    def save_csv(filename, data):
        df = pd.DataFrame(data)
        df.to_csv(filename + '.csv', index=False, encoding='utf-8')

    def save_pickle(filename, data):
        with open(filename + '.pkl', 'wb') as file:
            pickle.dump(data, file)

    def load_pickle(filename):
        with open(filename + '.pkl', 'rb') as file:
            data = pickle.load(file)
        return data