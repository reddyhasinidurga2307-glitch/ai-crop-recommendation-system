from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

# Load model and scaler
try:
    model = pickle.load(open('model.pkl', 'rb'))
    mx = pickle.load(open('minmaxscaler.pkl', 'rb'))
except FileNotFoundError:
    print("Error: model.pkl or minmaxscaler.pkl not found.")
    raise

app = Flask(__name__)

@app.route('/')
def log2():
    return render_template('log2.html')

@app.route("/predict", methods=['POST'])
def predict():
    print("Submitted form data:", request.form)  # Debug: Print form data to terminal
    try:
        N = float(request.form['Nitrogen'])
        P = float(request.form['Phosphorus'])
        K = float(request.form['Potassium'])
        temp = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['pH'])
        rainfall = float(request.form['Rainfall'])

        if N < 0 or P < 0 or K < 0:
            raise ValueError("N, P, and K values cannot be negative.")

        if N > 140:
           raise ValueError("Nitrogen must be between 0 and 140.")

        if P > 145:
           raise ValueError("Phosphorus must be between 0 and 145.")

        if K > 205:
            raise ValueError("Potassium must be between 0 and 205.")

        if humidity < 0 or humidity > 100:
            raise ValueError("Humidity must be between 0 and 100.")

        if ph < 0 or ph > 14:
            raise ValueError("pH must be between 0 and 14.")

        if rainfall < 0:
            raise ValueError("Rainfall cannot be negative.")
        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        mx_features = mx.transform(single_pred)
        prediction = model.predict(mx_features)

        crop_dict = {
            1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
            8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
            14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
            19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
        }

        if prediction[0] in crop_dict:
            crop = crop_dict[prediction[0]]
            result = f"{crop} is the best crop to be cultivated right there"
        else:
            result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
    except KeyError as e:
        result = f"Form field missing: {str(e)}. Check form names match app1.py."
    except ValueError as e:
        result = f"Invalid input: {str(e)}. Enter numbers only."
    except Exception as e:
        result = f"Unexpected error: {str(e)}"

    return render_template('log2.html', result=result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Change to 5001 if port conflict