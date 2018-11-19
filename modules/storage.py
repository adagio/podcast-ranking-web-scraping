import pickle

class Storage:

    def save(filename, data):
        with open(filename, 'wb') as file:  
            pickle.dump(data, file)

    def load(filename):
        with open(filename, 'rb') as file:  
            data = pickle.load(file)
        return data