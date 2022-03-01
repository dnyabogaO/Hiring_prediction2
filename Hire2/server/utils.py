import json
import pickle
import numpy as np

__data_columns = None
__model = None



def get_col_names():
    return __data_columns

def load_saved_artefacts():
    print("loading saved artefacts")
    global __data_columns

    with open("./artefacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']

    with open("./artefacts/hiring.pkl", 'rb') as f:
        __model = pickle.load(f)
    print("loading artefacts done")

def predict():
    global __model

    int_features = [int(x) for x in __data_columns.form.values()]
    final_features = [np.array(int_features)]
    prediction = __model.predict(final_features)

    output = round(prediction[0],2)

    ##return render_template('app.html', prediction_text='Employ Salary should be ksh {}'.format(output))
    return format(output)

if __name__ == "__main__":
    load_saved_artefacts()
    print(get_col_names())

    print(predict())
