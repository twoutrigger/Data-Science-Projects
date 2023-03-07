from flask import Flask, request
import numpy as np
import joblib
from sklearn.preprocessing import MinMaxScaler
import pickle
from numpy import array2string

model_path = "kmeans.pkl"

with open(model_path, "rb") as file:
    unpickled_model = pickle.load(file)

app = Flask(__name__)

@app.route("/pred_cluster", methods=["POST", "GET"])
def pred_cluster():

    url_args = request.args.get("features")
    url_args = url_args.split(",")
    url_args = [float(i) for i in url_args]

    # x = [1.52101, 13.64, 4.49, 1.10, 71.78, 0.06, 8.75, 0.00, 0.0]
    scaler = joblib.load('minmaxscaler.save') 
    url_args = scaler.transform([url_args])

    print(url_args)
    print(type(url_args))

    ## output for minmaxscaler should be:
    ##  [0.43283582, 0.43759398, 1. ,0.25233645, 0.35178571, 0.00966184, 0.30855019, 0., 0.]

    # return array2string(unpickled_model.predict(url_args))
    return 'test'

    # Example URLs:
    # http://172.20.10.3:5001/pred_cluster?features=1.52101,13.64,4.49,1.10,71.78,0.06,8.75,0.00,0.0


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5001")