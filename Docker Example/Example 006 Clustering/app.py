from flask import Flask, request
import pickle
from numpy import array2string

model_path = ""

with open(model_path, "rb") as file:
    unpickled_rf = pickle.load(file)

app = Flask(__name__)

@app.route("/pred_cluster", methods=["POST", "GET"])
def pred_cluster():

    url_args = 'test'
    # url_args = request.args.get("features")
    # url_args = url_args.split(",")
    # url_args = [float(i) for i in url_args] ## tbd on feature format

    return array2string(unpickled_rf.predict([url_args]))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5001")