import flask
import pickle
import pandas as pd
import numpy as np
import sklearn



# Use pickle to load in the pre-trained model
model = pickle.load(open(f'models/RandForest.sav', 'rb'))


# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')



# Set up the main route
@app.route('/', methods=['GET'])#, 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('home.html'))

@app.route('/predict',methods=['POST'])
def predict():
    cols = ['bedrooms', 'baths', 'OnSiteLaundry', 'AirConditioning',
       'Dishwasher', 'HardwoodFloor', 'CentralHeat', 'FitnessCenter',
       'Storage', 'BusinessCenter', 'Elevator', 'DryCleaningService',
       'InUnitLaundry', 'AssignedParking', 'Carpet', 'Furnished',
       'SwimmingPool', 'OnsiteManagement', 'Balcony', 'CeilingFan',
       'ControlledAccess', 'GarageParking', 'HighCeilings', 'OutdoorSpace',
       'WalkInCloset']   
    input = []
    # Extract the input
    for i in cols:
       input.append(flask.request.form[i])
    
    final = np.array([input])
    final = final.astype('int')
    # Get the model's prediction
    prediction = model.predict(final)[0]
    return flask.render_template('home.html',pred='Expected rental price will be {} $'.format(prediction))

    

##################################
if __name__ == '__main__':
    app.run()

