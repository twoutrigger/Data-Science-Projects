from flask import Flask, request
import pickle
from numpy import array2string

# path to pickled model
model_path = "rf-churn-model.pkl"

# unpickle customer churn model
with open(model_path, "rb") as file:
    unpickled_rf = pickle.load(file)

# define the app
app = Flask(__name__)

# define the end point
@app.route("/predict_churn", methods=["POST", "GET"])
def predict_churn():

    url_args = request.args.get("features")
    url_args = url_args.split(",")
    url_args = [float(i) for i in url_args]

    return array2string(unpickled_rf.predict([url_args]))

    # Example URLs
    # For churned:
    # http://10.100.10.115:5001/predict_churn?features=1359.0,102.25,0.0,13.0,1.0,1.0,0.0,1.0,2.0,1.0,0.0,0.0,2.0,0.0,2.0,2.0,0.0,1.0,1.0
    # For not churned:
    # http://10.100.10.115:5001/predict_churn?features=1501.75,25.0,1.0,61.0,1.0,1.0,0.0,1.0,2.0,2.0,1.0,1.0,1.0,1.0,1.0,1.0,2.0,0.0,0.0

# run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5001")