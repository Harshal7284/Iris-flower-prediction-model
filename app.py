from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the exported XGBoost model snapshot configuration
with open('flower_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Grab and format quantitative inputs from input rows
        sepal_length = float(request.form['SepalLengthCm'])
        sepal_width = float(request.form['SepalWidthCm'])
        petal_length = float(request.form['PetalLengthCm'])
        petal_width = float(request.form['PetalWidthCm'])
        
        # DataFrame matches columns layout exactly: ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
        flower_data = pd.DataFrame(
            [[sepal_length, sepal_width, petal_length, petal_width]], 
            columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
        )
        
        # Get numerical output label index [0, 1, or 2]
        prediction = model.predict(flower_data)[0]
        
        # Explicit mapping matching your notebook translation criteria
        if prediction == 0:
            species_output = "Flower is Iris-setosa"
        elif prediction == 1:
            species_output = "Flower is Iris-versicolor"
        else:
            species_output = "Flower is Iris-virginica"
            
        return render_template('index.html', prediction_text=species_output)

if __name__ == '__main__':
    app.run(debug=True)