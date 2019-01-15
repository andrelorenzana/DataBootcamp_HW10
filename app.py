# 1. Import Flask
from flask import Flask, jsonify
import csv




with open('Resources/prcp.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    prcp = list(reader)
with open('Resources/station.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    stations = list(reader)
with open('Resources/temp.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    temperature = list(reader)

raw_data = [prcp, stations, temperature]
var_num = 0
dict_data = []
for var in raw_data:
    var_dict = []
    for i in range(1,len(var)):
        entry = {var[0][0]: var[i][0], var[0][1] : var[i][1]}
        var_dict.append(entry)
    dict_data.append(var_dict)
    var_num += 1

prcp_dict = dict_data[0]
station_dict = dict_data[1]
temp_dict = dict_data[2]


# 2. Create an app
app = Flask(__name__)


# 3. Define static routes
@app.route("/")
def index():
    return "Welcome"


@app.route("/api/v1.0/precipitation")
def precipitation():

    return jsonify(prcp_dict)


@app.route("/api/v1.0/stations")
def stations():

    return jsonify(station_dict)

@app.route("/api/v1.0/tobs")
def tobs():

    return jsonify(temp_dict)

# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
