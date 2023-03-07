from flask import Flask, request
import numpy as np
import joblib
from sklearn.preprocessing import MinMaxScaler
import pickle
from numpy import array2string

# model_path = ""

# with open(model_path, "rb") as file:
#     unpickled_rf = pickle.load(file)

app = Flask(__name__)

@app.route("/pred_cluster", methods=["POST", "GET"])
def pred_cluster():

    url_args = 'test'
    # url_args = request.args.get("features")
    # url_args = url_args.split(",")
    # url_args = [float(i) for i in url_args] ## tbd on feature format

    x = [1.52101, 13.64, 4.49, 1.10, 71.78, 0.06, 8.75, 0.00, 0.0]
    minmaxscaler = joblib.load('minmaxscaler.save') 
    # x = minmaxscaler.fit_transform(np.array(x,))
    x = minmaxscaler.fit_transform([x])

    print(x)

    ## output should be:
    ##  [0.43283582, 0.43759398, 1. ,0.25233645, 0.35178571, 0.00966184, 0.30855019, 0., 0.]

    # return array2string(unpickled_rf.predict([url_args]))
    return url_args


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5001")