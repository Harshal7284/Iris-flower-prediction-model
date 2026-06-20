# Iris Flower Classification Web App 🌸

This project is an end-to-end Machine Learning web application that predicts the species of an Iris flower based on its sepal and petal measurements. It features a model trained on the classic Iris dataset using XGBoost, and it is served through a web interface built with Flask and HTML/CSS.

## 📂 Project Structure

* **`app.py`**: The main Flask application file. It loads the pre-trained machine learning model, renders the frontend interface, and handles prediction requests from the web form.
* **`Flower_classification_prediction .ipynb`**: A Jupyter Notebook containing the data exploration, model training, and evaluation steps. This script processes the raw data and exports the finalized XGBoost model.
* **`flower_model.pkl`**: The serialized (pickled) XGBoost machine learning model generated from the Jupyter notebook. This is used by the Flask app to make real-time predictions.
* **`Iris.csv`**: The dataset used to train the model, containing 150 records of Iris flowers with their corresponding Sepal Length, Sepal Width, Petal Length, Petal Width, and Species.
* **`index.html`**: The frontend user interface. It contains a responsive web form where users can input flower measurements to get a classification result.

## 🚀 Features

* **Machine Learning Model:** Utilizes a highly accurate XGBoost Classifier.
* **Interactive Web UI:** Clean, user-friendly HTML form to input flower dimensions.
* **Instant Predictions:** Real-time classification mapping numerical inputs to species names (*Iris-setosa*, *Iris-versicolor*, or *Iris-virginica*).

## 🛠️ Prerequisites

To run this project locally, you will need Python installed on your machine along with the following libraries:

* `Flask`
* `pandas`
* `xgboost`
* `scikit-learn` 

You can install the required packages using pip:
```bash
pip install Flask pandas xgboost scikit-learn
