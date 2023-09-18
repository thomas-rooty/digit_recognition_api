# Handwritten Digit Recognition Web App

![Django](https://img.shields.io/badge/Django-3.2-green.svg)
![Python](https://img.shields.io/badge/Python-3.8-blue.svg)

This Django web application recognizes handwritten digits using a trained AI model. Users can upload images of handwritten digits, and the app will predict and display the recognized digit.

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Demo

Todo le loup

## Features

- Upload and recognize handwritten digits.
- Utilizes a trained AI model for accurate digit recognition.
- RESTful API endpoint for programmatic access.
- Customizable and extendable for different recognition models.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/thomas-rooty/digit_recognition_api.git
   cd digit_recognition_api
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   ```
   
## Load the model

Place the trained .pkl file in the ai_model folder, named lenet_model.pkl
   
## Usage

1. Start the Django development server:

   ```bash
   python manage.py runserver
   ```
   
2. Access the app in your web browser at http://localhost:8000.
3. Upload an image of a handwritten digit to recognize it via form-data.
