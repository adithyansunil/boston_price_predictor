from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text=f'Estimated House Price: ${output}k')
    except:
        return render_template('index.html', prediction_text="Error in input. Please enter valid numbers.")

if __name__ == "__main__":
    app.run(debug=True)
