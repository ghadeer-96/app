import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model
model = pickle.load(open(f'models/RandForest.sav', 'rb'))


# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

['bedrooms', 'baths', 'On Site Laundry', 'Air Conditioning',
       'Dishwasher', 'Hardwood Floor', 'Central Heat', 'Fitness Center',
       'Storage', 'Business Center', 'Elevator', 'Dry Cleaning Service',
       'In Unit Laundry', 'Assigned Parking', 'Carpet', 'Furnished',
       'Swimming Pool', 'Onsite Management', 'Balcony', 'Ceiling Fan',
       'Controlled Access', 'Garage Parking', 'High Ceilings', 'Outdoor Space',
       'Walk In Closet']

# Set up the main route
@app.route('/', methods=['GET'])#, 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('home.html'))

@app.route('/predict',methods=['POST'])
def predict():
    #if flask.request.method == 'POST':
    # Extract the input
    int_features = [x for x in flask.request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    # Get the model's prediction
    prediction = model.predict(input_variables)[0]
    
    return flask.render_template('home.html',pred='Expected rental price will be {}'.format(prediction))

    
##################################
if __name__ == '__main__':
    app.run()

