import pickle


# simple_dict = {"a": '1', "b": '2'}
# with open('genre_vectorizer.pickle', 'r') as picklefile:

# asdf = joblib.load('genre_vectorizer.pickle')

# print(type(asdf))


class MyCustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):

        if module == "__main__":
            module = "data_preprocessing"
        return super().find_class(module, name)

with open('genre_vectorizer.pickle', 'rb') as f:
    unpickler = MyCustomUnpickler(f)
    obj = unpickler.load()
print(obj.get_feature_names_out())
print(type(obj))

##        return super().find_class(os.path.join(os.path.dirname(os.getcwd()), module) , name)
