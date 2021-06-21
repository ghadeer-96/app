import flask
import pickle
import pandas as pd
import numpy as np
import sklearn
#from sklearn.ensemble import GradientBoostingRegressor,RandomForestRegressor
#from sklearn.linear_model import LinearRegression,ElasticNet,Ridge, Lasso
#from sklearn.neighbors import KNeighborsRegressor
#from sklearn.model_selection import  GridSearchCV, KFold,RandomizedSearchCV



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
    #data_unseen = pd.DataFrame([final], columns = cols)
    # Get the model's prediction
    ##prediction = int(prediction.Label[0])
    prediction = dict()
    for model in ["models/Elastic.sav", "models/KNR.sav", "models/Lasso.sav", "models/LinReg.sav", "models/RandForest.sav", "models/Ridge.sav", "models/GrandBoost.sav" ]:
        print(model)
        loaded_model = pickle.load(open(model, 'rb'))
        prediction[model]=loaded_model.predict(final)[0]
    
    #prediction = model.predict(final)[0]
    #return flask.render_template('home.html',pred='Expected rental price will be {} $'.format(final.size))
    return flask.render_template('home.html',pred='Expected rental price will be {} $'.format(prediction))

    

##################################
if __name__ == '__main__':
    app.run()

