from flask import Flask, request
import pickle
import pandas
from numpy import array2string

table_path = "apriori_table.pkl"

with open(table_path, "rb") as file:
    df = pickle.load(file)

app = Flask(__name__)

@app.route("/apriori", methods=["POST", "GET"])
def predict_churn():

    url_args = request.args.get("items")
    url_args = url_args.split(",")
    url_args = frozenset(url_args)

    try:
        consequents = df[df.antecedents == frozenset(url_args)].iloc[0].consequents
    
    except IndexError:
        consequents = ['Not found']

    return f'Items that go with {", ".join(url_args)}: {", ".join(consequents)}'

    # Example URLs
    # http://10.100.10.115:5001/apriori?items=pasta
    # http://10.100.10.115:5001/apriori?items=mineral%20water,soup

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5001")