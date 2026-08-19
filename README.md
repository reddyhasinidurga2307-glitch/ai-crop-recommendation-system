# AI-Based Crop Recommendation System



An AI-powered web application that recommends a suitable crop for cultivation based on soil and environmental conditions.



## Project Overview



The AI-Based Crop Recommendation System uses a machine learning model to recommend a suitable crop based on seven input parameters:



- Nitrogen (N)

- Phosphorus (P)

- Potassium (K)

- Temperature

- Humidity

- Soil pH

- Rainfall



The application provides a simple web interface where users can enter these values and receive a crop recommendation.



## Objective



The main objective of this project is to help farmers and agricultural users make better crop-selection decisions using machine learning and environmental data.



## Machine Learning



The trained machine learning model is stored in:



- model.pkl - trained crop prediction model

- minmaxscaler.pkl - feature scaling model



Before prediction, the input features are transformed using the saved MinMaxScaler and then passed to the trained model.



## Supported Crops



The application can recommend the following crops:



- Rice

- Maize

- Jute

- Cotton

- Coconut

- Papaya

- Orange

- Apple

- Muskmelon

- Watermelon

- Grapes

- Mango

- Banana

- Pomegranate

- Lentil

- Blackgram

- Mungbean

- Mothbeans

- Pigeonpeas

- Kidneybeans

- Chickpea

- Coffee



## Technologies Used



- Python

- Flask

- NumPy

- Pandas

- Scikit-learn

- HTML

- Jupyter Notebook

- Git and GitHub



## Project Structure



ai-crop-recommendation-system/

|

|-- app1.py

|-- Crop_recommendation.csv

|-- crop.ipynb.ipynb

|-- model.pkl

|-- minmaxscaler.pkl

|-- requirements.txt

|-- README.md

|-- .gitignore

|

|-- templates/

&#x20;   |-- log2.html



## Installation



### 1. Clone the repository



git clone https://github.com/reddyhasinidurga2307-glitch/ai-crop-recommendation-system.git



### 2. Open the project directory



cd ai-crop-recommendation-system



### 3. Create a virtual environment



python -m venv venv



### 4. Activate the virtual environment



For Windows:



venvScriptsactivate



### 5. Install dependencies



pip install -r requirements.txt



## Run the Application



Start the Flask application:



python app1.py



The application will run locally at:



http://127.0.0.1:5000



Open this address in a web browser to use the crop recommendation system.



## Example Input



Example soil and environmental conditions:



Nitrogen: 90

Phosphorus: 42

Potassium: 43

Temperature: 20.8

Humidity: 82

pH: 6.5

Rainfall: 202



## Example Output



Orange is the best crop to be cultivated right there



## Dataset



The project uses Crop_recommendation.csv as the dataset for crop recommendation.



The dataset contains soil and environmental attributes associated with different crops.



## Prediction Workflow



User Input

|

v

Web Form

|

v

Flask Application

|

v

Input Feature Scaling

|

v

Trained Machine Learning Model

|

v

Crop Prediction

|

v

Recommendation Displayed



## Future Improvements



Possible future improvements include:



- Weather API integration

- Location-based recommendations

- Improved user interface

- Online deployment

- Multilingual support

- Crop cultivation guidance

- Fertilizer recommendations

- Model evaluation and comparison



## Author



Hasini Durga



## License



This project is intended for educational and project-development purposes.


