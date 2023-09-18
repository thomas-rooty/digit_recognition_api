import pickle
import os


def load_digit_recognition_model():
  # Define the path to your .pkl file
  model_file_path = os.path.join('ai_model', 'lenet_model.pkl')

  if os.path.exists(model_file_path):
    with open(model_file_path, 'rb') as model_file:
      model = pickle.load(model_file)
    return model
  else:
    raise FileNotFoundError("The model file 'lenet_model.pkl' was not found.")
